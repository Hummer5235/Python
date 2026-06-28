from requests import get



response = get('https://ticket.rzd.ru/booking/rail/110*С/seats')
print(response.status_code)
if response.status_code == 200:
    print(response.text)
    print(response.content)