from time import time
import asyncio


start = time()

async def spider(site_name):
    for page in range(1,4):
        await asyncio.sleep(1)
        print(site_name,page)



async def main():
    spiders = [
        asyncio.create_task(spider('Blog')),
        asyncio.create_task(spider('News')),
        asyncio.create_task(spider('Forum'))
    ]
    await asyncio.gather(*spiders)

asyncio.run(main())
print(time()-start)