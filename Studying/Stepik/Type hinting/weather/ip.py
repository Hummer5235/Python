import requests

def get_ip(url : str) -> str:
    response = requests.get(url)
    ip = response.text
    return ip


