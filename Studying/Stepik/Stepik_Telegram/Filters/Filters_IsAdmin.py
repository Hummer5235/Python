#Проверка на Админа
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, BaseFilter
from aiogram.types import Message
from environs import Env

env = Env() # Создаем экземпляр класса Env
env.read_env() # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
BOT_TOKEN = env('BOT_TOKEN') # Получаем и сохраняем значение переменной окружения в переменную BOT_TOKEN


# Создаем объекты бота и диспетчера
bot = Bot(BOT_TOKEN)
dp = Dispatcher()



#Id админа
admin_ids: list[int] = [852757379]

class IsAdmin(BaseFilter):
    def __init__(self,admin_ids:list[int]) ->None:
        self.admin_ids = admin_ids

    async def __call__(self, message:Message)->bool:
        return message.from_user.id in self.admin_ids


@dp.message(IsAdmin(admin_ids))
async def answer_if_admins_update(message:Message):
    await message.answer('Вы админ')

@dp.message()
async def answer_if_not_admins_update(message:Message):
    await message.answer('Вы не админ')


dp.run_polling(bot)