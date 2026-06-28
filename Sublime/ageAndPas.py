while True:
	print("Please , enter your age: ")
	age=input()
	if age.isdecimal():
		print()
		break

	print()
	print("Please enter a number for your age.")

while True:
	print("Select a new password(letters and numbers only): ")
	password= input()
	if password.isalnum():
		break
	print()
	print("Passwords can only have letters and numbers.")


