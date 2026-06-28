import copy
import random


b = []




Counter = 0


while True:
 for i in range(10):
  a = random.randint(1, 10)
  b.append(a)
 print(b)
 if b[0] == b[1] == b[2] == b[3] == b[4] == b[5] == b[6] == b[7] == b[8] == b[9]:
  break
 Counter += 1
 b.clear()


print('Количество попыток : ',Counter)