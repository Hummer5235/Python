# объявление функции
def get_next_prime(num):
    
    i = 1
    while True:
        counter = 0
        for g in range(2,num+i+1):
            if (num+i)%g == 0:
                counter +=1
        if counter == 1 and num+i != num:
            return (num+i)
        i += 1
# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))