from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

HTML_PAGE = """
<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BESTDEAL - أفضل صفقة</title>
<style>
body { margin:0; font-family: Tahoma; background:#0f172a; color:white; }
.header { background: linear-gradient(180deg,#1e3a8a,#1e40af); padding:35px 20px; text-align:center; }
.header h1 { margin:0; font-size:38px; letter-spacing:3px; }
.header p { margin:8px 0 0; font-size:22px; opacity:0.9; }
.search-box { background:#1e293b; padding:20px; display:flex; gap:10px; justify-content:center; }
.search-box input { width:60%; max-width:400px; padding:12px; border-radius:10px; border:none; }
.search-box button { background:#ff7a00; color:white; border:none; padding:12px 25px; border-radius:10px; font-weight:bold; }
.products { padding:20px; max-width:900px; margin:auto; }
.product { background:#1e293b; padding:18px; border-radius:14px; margin:15px 0; display:flex; justify-content:space-between; }
</style>
</head>
<body>
<div class="header">
<img src="https://raw.githubusercontent.com/nawaf7070n/nawaf-bot/main/logo.png" style="height:75px; margin-bottom:10px;" onerror="this.style.display='none'">
<h1>BESTDEAL</h1>
<p>أفضل صفقة</p>
</div>
<div class="search-box">
<input placeholder="ابحث: ساعة، ايفون...">
<button>بحث</button>
</div>
<div class="products">
<h2>المنتجات (3)</h2>
<div class="product">
<div>
<h3>ساعة ذكية</h3>
<p style="color:#94a3b8;">نون: 199 | امازون: 189</p>
<p style="color:#22d3ee; font-weight:bold;">الأرخص: امازون</p>
</div>
<div>
<button style="background:#f59e0b; padding:10px 15px; border:none; border-radius:8px; font-weight:bold;">نون</button>
<button style="background:#10b981; color:white; padding:10px 15px; border:none; border-radius:8px; font-weight:bold;">امازون</button>
</div>
</div>
</div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return HTML_PAGE

@app.get("/health")
def health():
    return {"status":"ok"}
