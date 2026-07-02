import os
import random
import requests
from datetime import datetime

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
BOT_TOKEN = os.environ["TG_BOT_TOKEN"]
CHAT_ID = os.environ["TG_CHAT_ID"]

topics = [
    "personal finance",
    "crypto education",
    "gold investment",
    "stock market basics",
    "saving money",
    "risk management",
]

topic = random.choice(topics)

prompt = f"""
Write one short Burmese Telegram channel post about {topic}.

Rules:
- Burmese language only
- 80 to 130 words
- Beginner friendly
- Educational, not financial advice
- Use emoji
- Add 3 relevant hashtags
- Do not promise profit
- Do not tell people to buy or sell
"""

response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    },
    json={
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a careful financial education content writer."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.9,
        "max_tokens": 400,
    },
)

print(response.status_code)
print(response.text)
response.raise_for_status()

ai_text = response.json()["choices"][0]["message"]["content"]

message = ai_text + f"\n\n🕒 {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}"

tg_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

tg_response = requests.post(tg_url, data={
    "chat_id": CHAT_ID,
    "text": message,
})

print(tg_response.status_code)
print(tg_response.text)
tg_response.raise_for_status()
