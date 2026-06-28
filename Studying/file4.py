import pickle

book1=["Евгений Онегин","Пушкин А.С.",200]
book2=["Муму","Тургенев И.С.",250]
book3=["Мастер и Маргарита","Булгаков М.А.",500]
book4=["Мертвые души","Гоголь Н.В.",190]

try:
    file = open("out.bin","wb+")
    try:
        pickle.dump(book1,file)
        pickle.dump(book2,file)
        pickle.dump(book3,file)
        pickle.dump(book4,file)
        file.seek(0)
        print(pickle.load(file))
        print(pickle.load(file))
        print(pickle.load(file))
        print(pickle.load(file))

    finally:
        file.close() # Обязательно закрываем файл по окончанию работы с ним
except FileNotFoundError:
    print("Файл не найден")
    print("Проверьте название файла или указанный путь")

