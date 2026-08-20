from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()
HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>أفضل صفقة</title>
<style>
body{margin:0;font-family:system-ui;background:#080808;color:#fff}
.header{background:#0a0a0a;padding:30px;text-align:center;border-bottom:2px solid #ff6a00}
.header h1{font-size:42px;margin:0} .header h1 span{color:#ff6a00}
.header p{color:#aaa;margin-top:8px}
.container{max-width:900px;margin:0 auto;padding:15px}
.search{display:flex;gap:8px;background:#151515;padding:10px;border-radius:12px}
.search input{flex:1;padding:12px;border-radius:8px;border:1px solid #333;background:#000;color:#fff}
.search button{padding:12px 22px;border-radius:8px;border:none;background:#ff6a00;color:#fff;font-weight:800}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:15px}
.card{background:#151515;border:1px solid #222;border-radius:12px;padding:12px}
.price{color:#ff6a00;font-weight:800}
</style>
</head>
<body>
<div class="header"><div style="font-size:50px">🛒</div><h1><span>أفضل</span> صفقة</h1><p>نقارن الأسعار ونجيب لك الأرخص</p></div>
<div class="container">
<div class="search"><input id="q" placeholder="ايفون، ساعة، لابتوب..."><button onclick="doSearch()">بحث</button></div>
<div id="grid" class="grid"></div>
</div>
<script>
let items=[
{name:"ايفون 15 برو ماكس - 256GB",price:"4299 ر.س",shop:"جرير"},
{name:"ايفون 15 عادي",price:"3299 ر.س",shop:"اكسترا"},
{name:"ساعة ذكية T800",price:"79 ر.س",shop:"نون"},
{name:"ساعة ابل 9",price:"1599 ر.س",shop:"جرير"},
{name:"لابتوب HP",price:"2299 ر.س",shop:"امازون"},
{name:"ايربودز برو",price:"699 ر.س",shop:"نون"},
{name:"شاحن انكر سريع",price:"59 ر.س",shop:"امازون"},
{name:"سماعة بلوتوث",price:"89 ر.س",shop:"نون"}
];
function show(list){
let g=document.getElementById('grid');
g.innerHTML='';
if(list.length==0){g.innerHTML='<p style=color:#777;text-align:center;grid-column:1/3>ما لقينا نتائج - جرب كلمة ثانية</p>';return}
list.forEach(p=>{g.innerHTML+=`<div class=card><b>${p.name}</b><div class=price>${p.price}</div><div style=color:#777;font-size:12px>${p.shop}</div></div>`});
}
function doSearch(){
let v=document.getElementById('q').value.trim();
if(v==''){show(items);return}
let f=items.filter(x=>x.name.includes(v));
show(f);
}
show(items);
</script>
</body>
</html>
"""
@app.get("/", response_class=HTMLResponse)
async def home(): return HTML
