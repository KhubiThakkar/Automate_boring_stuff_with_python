import pyinputplus as pyip
import random,time
numberOfQues = 10
correctAns = 0
for number in range(numberOfQues):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    try:
        print('#%s: %s * %s'%(number,num1,num2))
        answer = pyip.inputStr(allowRegexes=['^%s$'%(num1*num2)],blockRegexes=[('.*','Incorrect')],limit=3,timeout=8)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('correct')
        correctAns += 1
print('%s / %s' %(correctAns,numberOfQues))