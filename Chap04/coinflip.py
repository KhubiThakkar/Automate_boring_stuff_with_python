import random
value = 0
for j in range(10000):
    times = 100
    outcomes = []
    for i in range(times):
        if random.randint(0,1) == 0:
            outcomes.append('H')
        else:
            outcomes.append('T')
    numofStreak = 0
    for index in range(len(outcomes)-5):
        i = index + 1
        Streak =0
        while i <= index + 5:
            if outcomes[index] == outcomes[i]:
                Streak += 1
                i += 1
            else:
                break
        if Streak == 5:
            numofStreak += 1
    if numofStreak == True:
        value += 1
    
print(value/100)        #Chance in percentage that there will be a streak of 6 H or T in the outcome for 100 flips.