# class BankAccount:
# 	def __init__(self,name,balance,passport):
# 		self.__name = name
# 		self.__balance = balance
# 		self.__passport = passport

# 	def print_public_data(self):
# 		print(self.name,self.balance,self.passport)

# 	def print_protected_data(self):
# 		print(self._name,self._balance,self._passport)

# 	def print_private_data(self):
# 		print(self.__name,self.__balance,self.__passport)

# account1 = BankAccount("Bob",100000,452312)
# account1.print_private_data()

class JustCounter:  
    __secret_count = 0  
  
    def count(self):  
        self.__secret_count += 1  
        print(self.__secret_count)  
  
  
counter = JustCounter()  
counter.count()  
counter.count()  

