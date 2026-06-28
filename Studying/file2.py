#
# try:
#     file = open("myfile.txt",encoding='utf-8')
#     try:
#         print(file.read())
#     finally:
#         file.close() # Обязательно закрываем файл по окончанию работы с ним
#         print(file.closed)
# except FileNotFoundError:
#     print("Файл не найден")
#     print("Проверьте название файла или указанный путь")


try:
    #file = open("myfile.txt",encoding='utf-8')

#Используем менеджер контекста для автоматического закрытия файла
    with open("myfile.txt",encoding = "utf-8") as file:
        s = file.read()
        print(s)

except FileNotFoundError:
    print("Файл не найден")
    print("Проверьте название файла или указанный путь")

