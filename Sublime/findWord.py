#Записываем элементы списка в словарь и считаем количество
list_of_words=["hello","hello","hi"]
words={}

for word in list_of_words:
	words[word]=words.get(word,0)+1

print(words)