import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     format='[%(asctime)s] #%(levelname)s %(filename)s:'
#            '%(lineno)s - %(name)s - %(message)s'
# )


logging.basicConfig(
    level=logging.DEBUG,
    format='[{asctime}] #{levelname:8} {filename}:'
           '{lineno} - {name} - {message}',
    style='{'
)


logger = logging.getLogger(__name__)

logger.debug('Лог уровня DEBUG')
logger.debug('Лог уровня DEBUG')