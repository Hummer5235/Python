import time

import requests, json , enum
from datetime import datetime

class Place_Type:
    upper = 'верх'
    lower = 'низ'
    upper_side = 'верх.бок'
    lower_side = 'ниж.бок'
class Carriage:
    first_class = 'К'
    second_class = 'Э'


DICTIONARY = None
START_TIME = datetime.now()
def get_html_page(url):
    try:
        response = requests.get(url)
        return response.text
    except:
        print('Ошибка запроса')

def check_time():
    global START_TIME
    time_length = str(datetime.now() - START_TIME).split('.')[0]
    START_TIME = datetime.now()
    return time_length
def check_result(dictionary):
    global DICTIONARY
    if DICTIONARY != dictionary:
        DICTIONARY = dictionary
        return DICTIONARY
    else:
        return {}


# check_time({})
# time.sleep(1)
# check_time({})
# time.sleep(5)
# check_time({1:2})
# time.sleep(3)
# check_time({2:3})

def parse_html(text:str):
    try:
        text = text[text.index("'CarsFormat':{")+13:text.index('Reserved')-2]
        text = text.replace("'", '"')
        json_file = json.loads(text)
        return json_file

    except:
        print('Ошибка введенных данных')



def parse_json(json_file:json, place_type:Place_Type):
    dictionary = {}
    try:
        for carriage_number in json_file:
            if Carriage.second_class in carriage_number:
                for place_category in range(len(json_file[carriage_number])):
                    # print(carriage_number,json_file[carriage_number][place_category])
                    values = json_file[carriage_number][place_category]['PlaceTypes'].values()
                    if place_type in values :
                        carriage_number_redact = carriage_number[carriage_number.index('_') + 1:carriage_number.index('_') + 3]
                        # print(carriage_number)
                        dictionary[carriage_number_redact] = json_file[carriage_number][place_category]['PlaceTypes']
    except:
        print('Ошибка создания словаря')
    # print(dictionary)
    dictionary = check_result(dictionary)
    if dictionary:
        time_length = check_time()
        return dictionary,time_length
    return dictionary, 0



