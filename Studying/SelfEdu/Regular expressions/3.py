#Сохраняюзие скобки и группировка
import re

text = 'lat = 5, lon = 7, a = 5'
# text = 'pi = 12, kon = 34'
#?: несохраняющая группировка 2х литералов
match = re.findall(r'(?:lat|lon)\s*=\s*\d+',text)
match2 = re.findall(r'(lat|lon)\s*=\s*(\d)+',text)
print('1.',match)
print('2.',match2)


text = "<p>Картинка <img src='bg.img'> в тексте </p>"
match = re.findall(r'<img\s[^>]*src\s*=\s*([\'"])(.+?)\1',text)
print(match)
#Используем имя для сохраненного блока вместо цифры
match2 = re.findall(r'<img\s[^>]*src\s*=\s*(?P<q>[\'"])(.+?)(?P=q)',text) 
print(match2)


