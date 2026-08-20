import os
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
.header{background:linear-gradient(180deg,#0a0a0a,#141414);padding:35px 20px;text-align:center;border-bottom:2px solid #ff6a00}
.header img{width:130px;background:transparent;mix-blend-mode:screen;filter:brightness(1.1);margin-bottom:10px}
.header h1{margin:0;font-size:42px;font-weight:900}
.header h1 span{color:#ff6a00}
.header p{margin:10px 0 0;color:#bbb;font-size:18px}
.container{max-width:1000px;margin:0 auto;padding:20px}
.search-box{display:flex;gap:10px;margin:25px 0;background:#151515;padding:12px;border-radius:16px;border:1px solid #222}
.search-box input{flex:1;padding:14px;border-radius:12px;border:1px solid #333;background:#0f0f0f;color:#fff}
.search-box button{padding:14px 28px;border-radius:12px;border:none;background:#ff6a00;color:#fff;font-weight:800}
</style>
</head>
<body>
<div class="header">
<img src="https://raw.githubusercontent.com/nawaf7070n/nawaf-bot/main/logo.png" style="background:transparent" alt="logo">
<h1><span>أفضل</span> صفقة</h1>
<p>نقارن الأسعار ونجيب لك الأرخص</p>
</div>
<div class="container">
<div style="display:flex;gap:10px;background:#151515;padding:12px;border-radius:16px">
<input style="flex:1;padding:14px;border-radius:12px;border:1px solid #333;background:#0f0f0f;color:#fff" placeholder="ابحث: ايفون، ساعة ذكية، لابتوب...">
<button style="padding:14px 28px;border-radius:12px;border:none;background:#ff6a00;color:#fff;font-weight:800">بحث</button>
</div>
</div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTML
