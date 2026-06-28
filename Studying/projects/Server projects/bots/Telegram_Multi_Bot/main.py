
import asyncio
import logging
import pathlib

from aiogram import Bot, Dispatcher
from environs import Env

from Project.handlers import start_handlers,payments_handlers,current_date_handlers,game_handlers,others_handlers,day_event_mailing_handlers, admin_handlers
from Project.event_day_checker.event_day import mailing_events_loop

main_path = pathlib.Path(__file__)
data_path = main_path.parent/'Project/data'




# Функция конфигурирования и запуска бота
async def main():
    try:
        env = Env()  # Создаем экземпляр класса Env
        env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
        BOT_TOKEN = env('BOT_TOKEN')  # Получаем и сохраняем значение переменной окружения в переменную BOT_TOKEN
        # BOT_TOKEN= "6488447802:AAHsemIpNuz2FAL8O7Im6Lgy6suwg0Wm7ac"
        # Загружаем конфиг в переменную config
        # config: Config = load_config()


        # Инициализируем бот и диспетчер
        bot = Bot(token=BOT_TOKEN)
        dp = Dispatcher()

        #Регистрируем роутеры в диспетчере
        dp.include_router(start_handlers.router)
        dp.include_router(admin_handlers.router)
        dp.include_router(day_event_mailing_handlers.router)
        dp.include_router(payments_handlers.router)
        dp.include_router(current_date_handlers.router)
        dp.include_router(game_handlers.router)
        dp.include_router(others_handlers.router)

        # Запускаем код рассылки
        asyncio.create_task(mailing_events_loop(bot))

        # Пропускаем накопившиеся апдейты и запускаем polling
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)

    except:
        logging.warning('Ошибка работы программы')
        print('Error')


asyncio.run(main())