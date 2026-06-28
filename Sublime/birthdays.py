birthdays = {"Nastya":"Apr 27","Galya":"Jan 23","Natasha":"Sept 16"}

while True:
	print("Enter a name: ")
	name= input()
	if name =="":
		break
	if name in birthdays:
		print(birthdays[name]+" is the birthday of " + name)
	else:
		print("I don't have a birthday information for " + name)
		print("What is treir birthday?")
		bday=input()
		birthdays[name]=bday
		print("Birthday database updated")