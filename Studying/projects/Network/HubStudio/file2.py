import requests
from apikey import APITOKEN

params = {'q':'Москва','appid':APITOKEN,'units':'metric','lang':'ru'}


# params2 = {'lat':'57.767919','lon': '40.926894','appid':APITOKEN}
# responce2 = requests.get('https://api.openweathermap.org/data/2.5/weather',params=params2)

def get_weather(city='Москва'):
    params['q']= city
    try:
        responce = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
        j = responce.json()
        print(j)
        str_weather = f"На улице сейчас: {j['weather'][0]['description'].capitalize()}"
        str_temp = f"Текущая температура {round(j['main']['temp'], 1)} C°"
        return str_weather, str_temp
    except KeyError:
        return 'Введите правильное название \nнаселенного пункта'



if __name__ == '__main__':
    print(get_weather())

