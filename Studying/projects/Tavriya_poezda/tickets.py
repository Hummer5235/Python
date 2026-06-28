import time
from tickets_api_service import get_html_page , parse_html , parse_json, Place_Type
from answer_formatter import output



while True:
    try:
        html_page = get_html_page('https://grandtrain.ru/tickets/2000000-2064788/01.01.2024/092М/')
        json_file = parse_html(html_page)
        result,time_length = parse_json(json_file,Place_Type.upper_side)
        output(result,time_length)
        time.sleep(20)
    except:
        print('Нет соединения с интернетом!')
        time.sleep(5)



