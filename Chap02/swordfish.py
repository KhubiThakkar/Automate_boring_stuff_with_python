while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('What is your password Joe (It is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('Access Granted')