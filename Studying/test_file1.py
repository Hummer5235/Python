
try:
    file = open("out.txt","r",encoding="utf-8")
    file2 = open("new.txt","w+",encoding="utf-8")
    try:

        # r = file.read()
        # for i in range(0,200):
        #     if i%2==0:
        #         file2.write(r[i])

        r = file.read(200)  # Изначально нужно прочитать файл
        for i in range(0,len(r),2):
            file2.write(r[i])
        file2.seek(0)
        print(file2.read())



    finally:
        file.close()
        file2.close()
except FileNotFoundError:
    print("Файл не найден")
    print("Проверьте название файла или указанный путь")



