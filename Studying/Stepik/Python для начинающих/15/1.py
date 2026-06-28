def is_valid(data):
	if data.isdigit() and 1<= int(data) <= 100:
		return True
	else:
		return False



print(is_valid('10'))
print(is_valid('140'))