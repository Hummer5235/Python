import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.704 Yowser/2.5 Safari/537.36",
}

data = {
'authenticity_token': '',
'login': 'Hummer5235',
'password': 'GitTop15'
}

ses = requests.Session()

response = ses.get('https://github.com/session')
print(response.status_code)
text = response.text
text = text.split('\n')
for line in text:
    if 'token' in line and 'value' in line:
        # print(line)
        # print(line.index('value='))
        token = line[line.index('value=')+7:line.index('==')+2]
        data['authenticity_token'] = token
print(data)

response = ses.post('https://github.com/session',data=data,headers=headers)
print(response.status_code)
text  = response.text
with open('git_page.html','w',encoding='utf-8') as out:
    for line in text:
        out.write(line)