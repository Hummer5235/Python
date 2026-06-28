# def say(*args):
# 	names = ''
# 	for i in args:
# 		names += i+' and '
# 	names = names[:-5]
# 	# names += '!'
# 	print(names)


# say('Misha')
# say('Misha','Vadim')
# say('Misha','Vadim','Anton')



def say(a,*args):
	names = 'Hello '
	length = len(args)
	names += a 
	if len(args)>0:
		for i in args:
			names += ' and ' + i
		
	names += '!'	
	
	print(names)


say('Misha')
say('Misha','Vadim')
say('Misha','Vadim','Anton')