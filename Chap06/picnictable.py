def printpicnic(items,leftwidth,rightwidth):
    print('PICNIC ITEMS'.center(leftwidth+rightwidth,'-'))
    for k,v in items.items():
        print(k.ljust(leftwidth,'.')+str(v).rjust(rightwidth)
        )
picnicitems = {'sandwitch':4,'apples':12,'cups':4,'cookies':8000}
printpicnic(picnicitems,12,5)