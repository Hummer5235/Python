
firstname= input("Enter your firstname: ")
lastname= input("Enter your lastname: ")
age=int(input("Enter your age: "))

user={"firstname":"firstname","lastname":"lastname","age":"age"}
print(user)
user2=dict(firstname=firstname,lastname=lastname,age=age)
print(user2)