from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

HTML = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>أفضل صفقة - نقارن الأسعار ونجيب لك الأرخص</title>
<style>
body{margin:0;font-family:system-ui;background:#080808;color:#fff}
.header{background:#0a0a0a;padding:30px 20px;text-align:center;border-bottom:2px solid #ff6a00}
.header h1{margin:10px 0 0;font-size:40px;font-weight:900}
.header h1 span{color:#ff6a00}
.header p{color:#aaa;font-size:18px;margin-top:8px}
.container{max-width:900px;margin:0 auto;padding:20px}
.search{display:flex;gap:10px;margin:20px 0;background:#151515;padding:12px;border-radius:14px;border:1px solid #222}
.search input{flex:1;padding:14px;border-radius:10px;border:1px solid #333;background:#0f0f0f;color:#fff;font-size:16px}
.search button{padding:14px 28px;border-radius:10px;border:none;background:#ff6a00;color:#fff;font-weight:800;cursor:pointer}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:15px;margin-top:20px}
.card{background:#141414;border:1px solid #222;border-radius:14px;padding:16px}
.card h3{margin:0 0 8px}
.price{color:#ff6a00;font-weight:800;font-size:20px}
.store{color:#777;font-size:13px;margin-top:5px}
.no-results{text-align:center;color:#777;margin-top:30px;display:none}
.footer{text-align:center;padding:30px;color:#555;border-top:1px solid #1a1a1a;margin-top:30px}
</style>
</head>
<body>
<div class="header">
<div style="font-size:60px">🛒🏷️</div>
<h1><span>أفضل</span> صفقة</h1>
<p>نقارن الأسعار ونجيب لك الأرخص</p>
</div>
<div class="container">
<div class="search">
<input id="q" placeholder="ابحث: ايفون، ساعة، لابتوب..." onkeyup="if(event.key==='Enter')search()">
<button onclick="search()">بحث</button>
</div>
<div id="cards" class="cards"></div>
<div id="no" class="no-results">ما لقينا شي.. جرب كلمة ثانية</div>
<div class="footer">أفضل صفقة © 2026</div>
</div>
<script>
const products=[
{name:"ايفون 15 برو ماكس",price:"4299 ر.س",store:"جرير + اكسترا + نون"},
{name:"ساعة ذكية",price:"199 ر.س",store:"امازون + نون"},
{name:"لابتوب HP",price:"2499 ر.س",store:"جرير"},
{name:"سماعة بلوتوث",price:"89 ر.س",store:"نون + امازون"},
{name:"ستاند جوال",price:"25 ر.س",store:"امازون"},
{name:"ايربودز برو",price:"799 ر.س",store:"اكسترا"},
{name:"شاحن سريع",price:"49 ر.س",store:"نون"}
];
function render(list){
 const c=document.getElementById('cards');
 const n=document.getElementById('no');
 c.innerHTML='';
 if(list.length===0){n.style.display='block';return}
 n.style.display='none';
 list.forEach(p=>{
  c.innerHTML+=`<div class="card"><h3>${p.name}</h3><div class="price">${p.price}</div><div class="store">${p.store}</div></div>`;
 });
}
function search(){
 let q=document.getElementById('q').value.trim();
 if(!q){render(products);return}
 let f=products.filter(p=>p.name.includes(q));
 render(f);
}
render(products);
</script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTML
