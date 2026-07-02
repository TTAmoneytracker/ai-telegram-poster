import os
import random
import requests
from datetime import datetime

BOT_TOKEN = os.environ["TG_BOT_TOKEN"]
CHAT_ID = os.environ["TG_CHAT_ID"]

posts = [
    "💰 ငွေကြေးစီမံခန့်ခွဲမှုမှာ အရေးကြီးဆုံးက ဝင်ငွေထက် နည်းအောင်သုံးနိုင်ဖို့ပါ။\n\n#Finance #MoneyTips",
    "📈 ရင်းနှီးမြှုပ်နှံမှုမလုပ်ခင် Risk ကိုအရင်နားလည်ပါ။ အမြတ်ကြီးလေလေ Risk ကြီးလေဖြစ်တတ်ပါတယ်။\n\n#Investment #Risk",
    "💵 Emergency Fund ကို အနည်းဆုံး ၃ လစာ အသုံးစရိတ်လောက် စုထားသင့်ပါတယ်။\n\n#Saving #FinancialFreedom",
    "📊 Trading မှာ Plan မရှိဘဲ ဝင်တာက အန္တရာယ်များပါတယ်။ Stop Loss ကိုလည်း မမေ့ပါနဲ့။\n\n#Trading #Crypto",
]

message = random.choice(posts)
message += f"\n\n🕒 {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})

print(response.status_code)
print(response.text)
response.raise_for_status()
