import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# ===== غيّر الاسم هنا فقط =====
SITE_NAME = "BESTDEAL"
SITE_SUBTITLE = "أفضل صفقة"
BOT_USERNAME = "@MowafirAlas3ar_bot"
# ============================

PAGE_HTML = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{SITE_NAME} - {SITE_SUBTITLE}</title>
<style>
body{{margin:0;font-family:system-ui;background:#0a0a0a;color:#fff}}
.header{{background:linear-gradient(180deg,#0f0f0f,#1a1a1a);padding:35px 20px;text-align:center;border-bottom:1px solid #2a2a2a}}
.header img{{width:110px;background:transparent;filter:drop-shadow(0 4px 12px rgba(0,0,0,0.5));margin-bottom:12px}}
.header h1{{margin:10px 0 5px;font-size:42px;font-weight:900;letter-spacing:1px}}
.header p{{margin:0;color:#ff8c00;font-size:18px;font-weight:600}}
.container{{max-width:900px;margin:0 auto;padding:20px}}
.search-box{{display:flex;gap:10px;margin:20px 0}}
.search-box input{{flex:1;padding:14px;border-radius:12px;border:1px solid #333;background:#1a1a1a;color:#fff;font-size:16px}}
.search-box button{{padding:14px 28px;border-radius:12px;border:none;background:#ff6a00;color:#fff;font-weight:700;cursor:pointer}}
</style>
</head>
<body>
<div class="header">
<img src="https://raw.githubusercontent.com/nawaf7070n/nawaf-bot/main/logo.png" onerror="this.style.display='none'" alt="logo">
<h1>{SITE_NAME}</h1>
<p>{SITE_SUBTITLE}</p>
</div>
<div class="container">
<div class="search-box">
<input placeholder="ابحث: ايفون، ساعة، لابتوب...">
<button>بحث</button>
</div>
<p style="text-align:center;color:#888">بوت التليجرام: {BOT_USERNAME}</p>
</div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    return PAGE_HTML
