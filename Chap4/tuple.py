print(type(('hello')))      #without the comma it is a string
print(type(('hello',)))     #with comma (at the end) it is a tuple
spam = [1,2,3,4,5,6]
print(tuple(spam))      #convert list into a tuple
spam = (4,5,6,7,8,9)
print(list(spam))       #convert tuple into a list