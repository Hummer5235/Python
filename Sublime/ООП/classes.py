

class heroes:
	def __init__ (self,name,health,power,speed,stamina,age):
		self.name = name
		self.health = health
		self.power = power
		self.speed = speed
		self.stamina = stamina
		self.age = age
		
	def __str__(self):
		return f"""hero(Name= {self.name},health={self.health},
power={self.power},speed={self.speed},stamina={self.stamina},age={self.age})"""

	def update_health(self,b):
		self.health+=b

	def update_stamina(self,b):
		self.stamina+=b


Owl = heroes("Owl",100,50,30,50,25)

print(Owl)
print()
Owl.update_health(20)
Owl.update_stamina(-40)
print(Owl)