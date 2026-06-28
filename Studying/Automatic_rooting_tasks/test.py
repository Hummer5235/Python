# test_server.py
import sys, os

print('Список параметров, переданных скрипту')
print(sys.argv)
print('Исходные байты')
print([os.fsencode(arg) for arg in sys.argv])