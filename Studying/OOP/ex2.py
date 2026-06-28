class Point:
    'Класс для представления координат точек на плоскости'
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y
        
        
    def get_coords(self):
        return (self.x, self.y)


pt1 = Point()
pt2 = Point()
pt1.set_coords(10, 15)
pt2.set_coords(20, 10)

# Имена методов класса - те же самые атрибуты. Только они ведут не на данные , а на функции
f = getattr(pt1, 'get_coords')
print(f())