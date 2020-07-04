birthday = {'carol':'20 apr','bob':'21 sept','katy':'14 sept','sam':'21 apr'}
while True:
    print('Enter the name (or leave empty to quit)')
    name = input()
    if name == '':
        break
    if name in birthday:
        print(birthday[name] + ' is the birthday of ' + name)
    else:
        print('There is no such person in the data base')
        print('Enter their bdate')
        bdate = input()
        birthday[name] = bdate
        print('Database updated' + '\n' + str(birthday))