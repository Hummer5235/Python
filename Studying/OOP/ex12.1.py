#Пример использования функции __call__ вместо замыкания функции

class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        print('вызов метода __call__')
        if not isinstance(args[0], str):
            raise TypeError ("Аргумент должен быть строкой")
        
        return args[0].strip(self.__chars) # Возвращает измененную строку без лишних знаков
    
s1 = StripChars('!?:.;')
s2 = StripChars(' ')
res = s1("!Hello World!")
res2 = s2("!Hello World!")
print(res, res2 , sep='\n')