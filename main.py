from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import os, uvicorn
app = FastAPI()
products = [
    {"name": "ساعة ذكية Smart Watch", "noon": 199, "amazon": 189, "best": "amazon"},
    {"name": "سماعة بلوتوث Bluetooth", "noon": 149, "amazon": 129, "best": "amazon"},
    {"name": "ايفون 15 iPhone 15", "noon": 3299, "amazon": 3199, "best": "amazon"},
]
@app.get("/", response_class=HTMLResponse)
def home(q: str = ""):
    filtered = [p for p in products if q.lower() in p["name"].lower()] if q else products
    cards=""
    for p in filtered:
        cards+=f"""<div style="background:#1e293b;margin:10px;padding:15px;border-radius:12px;border:1px solid #334155"><h3>{p['name']}</h3><p>نون: {p['noon']} ر.س | أمازون: {p['amazon']} ر.س</p><p style="color:#10b981">🏆 الأرخص: {p['best']}</p><a href="https://www.amazon.sa/s?k={p['name']}" target="_blank" style="background:#ff6a00;color:white;padding:8px 12px;border-radius:6px;text-decoration:none;margin-left:5px">BESTDEAL Amazon</a><a href="https://www.noon.com/saudi-ar/search?q={p['name']}" target="_blank" style="background:#f59e0b;color:white;padding:8px 12px;border-radius:6px;text-decoration:none">BESTDEAL Noon</a></div>"""
    return f"""<html dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>BESTDEAL - أفضل صفقة | Best Deals From All Stores</title><style>body{{font-family:Tahoma;background:#0f172a;color:white;margin:0}} .header{{background:linear-gradient(90deg,#000,#ff6a00);padding:25px;text-align:center}} .container{{max-width:850px;margin:auto;padding:15px}} input{{width:65%;padding:14px;border-radius:30px;border:none;text-align:center}} button{{padding:14px 20px;border-radius:30px;border:none;background:#ff6a00;color:white;font-weight:bold}}</style></head><body><div class="header"><h1 style="margin:0;font-size:40px">BEST<span style="color:#ff6a00">DEAL</span></h1><h2 style="margin:5px 0">أفضل صفقة</h2><p>Find The BEST DEAL From 1000+ Stores | قارن أسعار كل المتاجر ووفر</p></div><div class="container"><form method="get" style="text-align:center;margin:20px"><input name="q" value="{q}" placeholder="ابحث: ساعة، ايفون، Search: watch, iPhone..."><button type="submit">🔍 قارن</button></form><h3>المنتجات ({len(filtered)}) - Products</h3>{cards}<hr style="margin:25px 0"><div style="background:#052e1a;padding:15px;border-radius:10px"><h3>💰 BESTDEAL - كيف تربح؟</h3><p>1. سجل في Amazon Associates + ArabClicks</p><p>2. أي عميل يضغط ويشتري = عمولة 10% لك تلقائي!</p><p>🌍 براند عالمي: BESTDEAL يشتغل عربي + إنجليزي</p></div></div></body></html>"""
@app.post("/add", response_class=HTMLResponse)
def add(name: str = Form(...), noon: int = Form(...), amazon: int = Form(...)):
    best="amazon" if amazon<noon else "noon"; products.insert(0, {"name": name, "noon": noon, "amazon": amazon, "best": best}); return '<html><head><meta http-equiv="refresh" content="1;url=/"></head><body>تمت الإضافة ✅</body></html>'
if __name__ == "__main__": uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
