import requests

url = "https://holidays.abstractapi.com/v1/?api_key=3c5b06c53922427ebb9fca73458d915d&country=RU&year=2026&month=1&day=6&language=RE"

response = requests.get(url)

print(response.text)