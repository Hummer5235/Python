import zipfile
my_zip = zipfile.ZipFile('files.zip','w')
my_zip.write("nes.txt")
my_zip.write("О задачах.docx")

my_zip.close()

print("Ok")

# Чтение zip файла
getZip = zipfile.ZipFile("files.zip")
print(getZip.namelist())   #namelist() - возвращает список
# содержимого zip архива
getZip.close()

# Извлечение файлов , метод extract()
a = input("Извлечь файлы?(Y/N): ")
if a == "Y":
	getZip = zipfile.ZipFile('files.zip')
	getZip.extract("О задачах.docx")
	getZip.close()

# Извлечение всего содержимого zip архива
getZip=zipfile.ZipFile("files.zip")
getZip.extractall()
getZip.close()