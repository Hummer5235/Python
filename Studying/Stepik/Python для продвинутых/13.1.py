#Decimal число
from decimal import *


num1 = Decimal('-1.456543')
num2 = float('-1.456543')

print(num1, num2)
print(num1.as_tuple()) # Как словарь
print(getcontext())
getcontext().prec = 5
print(getcontext())

print(num1*2)
