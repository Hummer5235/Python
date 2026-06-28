from __future__ import annotations
from aiogram.types import (Message,KeyboardButton,ReplyKeyboardMarkup)
from aiogram import Router,F
from aiogram.filters import BaseFilter
from ..payments.Count_month_payments import count_payments
from ..keyboards.keyboards import *
from .delete_messages.delete_game_messages import delete_message_from_bot

#Инициализируем роутер уровня модуля
router = Router()

users_ids = []

LEXICON = {'error':'Ошибка подсчета платежей.\n'
                    'Убедитесь что данные отправлены в формате:\n'
                    '(Стоимость) день,день...\n'
                    '(Стоимость) день,день...\n\n' 
                    '<b>Пример:</b>\n'
                    '(1000) 1,8,15,22,29\n'
                    '(1200) 1,8,15,22,29',

           'format':'Отправьте список оплат в формате:\n'
                    '(Стоимость) день,день...\n'
                    '(Стоимость) день,день...\n\n'
                    '<b>Пример:</b>\n'
                    '(1000) 1,8,15,22,29\n'
                    '(1200) 1,8,15,22,29',

           'choose_command':'Выберите команду:'}



class IsPayments(BaseFilter):
    def __init__(self, users_ids:list[int])->None:
        # В качестве параметра фильтр принимает список с целыми числами
        self.users_ids = users_ids

    async def __call__(self,message:Message)->bool:
        return message.from_user.id in self.users_ids




#Этот хендлер срабатывает при нажатии кнопки Посчитать платежи
@router.message(F.text == payments_button.text)
async def process_payments_command(message:Message,bot):
    user_id = message.from_user.id

    await delete_message_from_bot(user_id,bot) #Удаляем сообщения бота
    # await process_exit_game(message,bot) #Выходим из игры

    users_ids.append(user_id) #Добавляем пользователя в список
    await message.answer(text = LEXICON['format'],parse_mode='html',reply_markup=back_keyboard)

@router.message(IsPayments(users_ids),F.text==back_button.text)
async def process_exit_payments(message:Message):
    user_id = message.from_user.id
    users_ids.pop(users_ids.index(user_id))
    await message.answer(text=LEXICON['choose_command'],reply_markup=start_keyboard)

#Этот хендлер срабатывает при отправке любого сообщения, когда пользователь уже выбрал команду посчитать платежи
@router.message(IsPayments(users_ids))
async def process_other_answers(message:Message):
    user_id = message.from_user.id
    try:
        result = count_payments(message.text)

        if result != None:
            await message.answer(f'Сумма платежей: {result} Руб.')
        else:
            await message.answer(text=LEXICON['error'],parse_mode='html')
    except:
        await message.answer(text=LEXICON['error'],parse_mode='html')
    await process_exit_payments(message)

