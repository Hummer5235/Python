
try:
    file = open("out.txt","w")
    try:

        file.write("Hello World!\n")
        file.write("Hello!\n")
        file.write("Hello!\n")
        # file.seek(0)
        # print(file.read())
    finally:
        file.close() # Обязательно закрываем файл по окончанию работы с ним
except FileNotFoundError:
    print("Файл не найден")
    print("Проверьте название файла или указанный путь")

