import os
import random
import requests
from datetime import datetime

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
BOT_TOKEN = os.environ["TG_BOT_TOKEN"]
CHAT_ID = os.environ["TG_CHAT_ID"]

topics = [
    "Bitcoin",
    "Ethereum",
    "Saving Money",
    "Stock Market",
    "Gold Investment",
    "Personal Finance",
    "Risk Management"
]

topic = random.choice(topics)

prompt = f"""
Write ONE educational Telegram post in Burmese.

Topic: {topic}

Rules:
- Burmese language
- 100-150 words
- Friendly style
- Add emojis
- Add 3 hashtags
- Do NOT give financial advice
- Do NOT promise profit
"""

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

body = {
    "contents": [
        {
            "parts": [
                {
                    "text": prompt
                }
            ]
        }
    ]
}

response = requests.post(url, json=body)
print(response.status_code)
print(response.text)

response.raise_for_status()

data = response.json()

text = data["candidates"][0]["content"]["parts"][0]["text"]

message = text + "\n\n🕒 " + datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    telegram_url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
