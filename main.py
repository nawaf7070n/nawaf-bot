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
.header { background: linear-gradient(to bottom, #1e3a8a, #1e40af); padding:30px; text-align:center; }
.header h1 { margin:0; font-size:32px; letter-spacing:2px; }
.header p { margin:10px 0 0; opacity:0.8; }
.search-box { background:#1e293b; padding:20px; display:flex; gap:10px; justify-content:center; }
.search-box input { width:60%; padding:12px; border-radius:8px; border:none; font-size:16px; }
.search-box button { background:#ef4444; color:white; border:none; padding:12px 20px; border-radius:8px; cursor:pointer; }
.products { padding:20px; }
.product { background:#1e293b; padding:15px; border-radius:10px; margin:15px 0; }
.price { color:#94a3b8; }
.best { color:#22d3ee; font-weight:bold; }
.btn { padding:8px 15px; border-radius:6px; border:none; margin:5px; cursor:pointer; }
.btn-noon { background:#f59e0b; }
.btn-amazon { background:#10b981; color:white; }
</style>
</head>
<body>
<div class="header">
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
<h3>ساعة ذكية</h3>
<p class="price">نون: 199 ريال | امازون: 189 ريال</p>
<p class="best">الارخص: amazon</p>
<button class="btn btn-noon">اشتر من نون</button>
<button class="btn btn-amazon">اشتر من امازون</button>
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
    return {"status": "ok"}
