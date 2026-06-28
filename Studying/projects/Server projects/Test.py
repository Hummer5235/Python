import requests
from datetime import datetime

# Получаем текущие дату и время
now = datetime.now()

for j in range(1,12):
    for i in range(1,28):
        # Формируем URL с текущими значениями года, месяца и дня
        url = f"https://calendar.kuzyak.in/api/calendar/{now.year}/{j}/{i}"

        # Отправляем GET-запрос
        response = requests.get(url)

        # Проверяем статус ответа
        if response.status_code == 200:
            # Выводим данные в формате JSON
            print(response.json())
        else:
            # Выводим ошибку
            print(f"Ошибка: {response.json()}")