#Проверка на Админа
import aiogram.filters
from aiogram import Bot, Dispatcher
from aiogram.filters import ChatMemberUpdatedFilter, KICKED
from aiogram.types import ChatMemberUpdated
from environs import Env

env = Env() # Создаем экземпляр класса Env
env.read_env() # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
BOT_TOKEN = env('BOT_TOKEN') # Получаем и сохраняем значение переменной окружения в переменную BOT_TOKEN


# Создаем объекты бота и диспетчера
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

#Id админа
admin_ids: list[int] = [852757379]



@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def process_user_blocked_bot(event:ChatMemberUpdated):
    print(f'Пользователь {event.from_user.id} заблокировал бота')
    await bot.send_message(admin_ids[0],f'Пользователь {event.from_user.id} заблокировал бота')

@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=aiogram.filters.MEMBER))
async def process_user_blocked_bot(event:ChatMemberUpdated):
    print(f'Пользователь {event.from_user.id} разблокировал бота')
    await bot.send_message(admin_ids[0],f'Пользователь {event.from_user.id} разблокировал бота')

dp.run_polling(bot)