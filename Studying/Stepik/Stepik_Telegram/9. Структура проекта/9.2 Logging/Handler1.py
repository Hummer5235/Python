# хэндлеры логов отвечают за то, куда какие логи отправлять. А отправлять их можно много куда. Например:
#
# в stdout;
# в stderr;
# в файл;
# в базу данных;
# в специальный сервис хранения и анализа логов;
# старшему главному начальнику на телефон;
# куда угодно.



# За каждым логгером может быть закреплено от нуля до любого количества хэндлеров.
# Хэндлеры логгера можно посмотреть, если обратиться к атрибуту handlers:

import logging
import sys

logger = logging.getLogger(__name__)

stderr_handler = logging.StreamHandler()
stdout_handler = logging.StreamHandler(sys.stdout)



logger.addHandler(stdout_handler)
logger.addHandler(stderr_handler)

print(logger.handlers)

logger.warning('Это лог с предупреждением!')