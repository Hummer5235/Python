from requests import get
from Location import location

params = {"ll": f"{location.longitude},{location.latitude}",
          "spn": "0.5,0.5",
          "l": "map"}
response = get("https://static-maps.yandex.ru/1.x/?",params=params)
print(response)

# webbrowser.open("https://static-maps.yandex.ru/1.x/?")
with open('map.png','wb') as file:
    file.write(response.content)

