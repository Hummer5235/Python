import asyncio
import time

lst = []

def timeit(func):
    async def wrapper():
        i = 0
        while True:
            await asyncio.sleep(1)
            i+=1
            print(i)
            result = await func()
        return result
    return wrapper

@timeit
async def loop_while():
    print('Ок')

@timeit
async def loop_while_two():
        print('Новая строка - новое действие')

#
# loop_while_two()
# loop_while()



async def main():
    task1 = asyncio.create_task(loop_while())
    task2 = asyncio.create_task(loop_while_two())
    await task1
    await task2



asyncio.run(main())