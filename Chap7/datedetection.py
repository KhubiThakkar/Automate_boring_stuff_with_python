import re
date = re.compile(r'([0-3][0-9])/([0-1][0-9])/([1-2][0-9][0-9][0-9])')
text = '31/02/2020 01/00/1955 11/04/1999'
for groups in date.findall(text):
    print(groups[0] + groups[1] + groups[2])
    print(int(groups[0]) == 00 or int(groups[1]) == 00)
    print(int(groups[1]) == 1 or int(groups[1]) == 3 or int(groups[1]) == 5 or int(groups[1]) == 7 or int(groups[1]) == 8 or int(groups[1]) == 10 or int(groups[1]) == 12)
    print(int(groups[1]) == 4 or int(groups[1]) == 6 or int(groups[1]) == 9 or int(groups[1]) == 11)
    if int(groups[0]) == 00 or int(groups[1]) == 00:
        print (groups[0] +'/' +groups[1]+'/'+groups[2] + ' is an invalid date. \n')
    elif int(groups[1]) == 1 or int(groups[1]) == 3 or int(groups[1]) == 5 or int(groups[1]) == 7 or int(groups[1]) == 8 or int(groups[1]) == 10 or int(groups[1]) == 12:
        if int(groups[0])>31:
            print (groups[0] +'/' +groups[1]+'/'+groups[2] + ' is an invalid date. \n')
    elif int(groups[1]) == 4 or int(groups[1]) == 6 or int(groups[1]) == 9 or int(groups[1]) == 11:
        if int(groups[0])>30:
            print (groups[0] +'/' +groups[1]+'/'+groups[2] + ' is an invalid date. \n')
    elif int(groups[1]) == 2:
        if int(groups[0])>29:
            print (groups[0] +'/' +groups[1]+'/'+groups[2] + ' is an invalid date. \n')
    else:
        if groups[1] == '02':
            if int(groups[2])%4 == 0:
                if int(groups[2])%100 == 0:
                    if int(groups[2])%400 == 0:
                        print (groups[0] +'/' +groups[1]+'/'+groups[2] + ' is a valid date. \n')
                    else:
                        print (groups[0] +'/' +groups[1]+'/'+groups[2] + ' is an invalid date. \n')
                else:
                    print (groups[0] +'/' +groups[1]+'/'+groups[2] + ' is a valid date. \n')
            else:
                if int(groups[0])>28:
                    print (groups[0] +'/' +groups[1]+'/'+groups[2] + ' is an invalid date. \n')
                else:
                    print (groups[0] +'/' +groups[1]+'/'+groups[2] + ' is a valid date. \n')
        else:
            print (groups[0] +'/' +groups[1]+'/'+groups[2] + ' is a valid date. \n')


        

        