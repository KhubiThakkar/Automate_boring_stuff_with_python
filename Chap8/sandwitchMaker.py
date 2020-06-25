import pyinputplus as pyip

pricing = {'wheat':8,'white':9,'sourdough':10,'chicken':15,'ham':20,'turkey':25,'tofu':10,'cheddar':8,'swiss':10,'mozzarella':12}
price = 0

bread = ['wheat','white','sourdough']
protein = ['chicken', 'turkey','ham','tofu']
cheese = ['cheddar','swiss','mozzarella']
chooseB = pyip.inputMenu(bread)
chooseP = pyip.inputMenu(protein)
wantC = pyip.inputYesNo(prompt='Do you want cheese')
if wantC == 'yes':
    chooseC = pyip.inputMenu(cheese)
    price += pricing.get(chooseC)
number = pyip.inputInt(prompt='How many sandwitches you want?')



price += pricing.get(chooseB)
price += pricing.get(chooseP)
price = price * number

print('The price for you sandwitch(s) is/are: %s'%price)
