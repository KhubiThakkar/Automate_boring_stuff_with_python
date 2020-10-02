#creating strong random passwords
import secrets
import string
import random
lenght=input('how long should be the password')
lenght=int(lenght)
if lenght<6:
    print("The password should be atleast 6 digits long")
else:
    letters=input('how many letters in the password')
    letters=int(letters)
    numbers=input('how many numbers in the password')
    numbers=int(numbers)
    addition=letters+numbers
    if addition<lenght:
        password=''
        print(password)
        while letters>0:
            password=password+secrets.choice(string.ascii_letters)
            print(password)
            letters -= 1
            lenght -= 1
        while numbers>0:
            password=password + secrets.choice(string.digits)
            print(password)            
            numbers -= 1
            lenght -=1
        while lenght>0:
            password=password + secrets.choice(string.punctuation)
            print(password)
            lenght-=1
        l=list(password)
        random.shuffle(l)
        password=''.join(l)
        print('the password is',password)


