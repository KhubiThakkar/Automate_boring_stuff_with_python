import random
i = 0
correct = random.randint(1,20)
print('I am thinking of a number 1 and 20')
guess = '21'
while int(guess) != correct:
    print('Take a Guess')
    guess = input()
    i += 1
    if int(guess) < correct:
        print('Your guess is too low.')
    elif int(guess) > correct:
        print('Your guess is too high.')
print('God job! You guessed my number in '+ str(i) + ' guesses!')