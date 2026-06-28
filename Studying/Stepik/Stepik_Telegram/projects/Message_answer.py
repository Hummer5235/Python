from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F
from environs import Env

env = Env() # Создаем экземпляр класса Env
env.read_env() # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
BOT_TOKEN = env('BOT_TOKEN') # Получаем и сохраняем значение переменной окружения в переменную BOT_TOKEN

# Создаем объекты бота и диспетчера
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )

@dp.message(F.audio)
async def send_audio_echo(message: Message):
    await message.answer(
        'Я тоже могу так, смотри:'
    )
    await message.reply_audio(message.audio.file_id)

# Этот хэндлер будет срабатывать на отправку боту фото
@dp.message(F.photo)
async def send_photo_echo(message: Message):
    await message.answer(
        'Я тоже могу так, смотри:'
    )
    await message.reply_photo(message.photo[0].file_id)

@dp.message(F.video)
async def send_video_audio(message: Message):
    await message.answer(
        'Я тоже могу так, смотри:'
    )
    await message.reply_video(message.video.file_id)

@dp.message(F.voice)
async def send_voice_audio(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))
    await message.answer(
        'Я тоже могу так, смотри:'
    )
    await message.reply_voice(message.voice.file_id)

@dp.message(F.document)
async def send_document_echo(message: Message):
    await message.answer(
        'Я тоже могу так, смотри:'
    )
    await message.reply_document(message.document.file_id)

@dp.message(F.sticker)
async def send_sticker_echo(message: Message):
    await message.answer(
        'Я тоже могу так, смотри:'
    )
    await message.reply_sticker(message.sticker.file_id)

@dp.message(F.animation)
async def send_animation_echo(message: Message):
    await message.answer(
        'Я тоже могу так, смотри:'
    )
    await message.reply_animation(message.animation.file_id)

# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    print(message.model_dump_json(indent=4,exclude_none=True)) #Красивый вывод
    await message.reply(text=f'Все говорят "{message.text}", а ты купи слона')

# Регистрация хэндлеров в диспетчере
# dp.message.register(send_photo_echo,F.content_type == ContentType.PHOTO)

if __name__ == '__main__':
    dp.run_polling(bot)