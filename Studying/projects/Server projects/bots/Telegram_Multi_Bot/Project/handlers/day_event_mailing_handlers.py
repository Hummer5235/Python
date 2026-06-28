from aiogram import Router, F
from aiogram.types import Message

from ..keyboards.keyboards import *
from ..event_day_checker.event_day import *

#Инициализируем роутер уровня модуля
router = Router()



@router.message(F.text ==events_button.text)
async def day_events(message:Message,bot):
    user_id = message.from_user.id
    if users[user_id]['day_event_mailing'] :
        await message.answer(text='Выберите команду:',parse_mode='html',reply_markup=off_events_back_keyboard)
    else:
        await message.answer(text='Выберите команду:', parse_mode='html', reply_markup=on_events_back_keyboard)


@router.message(F.text ==day_event_mailing_start_button.text)
async def day_event_mailing_process(message:Message,bot):
    user = message.from_user
    user_id = user.id
    users[user_id]['day_event_mailing'] = 1
    print('Оповещения включены')
    await message.answer(text='\U0001F514Оповещения включены\nВремя оповещения <b>08:00 МСК</b>',parse_mode='html',reply_markup=start_keyboard)
    await update_users_data(user)


@router.message(F.text ==day_event_mailing_stop_button.text)
async def day_event_mailing_process(message:Message):
    user = message.from_user
    user_id = user.id
    users[user_id]['day_event_mailing'] = 0
    await message.answer(text='\U0001F515Оповещения отключены',reply_markup=start_keyboard)
    await update_users_data(user)

@router.message(F.text == get_event_now_button.text)
async def get_event_now(message:Message,bot):
    user = message.from_user
    user_id = user.id

    await mailing_process(bot, current_user_id=user_id,is_event=await is_event())
    await update_users_data(user)