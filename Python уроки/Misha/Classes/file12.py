class Vector(list):
	# pass
	def __str__(self):
		return " ".join(map(str, self))

	def append(self):
		print('Метод append')

v = Vector([1, 2, 3])
print(v)

print(dir(v))
# v.append(100)
print(v)