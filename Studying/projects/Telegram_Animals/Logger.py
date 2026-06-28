import logging

logging.basicConfig(level=logging.INFO,filename='cats_py_log.log',filemode='w',
                    format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger('__name__')
