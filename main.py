import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

SITE_NAME = "أفضل صفقة"
SITE_NAME_EN = "BESTDEAL"
BOT_USERNAME = "@MowafirAlas3ar_bot"
LOGO_URL = "https://raw.githubusercontent.com/nawaf7070n/nawaf-bot/main/logo.png"

HTML_PAGE = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{SITE_NAME} - {SITE_NAME_EN}</title>
<style>
*{{box-sizing:border-box}}
body{{margin:0;font-family:'Segoe UI',system-ui;background:#080808;color:#fff;min-height:100vh}}
.header{{background:linear-gradient(180deg,#0a0a0a 0%,#141414 100%);padding:40px 20px 30px;text-align:center;border-bottom:2px solid #ff6a00;position:relative}}
.header::after{{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,#ff6a00,transparent)}}
.header img{{width:120px;height:auto;background:transparent;margin-bottom:15px;filter:drop-shadow(0 2px 10px rgba(255,106,0,0.3))}}
.header h1{{margin:0;font-size:46px;font-weight:900;letter-spacing:1px;color:#fff}}
.header h1 span{{color:#ff6a00}}
.header p{{margin:8px 0 0;color:#aaa;font-size:18px}}
.container{{max-width:1000px;margin:0 auto;padding:25px 20px}}
.search-box{{display:flex;gap:10px;margin:30px 0;background:#151515;padding:12px;border-radius:16px;border:1px solid #222}}
.search-box input{{flex:1;padding:15px 18px;border-radius:12px;border:1px solid #2a2a2a;background:#0f0f0f;color:#fff;font-size:16px;outline:none}}
.search-box input:focus{{border-color:#ff6a00}}
.search-box button{{padding:15px 32px;border-radius:12px;border:none;background:linear-gradient(135deg,#ff6a00,#ff8c00);color:#fff;font-weight:800;font-size:16px;cursor:pointer}}
.products-title{{font-size:22px;font-weight:800;margin:30px 0 15px;color:#fff}}
.card{{background:#141414;border:1px solid #222;border-radius:16px;padding:18px;display:flex;gap:15px;margin-bottom:12px}}
.badge{{background:#1f1f1f;color:#ff8c00;padding:4px 10px;border-radius:20px;font-size:12px;font-weight:700}}
.footer{{text-align:center;padding:30px;color:#555;font-size:14px;margin-top:40px;border-top:1px solid #1a1a1a}}
.footer a{{color:#ff6a00;text-decoration:none}}
</style>
</head>
<body>
<div class="header">
<img src="{LOGO_URL}" onerror="this.style.display='none'" alt="logo">
<h1><span>أفضل</span> صفقة</h1>
<p>نلاقي لك أرخص سعر في السعودية</p>
</div>
<div class="container">
<div class="search-box">
<input id="q" placeholder="ابحث: ايفون، ساعة ذكية، لابتوب...">
<button onclick="search()">بحث</button>
</div>
<div class="products-title">المنتجات (3)</div>
<div class="card"><div><div class="badge">تم</div><h3>ساعة ذكية</h3></div></div>
<div class="card"><div><div class="badge">جديد</div><h3>سماعة بلوتوث</h3></div></div>
<div class="card"><div><div class="badge">عرض</div><h3>ستاند جوال</h3></div></div>
<div class="footer">بوت التليجرام: {BOT_USERNAME} | {SITE_NAME} © 2026<br><br><a href="https://t.me/{BOT_USERNAME.replace('@','')}">افتح البوت في تليجرام</a></div>
</div>
<script>
function search(){{let v=document.getElementById('q').value;if(v)alert('تبحث عن: '+v+' - قريبا ربط البحث الحقيقي')}}
</script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTML_PAGE

@app.get("/health")
async def health():
    return {"status":"ok","site":SITE_NAME}
