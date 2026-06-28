class Point:


    def set_coords(self,x,y):
        self.x = x
        self.y = y

    def get_coords(self):
        print(self.x,self.y)

a = Point()
b = Point()

a.set_coords(10,5)
b.set_coords(33,15)

a.get_coords()
b.get_coords()
