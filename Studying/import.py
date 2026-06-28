import mymath,mymath_test,dictionary

print(mymath.PI)
mymath.PI = 3
print(mymath.PI)

#Перезагружаем модуль mymath
from importlib import reload
reload(mymath)

print(mymath.PI)
print(dir(mymath))

#Задача 1
print(mymath_test.P(2,5))
print(mymath_test.S(2,5))

#Задача 2
dictionary.show()
dictionary.add("Way","Путь")
dictionary.show()
dictionary.delete("Goodbye")
dictionary.show()