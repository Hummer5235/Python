import webbrowser

import requests

params = {'q':'funny cats'} #Параметры для поиска

# response = requests.get('https://google.com')
response = requests.get('https://google.com/search',params=params)

# print(response.status_code)
# print(response.content)
# print(response.text)
# print(response.headers)


headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru,en;q=0.9",
    "Host": "httpbin.org",
    "Referer": "https://httpbin.org/",
    "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"YaBrowser\";v=\"23\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2526 Yowser/2.5 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-64b95e3e-4a3ad40c260203d962f2ea20"
  }

# response = requests.get('https://httpbin.org/headers',headers=headers)
# print(response.text)


data = {'custname':'Log',
        'custtel':'89',
        'custeemail':'',
        'delivery':'',
        'comments':''
        }

# response = requests.post('https://httpbin.org/post',data=data)
# print(response.text)
# print(response.status_code)


data = {
    'st.redirect': '',
    'st.asr': '',
    'st.posted': 'set',
    'st.fJS': 'on',
    'st.st.screenSize': '1289 x 725',
    'st.st.browserSize': '776',
    'st.st.flashVer': '0.0.0',
    'st.email': '',
    'st.password':'',
    'st.iscode': 'false',
    'st.email': '+79220748359',
    'st.password': 'OkTop151'
}
# response2 = requests.get('https://ok.ru/')

session_var = requests.Session() # Создание сессии для хранения файлов Cookies
response3 = session_var.post('https://ok.ru/dk?cmd=AnonymLogin&st.cmd=anonymMain',data=data,allow_redirects = True)
# print(response3.status_code)
# print(response3.text)

