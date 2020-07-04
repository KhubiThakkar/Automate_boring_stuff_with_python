def displayInventory(inventory):
    total = 0
    for key in inventory.keys():
        print(str(inventory[key])+' '+key)
        total += inventory[key]
    print('Total number of items '+str(total))
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(inv)