import re
match = []
pattern = re.compile(r'[a-zA-Z0-9]{8,}')
print('Enter your password:')
password = input()
num = 0
upper = 0
lower = 0
match = pattern.search(password)
if match == None:
    print('Password is not Strong enough')
else:
    for i in range(len(match[0])):
        if match[0][i].isdigit():
            num+=1
        if match[0][i].isupper():
            upper+=1
        if match[0][1].islower():
            lower+=1
    if num < 1:
        print('Password is not Strong enough')
    elif upper < 1:
        print('Password is not strong enough')
    elif lower < 1:
        print('Password is not strong enough')
    else:
        print('Valid Password')