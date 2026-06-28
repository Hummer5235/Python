import asyncio
import time

#async функция()- корутина, сопрограмма, то , что возвращает функция после вызова
#asyncio.sleep - неблокирующий sleep
#Перед вызовом асинхронных функций появился префикс await.
#Приостанавливает выполнение текущей подпрограммы (coroutine) и вызывает указанное ожидание awaitable.

#Корутина — это то, что возвращает функция с await
async def fun1(x):
    print(x**2)
    await asyncio.sleep(3)
    print('fun1 завершена')


async def fun2(x):
    print(x**0.5)
    await asyncio.sleep(3)
    print('fun2 завершена')


async def main():
    #Задача — это частный случай футуры, предназначенный для оборачивания корутины.
    task1 = asyncio.create_task(fun1(4)) #Корутину асинхронной функции fun1 обернули задачей task1
    task2 = asyncio.create_task(fun2(4)) #Корутину асинхронной функции fun2 обернули задачей task2

    print(type(task1)) # <class '_asyncio.Task'>
    print(task1.__class__.__bases__) # (<class '_asyncio.Future'>,)


    await task1
    await task2


asyncio.run(main()) #Точка входа в приложение

print(type(fun1)) #Класс функция

print(type(fun1(4))) #Класс корутина. Разновидность генератора
#Корутина дает интерпретатору возможность возобновить базовую функцию,
#которая была приостановлена в месте размещения ключевого слова await.
#Задача — это частный случай футуры, предназначенный для оборачивания корутины.