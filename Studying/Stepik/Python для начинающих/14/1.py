# объявление функции
def draw_triangle():
    g = 1
    for i in range(15):
        print(' '*(7-i)+'*'*g)
        g+=2

# основная программа
draw_triangle()  # вызов функции