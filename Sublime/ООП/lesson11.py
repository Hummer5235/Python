#Property. getter - метод и setter метод

class BankAccount:

	def __init__(self,name,balance):
		self.name = name
		self.__balance = balance

	def get_balance(self):
		return self.__balance

	def set_balance(self,value):
		if not isinstance(value,(int,float)):
			raise ValueError("Баланс должен быть числом")
		self.__balance = value

	# def delete_balance(self):
	# 	print("delete_balance")
	# 	del self.__balance

	balance = property(fget =get_balance,fset = set_balance) #fdel = delete_balance
c = BankAccount("Nikolya",1000)
print(c.balance)
c.balance = 777
print(c.balance)