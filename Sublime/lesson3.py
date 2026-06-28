class Cat:
	breed = "pers"

	def hello(*args):
		print("Hello from kitty",args)

	def show_breed(self):
		print(f'My breed is {self.breed}')

	def show_name_and_age(self):
		if hasattr(self,"name"):
			print(f"My name is {self.name}")
			print(f"I am {self.age} years old")

		else:
			print("nothing")

	def set_value(self,value,age = 0):
		self.name = value
		self.age = age

walt = Cat()
walt.set_value("Walt",5)
walt.show_breed()
walt.show_name_and_age()
