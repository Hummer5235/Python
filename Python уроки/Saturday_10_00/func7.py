

inventory = {'веревка':3, 'золотая монета':140, 'меч':1, 'топор':1, 'мясо':1}


def show_inventory():
	for k,v in inventory.items():
		print(v, k)

lst = ['золотая монета','веревка','веревка']

def addToInventory(lst):
	for i in lst:
		if i in inventory:
			inventory[i] += 1
		else:
			inventory[i] = 1

addToInventory(lst)
show_inventory()
