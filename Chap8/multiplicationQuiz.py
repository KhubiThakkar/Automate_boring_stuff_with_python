import pyinputplus as pyip
import random,time
numOfQuestions = 10
correctanswer = 0
for quesNumber in range(numOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    answer = num1 * num2
    promt = '#%s: %s x %s ='%(quesNumber,num1,num2)
    try:
        pyip.inputStr(promt,allowRegexes=['^%s$'%answer],blockRegexes = [('.*','incorect')],timeout=8,limit=3)
    except pyip.TimeoutException:
        print('out of time')
    except pyip.RetryLimitException:
        print('out of tries')
    else:
        print('correct')
        correctanswer +=1
    time.sleep(1)
print('score: %s / %s'%(correctanswer,numOfQuestions))