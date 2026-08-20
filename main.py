from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
import uvicorn, os

app = FastAPI()

# 🔧 حط هنا أكواد الأفلييت حقك بعد ما تسجل
MY_AFFILIATE = {
    "amazon": "nawaf-21",  # من Amazon Associates
    "noon": "YOUR_ARABCLICKS_ID",  # من ArabClicks
    "temu": "YOUR_TEMU_ID"
}

# قاعدة منتجات تجريبية - أنت تقدر تضيف من كل المنصات
products = [
    {"name": "ساعة ذكية", "noon_price": 199, "amazon_price": 189, "temu_price": 89, "best": "temu", "image": "⌚", "rating": 4.7},
    {"name": "سماعة بلوتوث", "noon_price": 149, "amazon_price": 129, "temu_price": 59, "best": "temu", "image": "🎧", "rating": 4.5},
    {"name": "ايفون 15", "noon_price": 3299, "amazon_price": 3199, "temu_price": 0, "best": "amazon", "image": "📱", "rating": 4.9},
]

def get_aff_link(store, product_name):
    # هنا يتركب رابط الأفلييت حقك تلقائي
    base = f"https://www.{store}.com/s?k={product_name.replace(' ', '+')}"
    if store == "amazon":
        return f"{base}&tag={MY_AFFILIATE['amazon']}"
    return base  # لباقي المتاجر من ArabClicks

@app.get("/", response_class=HTMLResponse)
def home(q: str = ""):
    q_lower = q.lower()
    filtered = [p for p in products if q_lower in p["name"].lower()] if q else products
    
    cards = ""
    for p in filtered:
        cards += f"""
        <div class="card">
            <div style="font-size:40px">{p['image']}</div>
            <h2>{p['name']} ⭐ {p['rating']}</h2>
            <div class="prices">
                <div class="price {'best' if p['best']=='noon' else ''}">نون: {p['noon_price']} ريال <a href="{get_aff_link('noon', p['name'])}" target="_blank" class="buy">شراء</a></div>
                <div class="price {'best' if p['best']=='amazon' else ''}">أمازون: {p['amazon_price']} ريال <a href="{get_aff_link('amazon', p['name'])}" target="_blank" class="buy">شراء - أرخص</a></div>
                {f"<div class='price {'best' if p['best']=='temu' else ''}'>تيمو: {p['temu_price']} ريال <a href='{get_aff_link('temu', p['name'])}' target='_blank' class='buy'>شراء</a></div>" if p['temu_price']>0 else ""}
            </div>
            <div class="badge">💰 عمولتك: 10% من أي متجر يختاره العميل</div>
        </div>
        """

    return f"""
    <html dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
    <title>سوق نواف الشامل - قارن أسعار كل المتاجر</title>
    <style>
        body{{font-family:Tahoma;background:#0f172a;color:white;margin:0}}
        .header{{background:linear-gradient(90deg,#3b82f6,#10b981);padding:20px;text-align:center}}
        .search-box{{background:#1e293b;padding:20px;text-align:center;position:sticky;top:0;z-index:10}}
        .search-box input{{width:70%;padding:15px;border-radius:30px;border:none;font-size:18px;text-align:center}}
        .search-box button{{padding:15px 25px;border-radius:30px;border:none;background:#f59e0b;color:white;font-weight:bold;cursor:pointer;margin-right:10px}}
        .container{{max-width:900px;margin:auto;padding:15px}}
        .card{{background:#1e293b;margin:15px 0;padding:20px;border-radius:15px;border:1px solid #334155}}
        .prices{{display:flex;flex-direction:column;gap:10px;margin:15px 0}}
        .price{{background:#0f172a;padding:12px;border-radius:10px;display:flex;justify-content:space-between;align-items:center}}
        .price.best{{border:2px solid #10b981;background:#052e1a}}
        .buy{{background:#10b981;color:white;padding:8px 15px;border-radius:8px;text-decoration:none}}
        .badge{{background:#334155;padding:5px 10px;border-radius:20px;font-size:12px;color:#94a3b8}}
        .add-form{{background:#1e293b;padding:20px;border-radius:15px;margin:20px 0}}
        .add-form input{{width:90%;padding:12px;margin:8px;border-radius:8px;border:1px solid #334155;background:#0f172a;color:white}}
        .btn{{background:#3b82f6;color:white;padding:12px 20px;border:none;border-radius:8px;cursor:pointer}}
    </style></head>
    <body>
        <div class="header">
            <h1>🛒 سوق نواف الشامل</h1>
            <p>ابحث مرة وحدة - نقارن لك السعر في نون وأمازون وتيمو وشي إن و 1000 متجر!</p>
            <p>🇸🇦 عربي | 🇺🇸 English | 🌍 يستهدف العالم كله</p>
        </div>
        <div class="search-box">
            <form method="get">
                <input name="q" value="{q}" placeholder="وش تبي تشتري؟ مثلا: ساعة، ايفون، سماعة...">
                <button type="submit">🔍 قارن الأسعار</button>
            </form>
        </div>
        <div class="container">
            <h2>🔥
