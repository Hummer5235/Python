#__len__() – позволяет применять функцию len() к экземплярам класса
#__abs__() - позволяет применять функцию abs() к экземплярам класса


class Point:
    def __init__(self, *args):
        self.coords = args

    def __len__(self):
        print(type(self.coords))
        return len(self.coords)

p = Point(10,15)
print(len(p))
