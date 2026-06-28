#Реализация декотраторов с помощью класса
import math

#Класс - декоратор
class Derivate:
    def __init__(self, func):
        self.__fn = func
    
    def __call__(self, x, dx = 0.0001, *args, **kwargs):
        return (self.__fn(x+dx) - self.__fn(x)) / dx


#Функция к которой применяется декоратор
@Derivate
def df_sin(x):
    return math.sin(x)



#Вместо прямого использования мы добавили декоратор
# df_sin = Derivate(df_sin)
print(df_sin(math.pi/3))