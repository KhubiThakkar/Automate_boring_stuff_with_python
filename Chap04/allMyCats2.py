catNames=[]
while True:
    print('Enter the name of your cat' + str(len(catNames)+1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('The names of the cats are:')
for name in catNames:
    print(' '+name)