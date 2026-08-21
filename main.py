from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()
HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>BESTDEAL - أفضل صفقة</title>
<style>
body{margin:0;font-family:system-ui;background:#080808;color:#fff}
.header{background:#0a0a0a;padding:35px 20px;text-align:center;border-bottom:3px solid #ff6a00}
.header h1{font-size:52px;margin:0;color:#ff6a00;font-weight:900;letter-spacing:2px}
.header .ar{font-size:34px;margin:10px 0 0;color:#fff;font-weight:800}
.header .slogan{color:#aaa;margin-top:8px;font-size:16px}
.container{max-width:900px;margin:0 auto;padding:15px}
.search{display:flex;gap:8px;background:#151515;padding:12px;border-radius:14px;border:1px solid #222}
.search input{flex:1;padding:13px;border-radius:10px;border:1px solid #333;background:#000;color:#fff}
.search button{padding:13px 26px;border-radius:10px;border:none;background:#ff6a00;color:#fff;font-weight:900}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:18px}
.card{background:#141414;border:1px solid #222;border-radius:12px;padding:14px}
.price{color:#ff6a00;font-weight:800}
</style>
</head>
<body>
<div class="header">
<div style="font-size:55px">🛒</div>
<h1>BESTDEAL</h1>
<div class="ar">أفضل صفقة</div>
<div class="slogan">نقارن الأسعار ونجيب لك الأرخص</div>
</div>
<div class="container">
<div class="search"><input id="q" placeholder="ابحث: ايفون، ساعة..."><button onclick="doSearch()">بحث</button></div>
<div id="grid" class="grid"></div>
</div>
<script>
let items=[
{name:"ايفون 15 برو ماكس",price:"4299 ر.س",shop:"جرير"},
{name:"ايفون 15",price:"3299 ر.س",shop:"اكسترا"},
{name:"ساعة ذكية",price:"79 ر.س",shop:"نون"},
{name:"لابتوب HP",price:"2299 ر.س",shop:"امازون"}
];
function show(list){
let g=document.getElementById('grid');g.innerHTML='';
if(list.length==0){g.innerHTML='<p style=color:#777;grid-column:1/3;text-align:center>ما لقينا نتائج</p>';return}
list.forEach(p=>{g.innerHTML+=`<div class=card><b>${p.name}</b><div class=price>${p.price}</div><div style=color:#777;font-size:12px>${p.shop}</div></div>`});
}
function doSearch(){
let v=document.getElementById('q').value.trim();
if(!v){show(items);return}
show(items.filter(x=>x.name.includes(v)));
}
show(items);
</script>
</body>
</html>
"""
@app.get("/", response_class=HTMLResponse)
async def home(): return HTML
