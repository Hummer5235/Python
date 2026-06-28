from requests import get


def get_fact(month,day):
    answer = get(f'http://numbersapi.com/{month}/{day}').text
    return answer