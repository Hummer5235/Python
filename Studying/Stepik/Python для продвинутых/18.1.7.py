import string
eng_lang = "a b v g d e jo zh z i j k l m n o p r s t u f h c ch sh shh * y ' je ju ya".split() 
rus_lang = 'а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split()
dictionary = dict(zip(rus_lang,eng_lang))

with open('cyrillic.txt',encoding='utf-8') as file, open('transliteration.txt','w') as out:
	for simb in file.read():
		if simb.isupper():
			if simb.lower() in dictionary:
				simb = dictionary[simb.lower()]
				if len(simb) == 1:
					simb = simb.upper()
				else:
					simb = simb[0].upper()+simb[1:]
					
		elif simb.islower():
			if simb.lower() in dictionary:
				simb = dictionary[simb.lower()]

		out.write(simb)