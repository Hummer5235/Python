import asyncio
import async_google_trans_new


async def coro():
    g = async_google_trans_new.AsyncTranslator()
    print(await g.translate("こんにちは、世界！","en"))

# async def main():
#     # task1 = asyncio.create_task(coro())
#     # await task1




if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(coro())



