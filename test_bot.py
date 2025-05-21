import requests

url = "https://api.telegram.org/bot7352244492:AAGOrkQXT88z1OH975q09jWkBcoI3G3ifEQ/sendMessage"
payload = {
    "chat_id": "-1002586854094",
    "text": "فقط تست خام MasoudGOLDXBot"
}
r = requests.post(url, data=payload)
print(r.status_code)
print(r.text)
