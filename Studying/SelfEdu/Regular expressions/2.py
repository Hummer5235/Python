#Квантификаторы регулярных выражений
import re
 
text = "Google, Gooogle, Goooooogle"
match = re.findall(r"o{2,5}", text) # Мажорный или жадный , ищет большее число совпадений
match2 = re.findall(r"o{2,5}?",text)
print('1.',match)
print('2.',match2)

'''
{m} – повторение выражения ровно m раз (эквивалент {m,m});
{m,} – повторения от m и более раз;
{, n} – повторения не более n раз.


? – от нуля до одного (аналог {0,1});
* – от нуля и до «бесконечности» (в действительности, большого числа – от 32767), соответствует квантификатору {0,};
+ – от единицы и до «бесконечности» (также большого числа – от 32767), соответствует квантификатору {1,}.
'''

text = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001"
match = re.findall(r'\w+\s*=\s*[^;]+',text)
match2 = re.findall(r'(\w+)\s*=\s*([^;]+)',text)
print('1.',match)
print('2.',match2)


text = "Картинка <img src='bg.jpg'> в тексте</p>"
match = re.findall(r'<img.*?>',text)

text2 = "<p>Картинка <img alt='картинка' src='bg.jpg'> в тексте</p>"
text3 = "<img>"
text4 = "<p>Картинка <img src='bg.jpg' title='картинка'> в тексте</p>"
text5 =	"<p>Картинка <img src2='bg.jpg'> в тексте</p>"
text6 = "<p>Картинка <img src='bg.jpg'> в тексте</p>"
text7 = "<p>Картинка <img alt='картинка'> в тексте</p>"
match2 = re.findall(r'<img\s+[^>]*?src\s*=\s*[^>]*>',text2)
match3 = re.findall(r'<img\s+[^>]*?src\s*=\s*[^>]*>',text3)
match4 = re.findall(r'<img\s+[^>]*?src\s*=\s*[^>]*>',text4)
match5 = re.findall(r'<img\s+[^>]*?src\s*=\s*[^>]*>',text5)
match6 = re.findall(r'<img\s+[^>]*?src\s*=\s*[^>]*>',text6)
match7 = re.findall(r'<img\s+[^>]*?src\s*=\s*[^>]*>',text7)
print('1.', match)
print('2.', match2)
print('3.', match3)
print('4.', match4)
print('5.', match5)
print('6.', match6)
print('7.', match7)
