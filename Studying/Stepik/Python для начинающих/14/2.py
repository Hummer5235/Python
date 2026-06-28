# объявление функции
from math import factorial as f
def compute_binom(n, k):
    return f(n)/(f(k)*f(n-k))

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))