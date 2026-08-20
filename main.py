from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

HTML_PAGE = """
<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>بوت نواف الذكي</title>
<style>
body{font-family:system-ui;background:#0f0f0f;color:#fff;padding:20px;text-align:center}
.box{max-width:500px;margin:auto;background:#1a1a1a;padding:25px;border-radius:20px;border:1px solid #333}
input,textarea,button{width:100%;padding:15px;margin:10px 0;border-radius:12px;border:none;font-size:16px;box-sizing:border-box}
button{background:#a855f7;color:white;font-weight:bold;cursor:pointer}
.result{background:#222;padding:15px;border-radius:12px;margin-top:15px;text-align:right;white-space:pre-line;border:1px solid #333}
</style>
</head>
<body>
<div class="box">
<h2>🤖 بوت نواف - وصف منتجات</h2>
<form id="f">
<input type="text" id="name" placeholder="اسم المنتج مثلا: ساعة ذكية" required>
<input type="text" id="price" placeholder="السعر مثلا: 199 ريال">
<textarea id="desc" placeholder="وصف بسيط للمنتج (اختياري)"></textarea>
<button type="submit">✨ ولّد الوصف بالذكاء الاصطناعي</button>
</form>
<div id="res" class="result" style="display:none"></div>
</div>
<script>
document.getElementById('f').onsubmit=async(e)=>{
e.preventDefault();
let r=document.getElementById('res');
r.style.display='block';
r.innerText='⏳ جاري التوليد...';
let name=document.getElementById('name').value;
let price=document.getElementById('price').value;
let desc=document.getElementById('desc').value;
let form=new FormData();
form.append('name',name);
form.append('price',price);
form.append('desc',desc);
let res=await fetch('/generate',{method:'POST',body:form});
let data=await res.json();
r.innerText=data.text;
}
</script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return HTML_PAGE

@app.post("/generate")
async def generate(name: str = Form(...), price: str = Form(""), desc: str = Form("")):
    # وصف احترافي جاهز بدون ما نحتاج مفتاح OpenAI في البداية
    text = f"""🔥 {name} - الفخامة اللي تستاهلها!

✨ {desc if desc else f'{name} بجودة عالية وتصميم عصري يلفت الأنظار'}

💎 المميزات:
• جودة ممتازة ومضمونة
• تصميم أنيق وعصري
• عملي وينفع للاستخدام اليومي
• هدية مثالية لنفسك أو لمن تحب

💰 السعر: {price if price else 'سعر خاص'}

🚀 اطلبه الحين قبل نفاد الكمية! الدفع عند الاستلام وشحن سريع لكل السعودية!

#متجر_نواف # {name.replace(' ', '_')}
"""
    return {"text": text}
  -+
