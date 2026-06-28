import asyncio, time



async def prints(sec):
    await asyncio.sleep(sec)
    print(sec)

async def main():
    tasks = []
    for i in range(1,16):
        tasks.append(asyncio.create_task(prints(i)))

    await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())

print(f'Время на работу программы: {time.time()-start}')