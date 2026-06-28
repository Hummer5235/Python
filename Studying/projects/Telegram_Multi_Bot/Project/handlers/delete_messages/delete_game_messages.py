import logging

# Словарь, в котором будут храниться данные пользователей
from ..game_handlers import users

async def delete_message_from_bot(user_id,bot):
    if user_id in users:
        message_ids_list: list = users[user_id]['bot_messages_ids']
        logging.info(f'Сообщения бота : {message_ids_list}')
        if len(message_ids_list) >0 :
            users[user_id]['bot_messages_ids'] = []
            logging.info(f'Сообщения бота удалены : {message_ids_list}')
            await bot.delete_messages(chat_id=user_id, message_ids=message_ids_list)



async def delete_message_from_user(user_id,bot):
    message_ids_list: list = users[user_id]['user_messages_ids']
    logging.info(f'Сообщения пользователя : {message_ids_list}')
    if len(message_ids_list) > 0:
        users[user_id]['user_messages_ids'] = []
        logging.info(f'Сообщения пользователя удалены : {message_ids_list}')
        await bot.delete_messages(chat_id=user_id,message_ids=message_ids_list)