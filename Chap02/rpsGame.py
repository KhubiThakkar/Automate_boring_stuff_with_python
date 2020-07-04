import random
import sys
print('ROCK,PAPER,SCISSORS')
wins = 0
losses = 0
ties = 0
move = ''
while True:
    print(str(wins) + ' Wins,' + str(losses) + ' Losses,' + str(ties) + ' Ties')
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    move = input()
    
    randInt = random.randint(1,3)
    if randInt == 1:
        computer = 'ROCK'
    elif randInt == 2:
        computer = 'SCISSORS'
    elif randInt == 3:
        computer = 'PAPER'

    if move == 'r':
        print('ROCK versus...')
        if computer == 'ROCK':
            print(computer)
            print('It''s a tie!')
            ties += 1
        elif computer == 'SCISSORS':
            print(computer)
            print ('You won!')
            wins += 1
        elif computer == 'PAPER':
            print(computer)
            print('You lose!')
            losses += 1
    elif move == 'p':
        print('PAPER versus...')
        if computer == 'ROCK':
            print(computer)
            print('You won!')
            wins += 1
        elif computer == 'SCISSORS':
            print(computer)
            print ('You lose!')
            losses += 1
        elif computer == 'PAPER':
            print(computer)
            print('It''s a tie!')
            ties += 1
    elif move == 's':
        print('SCISSORS versus...')
        if computer == 'ROCK':
            print(computer)
            print('You lose!')
            losses += 1
        elif computer == 'SCISSORS':
            print(computer)
            print ('It''s a tie!')
            ties += 1
        elif computer == 'PAPER':
            print(computer)
            print('You won!')
            wins += 1
    elif move == 'q':
        sys.quit()
    