def displayInventory(inventory):
    total = 0
    for key in inventory.keys():
        print(str(inventory[key])+' '+key)
        total += inventory[key]
    print('Total number of items '+str(total))

def addtoinventory(inventory,addeditems):
    for items in addeditems:
        num = inventory.get(items,0)
        if num !=0:
            inventory[items]+=1
        else:
            inventory1={items:1}
            inventory.update(inventory1)
    displayInventory(inventory)

stuff = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addtoinventory(stuff,dragonLoot)