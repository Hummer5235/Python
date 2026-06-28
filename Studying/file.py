try:
    file = open("myfile.txt",encoding='utf-8')
    print(file.read(2))
    file.seek(0) # Сместить позицию файла на 0
    print(file.read(2))
    pos = file.tell() # Получить позицию ( 1 символ = 2 байта в кодировке utf-8)
    print(pos)

except FileNotFoundError:
    print("Файл не найден")
    print("Проверьте название файла или указанный путь")