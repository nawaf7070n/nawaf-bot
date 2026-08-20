from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import os
import uvicorn

app = FastAPI()

# منتجات تجريبية - مجمع شامل
products = [
    {"name": "ساعة ذكية", "noon": 199, "amazon": 189, "best": "amazon"},
    {"name": "سماعة بلوتوث", "noon": 149, "amazon": 129, "best": "amazon"},
    {"name": "ايفون 15", "noon": 3299, "amazon": 3199, "best": "amazon"},
]

@app.get("/", response_class=HTMLResponse)
def home(q: str = ""):
    filtered = [p for p in products if q.lower() in p["name"].lower()] if q else products
    cards_html = ""
    for p in filtered:
        cards_html += f"""
        <div style="background:#1e293b;margin:10px;padding:15px;border-radius:10px;border:1px solid #334155">
            <h3>{p['name']}</h3>
            <p>نون: {p['noon']} ريال | امازون: {p['amazon']} ريال</p>
            <p style="color:#10b981">الارخص: {p['best']}</p>
            <a href="https://www.amazon.sa/s?k={p['name']}" target="_blank" style="background:#10b981;color:white;padding:8px 12px;border-radius:5px;text-decoration:none">اشتر من امازون</a>
            <a href="https://www.noon.com/saudi-ar/search?q={p['name']}" target="_blank" style="background:#f59e0b;color:white;padding:8px 12px;border-radius:5px;text-decoration:none">اشتر من نون</a>
        </div>
        """

    return f"""
    <html dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
    <title>سوق نواف الشامل</title>
    <style>body{{font-family:Tahoma;background:#0f172a;color:white;margin:0;padding:0}} .header{{background:#3b82f6;padding:20px;text-align:center}} .container{{max-width:800px;margin:auto;padding:15px}} input{{width:70%;padding:12px;border-radius:8px;border:none}} button{{padding:12px;background:#f59e0b;color:white;border:none;border-radius:8px}}</style>
    </head><body>
    <div class="header"><h1>سوق نواف الشامل</h1><p>قارن الاسعار من كل المتاجر</p></div>
    <div class="container">
        <form method="get" style="text-align:center;margin:20px"><input name="q" value="{q}" placeholder="ابحث: ساعة، ايفون..."><button type="submit">بحث</button></form>
        <h2>المنتجات ({len(filtered)})</h2>
        {cards_html}
        <hr style="margin:20px 0">
        <h3>اضف منتج جديد</h3>
        <form action="/add" method="post"><input name="name" placeholder="اسم المنتج" required><input name="noon" placeholder="سعر نون" type="number" required><input name="amazon" placeholder="سعر امازون" type="number" required><button type="submit">اضف</button></form>
    </div></body></html>
    """

@app.post("/add", response_class=HTMLResponse)
def add(name: str = Form(...), noon: int = Form(...), amazon: int = Form(...)):
    best = "amazon" if amazon < noon else "noon"
    products.insert(0, {"name": name, "noon": noon, "amazon": amazon, "best": best})
    return '<html><head><meta http-equiv="refresh" content="1;url=/"></head><body>تمت الاضافة - جاري التحويل...</body></html>'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
