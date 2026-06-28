import re
#Флаг re.VERBOSE позволяет расписывать шаблон в развернутом виде


phoneNumbers ='495-242-1429'

phoneRegex = re.compile(r'''
	(\d{3}|\(\d{3}\)) 		#территориальный код
	(\s|-|\.)?				#разделитель
	\d{3}					#первые 3 цифры
	(\s|-|\.)?				#разделитель
	\d{4}
	''',re.VERBOSE)

match = phoneRegex.search(phoneNumbers)
print(match)

text = 'pet carPeT SunPetrol'
match = re.findall('pet',text,re.I|re.DOTALL)
print(match)