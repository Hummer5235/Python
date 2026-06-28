from Telegram_Api import get_updates
from Logger import *

API_URL = 'https://api.telegram.org/bot'

while True:
    try:
        get_updates()
        logger.info('successful result')
    except Exception:
        logger.exception(Exception)




