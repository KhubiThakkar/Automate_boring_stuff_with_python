allguests = {'alice':{'apples':5,'pretzels':12},'bob':{'ham sandwich':3,'apples':2},'carol':{'cups':3,'apple pie':1}}
def totalbrought(guests,item):
    numbrought = 0
    for k,v in guests.items():
        numbrought = numbrought+v.get(item,0)
    return numbrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalbrought(allguests, 'apples')))
print(' - Cups           ' + str(totalbrought(allguests, 'cups')))
print(' - Cakes          ' + str(totalbrought(allguests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalbrought(allguests, 'ham sandwich')))
print(' - Apple Pies     ' + str(totalbrought(allguests, 'apple pie')))