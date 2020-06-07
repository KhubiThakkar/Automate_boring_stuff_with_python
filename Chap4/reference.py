#the varible stores only the reference(memory location) of the list stored
spam = [1,2,3,4,5,6,7,8,9,0]
cheese = spam
cheese[4] = 'HELLO'
print(spam)
print(cheese)
#we just changed the value in list of variable cheese but as cheese and spam point to memory location of the same list both their values change.
print(id(spam))     #the location of the list