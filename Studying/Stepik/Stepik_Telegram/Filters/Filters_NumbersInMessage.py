#Проверка на доп параметры
from __future__ import annotations

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, BaseFilter
from aiogram.types import Message
from aiogram import F
from environs import Env

env = Env() # Создаем экземпляр класса Env
env.read_env() # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
BOT_TOKEN = env('BOT_TOKEN') # Получаем и сохраняем значение переменной окружения в переменную BOT_TOKEN


# Создаем объекты бота и диспетчера
bot = Bot(BOT_TOKEN)
dp = Dispatcher()



# Этот фильтр будет проверять наличие неотрицательных чисел
# в сообщении от пользователя, и передавать в хэндлер их список
class NumbersInMessage(BaseFilter):
    async def __call__(self, message:Message)-> bool|dict[str,list[int]] :
        numbers = []
        # Разрезаем сообщение по пробелам, нормализуем каждую часть, удаляя
        # лишние знаки препинания и невидимые символы, проверяем на то, что
        # в таких словах только цифры, приводим к целым числам
        # и добавляем их в список
        for word in message.text.split():
            normalized_word = word.replace(',','').replace('.','').strip()
            if normalized_word.isdigit():
                numbers.append(int(normalized_word))
        # Если в списке есть числа - возвращаем словарь со списком чисел по ключу 'numbers'
        if numbers:
            return {'numbers':numbers}
        else:
            return False



# Этот хэндлер будет срабатывать, если сообщение пользователя
# начинается с фразы "найди числа" и в нем есть числа
@dp.message(F.text.lower().startswith('найди числа'),NumbersInMessage())
# Помимо объекта типа Message, принимаем в хэндлер список чисел из фильтра
# по соответствующему ключу `numbers`
async def process_if_numbers(message:Message,numbers:list[int]):
    await message.answer(
        text=f'Нашел: {", ".join(str(num) for num in numbers)}')


# Этот хэндлер будет срабатывать, если сообщение пользователя
# начинается с фразы "найди числа", но в нем нет чисел
@dp.message(F.text.loswer().startswith('найди числа'))
async def process_if_not_numbers(message:Message):
    await message.answer(
        text='Не нашел что-то :(')


#Функция для проверки
# def my_start_filter(message:Message):
#     return message.text.lower().startswith('найди числа')
#
#
#
# @dp.message(my_start_filter)
# async def check_message(message:Message):
#     numbers = []
#     await message.answer('Сейчас найду!')
#     for word in message.text.split():
#         normalized_word = word.replace('.', '').replace(',', '').strip()
#         if normalized_word.isdigit():
#             numbers.append(int(normalized_word))
#     if len(numbers)>0:
#         await message.answer(f'Вот они: {",".join(str(num) for num in numbers)}')
#     else:
#         await message.answer('Не нашел что то :(')




dp.run_polling(bot)








