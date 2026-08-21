from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()
HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>BESTDEAL - نقارن الأسعار ونجيب لك الأرخص</title>
<style>
body{margin:0;font-family:system-ui;background:#080808;color:#fff}
.header{background:#0a0a0a;padding:35px;text-align:center;border-bottom:3px solid #ff6a00}
.header h1{font-size:48px;margin:10px 0 0;letter-spacing:2px;color:#ff6a00;font-weight:900}
.header p{color:#bbb;margin-top:8px;font-size:18px}
.container{max-width:900px;margin:0 auto;padding:15px}
.search{display:flex;gap:8px;background:#151515;padding:12px;border-radius:14px;border:1px solid #222}
.search input{flex:1;padding:13px;border-radius:10px;border:1px solid #333;background:#000;color:#fff;font-size:16px}
.search button{padding:13px 26px;border-radius:10px;border:none;background:#ff6a00;color:#fff;font-weight:900;cursor:pointer}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:18px}
.card{background:#141414;border:1px solid #222;border-radius:12px;padding:14px}
.card b{display:block;margin-bottom:6px}
.price{color:#ff6a00;font-weight:800;font-size:18px}
.footer{text-align:center;padding:30px;color:#555;border-top:1px solid #1a1a1a;margin-top:30px}
</style>
</head>
<body>
<div class="header"><div style="font-size:60px">🛒</div><h1>BESTDEAL</h1><p>نقارن الأسعار ونجيب لك الأرخص</p></div>
<div class="container">
<div class="search"><input id="q" placeholder="ابحث: ايفون، ساعة، لابتوب..."><button onclick="doSearch()">بحث</button></div>
<div id="grid" class="grid"></div>
</div>
<div class="footer">BESTDEAL © 2026 - bestdeal.onrender.com</div>
<script>
let items=[
{name:"ايفون 15 برو ماكس",price:"4299 ر.س",shop:"جرير"},
{name:"ايفون 15",price:"3299 ر.س",shop:"اكسترا"},
{name:"ساعة T800",price:"79 ر.س",shop:"نون"},
{name:"ساعة ابل",price:"1599 ر.س",shop:"جرير"},
{name:"لابتوب HP",price:"2299 ر.س",shop:"امازون"},
{name:"ايربودز",price:"699 ر.س",shop:"نون"},
{name:"شاحن سريع",price:"59 ر.س",shop:"امازون"},
{name:"سماعة بلوتوث",price:"89 ر.س",shop:"نون"}
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
