from .Date import get_date
from .Numbers_Api import get_fact
from .Googletrans_Api import get_translate
from .Logger import *


def main():
    day, month = get_date()
    fact = get_fact(month, day)
    print(fact)
    text = get_translate(fact)
    logging.info(f"successful result")
    return text






