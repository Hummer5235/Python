import time
import asyncio

#async функция()- корутина, сопрограмма, то , что возвращает функция после вызова
#asyncio.sleep - неблокирующий sleep
#Перед вызовом асинхронных функций появился префикс await.
# Приостанавливает выполнение текущей подпрограммы (coroutine) и вызывает указанное ожидание awaitable.

#Результат вызова async функции - coroutine(корутина)

async def print1():
    print(1)

async def print2():
    await  asyncio.sleep(5) # Специальная функция в модуле (ожидание)
    print(2)

async def print3():
    print(3)


async def main():
    #Преподготовка программ
    task1 = asyncio.create_task(print1())
    task2 = asyncio.create_task(print2())
    task3 = asyncio.create_task(print3())

    await task1
    await task2
    await task3


async def main2():
    # Преподготовка программ

    task1 = asyncio.create_task(print1())
    task2 = asyncio.create_task(print2())
    task3 = asyncio.create_task(print3())
    tasks = [task1,task2,task3]
    print(type(task1))
    print(task1.__class__.__bases__)

    await asyncio.gather(*tasks)

    #Функция gather() модуля asyncio одновременно запускает объекты awaitable,
    # переданные в функцию как последовательность


asyncio.run(main2()) #Событийный цикл. Необходима точка входа


