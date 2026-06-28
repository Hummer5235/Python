
b = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л',
 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 
 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

word = input() + " запретил букву"
for i in b:
	if i in word:
		
		print(word,i)
		word = word.replace(i,"")
		if len(word) > 0:
			if word[0] == " ":
				word = word[1:]
			word = word.replace("  "," ")
			word = word.strip()
		
		


			








# lst.sort()
# space_counter = lst.count(' ')
# if space_counter > 0:
# 	for i in range(space_counter):
# 		lst.remove(" ")

# letters_counter = 0
# for i in lst:
# 	letters_counter = lst.count(i)
# 	if letters_counter > 1:
# 		lst.remove(i)



