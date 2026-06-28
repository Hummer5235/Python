import asyncio
from datetime import datetime
from ..data.users_data import *
from aiogram import Bot
from ..path_file import data_path
from ..keyboards.keyboards import *


current_date :str = ''

hour = 8
minute = 0
time_to_mailing = (hour,minute)
event_date = None
event = None
dates:dict = {}



month_dictionary = {
    1:'Января',
    2:'Февраля',
    3:'Марта',
    4:'Апреля',
    5:'Мая',
    6:'Июня',
    7:'Июля',
    8:'Августа',
    9:'Сентября',
    10:'Октября',
    11:'Ноября',
    12:'Декабря'
}




async def check_time_to_mailing_process():
    global current_date
    time = datetime.now()
    print(f'{time.strftime("%H:%M:%S")} Проверка времени')
    current_date = str(time.day)+' '+ month_dictionary[time.month]
    if (time.hour,time.minute) == time_to_mailing:
        return True


async def is_event():
    global event_date,event
    print('Проверяем наличие праздников на сегодня')
    for event_date, value in dates.items():
        if event_date == current_date:
            event = '\U0001F7E2'+'\n\U0001F7E2'.join(value)
            return True
    return False


async def mailing_process(bot:Bot,current_user_id = None,is_event = True):
    if current_user_id == None :
        print('Рассылка')
        for user_id in users:
            if users[user_id]['day_event_mailing']:
                if is_event:
                    await bot.send_message(user_id, f'\U0001F514Оповещение о праздниках:\n\n<b>{current_date}:</b>\n\n{event}',parse_mode='html',reply_markup=start_keyboard)
                else:
                    await bot.send_message(user_id,f'\U0001F514Оповещение о праздниках:\n\n<b>{current_date}:</b>\n\nНа сегодня нет праздников, известных мне, удивительно)',parse_mode='html',reply_markup=start_keyboard)
    else:
        if is_event:
            await bot.send_message(current_user_id, f'\U0001F514Оповещение о праздниках:\n\n<b>{current_date}:</b>\n\n{event}',parse_mode='html',reply_markup=start_keyboard)
        else:
            await bot.send_message(current_user_id,f'\U0001F514Оповещение о праздниках:\n\n<b>{current_date}:</b>\n\nНа сегодня нет праздников, известных мне, удивительно)',parse_mode='html', reply_markup=start_keyboard)

async def get_events():
    print('Получаем все даты и праздники!')
    with open(data_path / 'holidays_dates.txt', encoding='utf-8') as file:
        dictionary = {}
        sep = '-'
        for line in file:
            if line[0].isdigit():
                line = line.strip('\n')
                date = line[:line.index('-') - 1]
                line = line[line.index('-') + 2:]
                if not dictionary.get(date):
                    dictionary[date] = []
                dictionary[date].append(line)
    return dictionary

async def mailing_events_loop(bot):
    global dates
    dates = await get_events()
    while True:
        if await check_time_to_mailing_process():
            await mailing_process(bot,is_event=await is_event())
            await asyncio.sleep(60)
        await asyncio.sleep(1)

