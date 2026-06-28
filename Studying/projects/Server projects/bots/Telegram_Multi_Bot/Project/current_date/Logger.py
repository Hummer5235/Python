import logging

logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w',
                    format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger('__name__')

try:
    logging.info(f"successful result")
except Exception as err:
    logging.exception("Error")