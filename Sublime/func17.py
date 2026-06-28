

def three_args(*,var1=None,var2=None,var3=None):
	if var1 != None:
		print(var1)
	if var2 != None:
		print(var2)
	if var3 != None:
		print(var3)
	return ""


print(three_args(var1=7,var2=11,var3=4))
