#game of guess the number
import random

num = random.randint(0,100)
select = input("select a value between 0 to 100: ")
select = int(select)
if num<select:
    print("too high")
elif num>select:
    print ("too low")
else:
    print("correct guess")
