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
.header{background:#0a0a0a;padding:35px 20px;text-align:center;border-bottom:2px solid #ff6a00}
.logo-icon{font-size:70px;display:block;margin-bottom:10px}
.header h1{margin:0;font-size:44px;font-weight:900}
.header h1 span{color:#ff6a00}
.header p{margin:10px 0 0;color:#aaa;font-size:19px}
.container{max-width:900px;margin:0 auto;padding:20px}
.search{display:flex;gap:10px;margin:25px 0;background:#151515;padding:12px;border-radius:16px;border:1px solid #222}
.search input{flex:1;padding:14px;border-radius:12px;border:1px solid #333;background:#0f0f0f;color:#fff}
.search button{padding:14px 28px;border-radius:12px;border:none;background:#ff6a00;color:#fff;font-weight:800}
.footer{text-align:center;padding:30px;color:#555;border-top:1px solid #1a1a1a;margin-top:30px}
</style>
</head>
<body>
<div class="header">
<div class="logo-icon">🛒🏷️</div>
<h1><span>أفضل</span> صفقة</h1>
<p>نقارن الأسعار ونجيب لك الأرخص</p>
</div>
<div class="container">
<div class="search">
<input placeholder="ابحث: ايفون، ساعة، لابتوب...">
<button>بحث</button>
</div>
<div class="footer">أفضل صفقة © 2026 - نقارن الأسعار ونجيب لك الأرخص</div>
</div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTML
