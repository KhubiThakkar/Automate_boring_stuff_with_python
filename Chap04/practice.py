list = ['hello','bye','regards','hi','yours','forgive','pardon']
# print('Loops with Lists:')
# for words in list:
#     print(words)
# w1,w2,w3,w4,w5,w6,w7 = list
# print('multiple assignment:')
# print (w1)
# print (w2)
# print (w3)
# print (w4)
# print (w5)
# print (w6)
# print (w7)
# print('enumerate Function:')
# for index,words in enumerate(list):
#     print('Index ' + str(index) + ' in lists is ' + words)
# print('Using Random Library:')
# import random 
# print(random.choice(list))
# print(random.shuffle(list))
print('Methods:')
print(list.index('hi'))     #it doesnot return any value it changes the already existing list
print(list)
print(list.append('thanks'))
print(list)
print(list.insert(2,'okay'))
print(list)
print(list.remove('okay'))      #only the first instance of that value will be removed from the list
print(list)
list.sort()     #1. returns no value, changes the already existing list 2. Cannot sort list with both integers and strings 3. uses ACIIbetical order and not alphabetical order
print(list)
list.sort(reverse = True)
print(list)
list.reverse()
print(list)
