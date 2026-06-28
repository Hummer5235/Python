from pprint import pprint
inventory={"rope":1,"torch":6,"gold coin":42,"dagger":1,"arrow":12}


def displayInventory(lst):
	total_items=0
	print("Inventory:")
	for i,m in inventory.items():
		print(m,i)
		total_items+=m
	print(f"Toral number of items: {total_items}")

dragonLoot=["gold coin","dagger","gold coin","gold coin","ruby"]


def addToInventory(inventory,addedItems):
	for i in addedItems:
		if i in inventory:
			inventory[i]= inventory[i]+1
		else:
			inventory.setdefault(i,1)


addToInventory(inventory,dragonLoot)
displayInventory(inventory)


