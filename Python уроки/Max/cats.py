class Cats:
    def __init__(self,breed,name,age):
        self.breed = breed
        self.name = name
        self.age = age

    def  __str__(self):
        return f"Cat({self.name},{self.breed},{self.age})"



cat1= Cats("British","Black",3)
cat2 = Cats("Siamskiy","Barsik",25)

print(cat1.__str__())
print(cat2.__str__())