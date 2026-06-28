import requests



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.704 Yowser/2.5 Safari/537.36",
}

data = {
'fr.login': '+79220748359',
'fr.password': 'VkTop151'
}


response = requests.get('https://m.ok.ru/dk?bk=GuestMain&st.cmd=main&st.lgi=WeMuf4HPxb3i&_prevCmd=main&tkn=9455&_cl'
                        '.id=1695022798179&_clickLog=%5B%7B%22target%22%3A%22sign_in%22%7D%2C%7B%22stateParams%22%3A'
                        '%22%7B%5C%22stateId%5C%22%3A%5C%22main%5C%22%2C%5C%22st-prm_lgi%5C%22%3A%5C%22WeMuf4HPxb3i'
                        '%5C%22%7D%22%2C%22registrationContainer%22%3A%22home.login_form%22%7D%5D&_cl.sID=main',
                        headers= headers,data=data)
# print(response.headers['Content-type'])
print(response.text)
