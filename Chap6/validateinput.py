while True:
    print('Enter you  age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter valid age')

while True:
    print('Select a password(letters and numbers only)')
    password = input()
    if password.isalnum():
        break
    print('Passwords can have only letters and numbers')