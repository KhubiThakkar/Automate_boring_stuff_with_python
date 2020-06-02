name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hello Alice')
elif age < 12:
    print('You are not Alice,kiddo')
elif age > 100:
    print('You are not Alice, grannie')
elif age > 2000:
    print('Unlikely,Alice is not immortal, you vampire')        #A problem is introduced as the program jumps out after finding one correct elif statement and won't check the rest