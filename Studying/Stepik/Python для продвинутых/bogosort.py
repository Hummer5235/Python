import random,datetime

def is_sort(nums):                   # отсортирован ли список?
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

def bogosort(nums):                # реализация алгоритма болотной сортировки
    check_time()
    while not is_sort(nums):
        random.shuffle(nums)
    check_time()
    return nums

def check_time():
    start_time = datetime.datetime.now()
    print(f'Time: {start_time} ')


numbers = list(range(12))
random.shuffle(numbers)              # перемешиваем начальный список
print(numbers)                       # выводим начальный список

sorted_numbers = bogosort(numbers)

print(sorted_numbers)    