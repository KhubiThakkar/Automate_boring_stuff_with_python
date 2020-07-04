#This program says hello and asks for my name.

print('hello world')
print('What is your name?')
myName = input()
print('It is good to meet you, '+myName)
print('The length of yur name is')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be '+str(int(myAge)+1)+' in an year')   #input() function always returns a string