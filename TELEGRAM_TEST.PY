import requests

TOKEN = "7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ"
CHAT_ID = "-1002586854094"
TEXT = "تست ارسال پیام از بات MasoudGOLDXBot"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {
    "chat_id": CHAT_ID,
    "text": TEXT
}

response = requests.post(url, data=data)

print("Status Code:", response.status_code)
print("Response:", response.text)
