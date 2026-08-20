from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html dir="rtl">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>BESTDEAL - افضل صفقة</title>
        <style>
            body{font-family:Tahoma;background:#0f172a;color:white;margin:0}
            .header{background:#000;padding:30px;text-align:center;border-bottom:3px solid #ff6a00}
            .header h1{font-size:55px;margin:0;letter-spacing:2px}
            .header h1 span{color:#ff6a00}
            .header p{color:#aaa;margin-top:10px;font-size:18px}
            .container{max-width:800px;margin:auto;padding:20px}
            .card{background:#1e293b;margin:15px 0;padding:20px;border-radius:15px;border:1px solid #334155}
            .card h3{margin:0 0 10px 0}
            .price{color:#10b981;font-weight:bold;font-size:18px;margin:10px 0}
            .btn{display:inline-block;padding:10px 18px;border-radius:8px;text-decoration:none;color:white;margin:5px;font-weight:bold}
            .btn-amazon{background:#ff6a00} .btn-noon{background:#f59e0b}
            .footer{text-align:center;color:#64748b;margin:40px 0}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>BEST<span>DEAL</span></h1>
            <h2 style="margin:10px 0 0 0">أفضل صفقة</h2>
            <p>Find The BEST DEAL From 1000+ Stores | قارن ووفر</p>
        </div>
        <div class="container">
            <div class="card">
                <h3>⌚ ساعة ذكية Smart Watch</h3>
                <div class="price">نون: 199 ر.س | أمازون: 189 ر.س - الأرخص: أمازون 🏆</div>
                <a class="btn btn-amazon" href="https://www.amazon.sa/s?k=smart+watch" target="_blank">شراء من أمازون</a>
                <a class="btn btn-noon" href="https://www.noon.com/saudi-ar/search?q=smart+watch" target="_blank">شراء من نون</a>
            </div>
            <div class="card">
                <h3>🎧 سماعة بلوتوث Bluetooth</h3>
                <div class="price">نون: 149 ر.س | أمازون: 129 ر.س - الأرخص: أمازون 🏆</div>
                <a class="btn btn-amazon" href="https://www.amazon.sa/s?k=bluetooth" target="_blank">شراء من أمازون</a>
                <a class="btn btn-noon" href="https://www.noon.com/saudi-ar/search?q=bluetooth" target="_blank">شراء من نون</a>
            </div>
            <div class="card">
                <h3>📱 آيفون 15 iPhone 15</h3>
                <div class="price">نون: 3299 ر.س | أمازون: 3199 ر.س - الأرخص: أمازون 🏆</div>
                <a class="btn btn-amazon" href="https://www.amazon.sa/s?k=iphone+15" target="_blank">شراء من أمازون</a>
                <a class="btn btn-noon" href="https://www.noon.com/saudi-ar/search?q=iphone+15" target="_blank">شراء من نون</a>
            </div>
            <div class="footer">
                <p><b>BESTDEAL</b> - أفضل صفقة | قارن قبل ما تشتري</p>
                <p>جاري تطوير نظام الأفلييت والسحب التلقائي...</p>
            </div>
        </div>
    </body>
    </html>
    """
