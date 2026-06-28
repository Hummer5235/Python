class Cars:
    def __init__(self, brand, color, speed):
        self.brand = brand
        self.color = color
        self.speed = speed
        self.distance = 0

    def  __str__(self):
        return f"Car({self.brand},{self.color},Distance = {self.distance})"

    def update(self,number = 1):
        self.distance += self.speed *number

bmw= Cars("bmw","Black",90)
mersedes = Cars("mersedes","Red",95)

bmw.update(95)
mersedes.update(88)



print(bmw.__str__())
print(mersedes.__str__())