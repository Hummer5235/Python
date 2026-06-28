#29. Обработка исключений. Блоки finally и else

f = None

try:
    f = open('myfile.txt')
    f.write('Hello')
    print(f)
except FileNotFoundError as z:
    print(z)
except:
    print('Ошибка')
else:
    print('Исключений не произошло')

finally: # finally можно использовать для обязательного закрытия файла, несмотря на ошибку
    if f :
        f.close()
        print('Работа программы завершена. Блок finally выполняется всегда')