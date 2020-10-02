#game of rock, paper, scissors
import random
options='rock','paper','scissors'
s=1
while (s==1):
    value=random.choice(options)
    print(options)
    taken=input('enter the your choice')
    taken=taken.lower()
    print('opponents choice is ', value)
    if taken=='rock':
        if value=='paper':
            print('YOU lose!!')
        else :
            print('You win')
    elif taken=='paper':
        if value=='scissors':
            print(' YOU lose!!')
        else :
            print('You win')
    elif taken=='exit':
        break
    else:
        if value=='rock':
            print('YOU lose!!')
        else:
            print('You win')