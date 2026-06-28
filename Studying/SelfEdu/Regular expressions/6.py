import re 
text = '+7(123)456-53-52'


#Метод match который определяет совпадение шаблона pattern в НАЧАЛЕ строки string 
print('\nВыполнение метода match:')

m = re.match(r'\+7\(\d{3}\)\d{3}-\d{2}-\d{2}',text)
print(m)


#re.split(pattern, string, flags)
#выполняет разбивку строки string по заданному шаблону pattern. 

text = """<point lon="40.8482" lat="52.6274" />
<point lon="40.8559" lat="52.6361" />; <point lon="40.8614" lat="52.651" />
<point lon="40.8676" lat="52.6585" />, <point lon="40.8672" lat="52.6626" />
"""
print('\nВыполнение метода split:')
m = re.split(r'[\n;,]+',text)
print(m)


# Метод sub выполняет замену в строке найденных совпадений строкой или результатом работы функции repl и возвращает преобразованную строку. Также используем ссылки на сохр группы
text= 'Agent Alice with Agent Bob told Agent Carol that Agent Eve knew Agent Bob was a double agent.'
agNameRegex = re.sub(r'Agent (\w)\w*',r'\1****',text)
print(agNameRegex)




text = """Москва
Казань
Тверь
Самара
Уфа"""


list = re.sub(r'\s*(\w+)\s*',r'<option>\1</option>\n',text)

print('\nВыполнение метода sub:')
print(list)


# Также в метод можно передавать ссылку на функцию
#В качестве параметра она принимает ссылку на объект re.Match, в котором хранится информация о найденном совпадении. И далее формируется строка с атрибутом value, причем, значение этого атрибута каждый раз увеличивается на 1.




count = 0
def replFind(m):
	global count
	count += 1
	return f'<option value = "{count}">{m.group(1)}</option>\n'

print('\nВыполнение метода sub с доп функцией:')

list2 = re.sub(r'\s*(\w+)\s*',replFind, text)
print(list2)





#Аналогично работает метод subn , только он еще возвращает число замен
list, total = re.subn(r"\s*(\w+)\s*", r"<option>\1</option>\n", text)
print(list, total)	



#Метод re.compile - выполняет компиляцию регулярного выражения и возвращает его в виде экз класса Pattern
text = '+7(123)456-53-52'

rx = re.compile(r'\+7\(\d{3}\)\d{3}-\d{2}-\d{2}')