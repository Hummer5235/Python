import asyncio
import logging

from aiogram import Bot, Dispatcher
from environs import Env
from Project.handlers import start_handlers,payments_handlers,current_date_handlers,game_handlers,others_handlers


# Функция конфигурирования и запуска бота
async def main():
    try:
        env = Env()  # Создаем экземпляр класса Env
        env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
        BOT_TOKEN = env('BOT_TOKEN')  # Получаем и сохраняем значение переменной окружения в переменную BOT_TOKEN

        # Загружаем конфиг в переменную config
        # config: Config = load_config()

        # Инициализируем бот и диспетчер
        bot = Bot(token=BOT_TOKEN)
        dp = Dispatcher()

        #Регистрируем роутеры в диспетчере
        dp.include_router(start_handlers.router)
        dp.include_router(payments_handlers.router)
        dp.include_router(current_date_handlers.router)
        dp.include_router(game_handlers.router)
        dp.include_router(others_handlers.router)


        # Пропускаем накопившиеся апдейты и запускаем polling
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except:
        logging.WARN('Ошибка работы программы')


asyncio.run(main())


