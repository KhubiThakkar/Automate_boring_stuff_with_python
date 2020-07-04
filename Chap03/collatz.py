import sys
def collatz(number):
    if number%2 == 0:
        return number//2
    else:
        return 3*number+1
try:
    print('Please enter an integer')
    num = input()
    num = int(num)
    while num != 1:
        num = collatz(num)
        print(num)

except ValueError:
    sys.exit()