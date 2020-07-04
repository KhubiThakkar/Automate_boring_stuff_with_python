import re
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number (is 415-555-4242')
# print('Phone number found '+mo.group())
# print(mo.group(1))
# print(mo.group(2))

#multiple groups with pipe
# hero = re.compile(r'Batman|Tina Fey')
# mo1 = hero.search('Batman and Tina Fey')
# print(mo1.group())
# mo2 = hero.search('Tine Fey and Batman')
# print(mo2.group())

# batRegex=re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel')
# print(mo.group())
# print(mo.group(1))

#optional matching with the question mark
# batRegex = re.compile(r'Bat(wo)?man')
# mo1 = batRegex.search('The adventures of Batman')
# mo2 = batRegex.search('The adventures of Batwoman')
# print(mo1.group() + mo2.group())

#matching zero or more with the star

# batRegex = re.compile(r'Bat(wo)*man')
# mo1 = batRegex.search('The adventures of the Batman')
# mo2 = batRegex.search('The adventures of the Batwowowowoman')
# print(mo1.group() + mo2.group())

#greedy and nongreedy
# greedyHa = re.compile(r'(Ha){3,5}')
# mo1 = greedyHa.search('HaHaHaHaHaHaHaHaHa')
# nongreedyHa = re.compile(r'(Ha){3,5}?')
# mo2 = nongreedyHa.search('HaHaHaHaHaHaHaHaHa')
# print(mo1.group() + ' ' + mo2.group())

#findall() 
# xmasRegex = re.compile(r'\d+\s\w+')
# print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 patridge'))

#making your character class
# vowelRegex = re.compile(r'[aeiouAEIOU]')
# print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

#normal regular expression symbols 
# regex = re.compile(r'[a-zA-Z0-9\-.]')       #you do not need to escape only hyphens and not other symbols inside the square brackets.
# print(regex.findall('Robocop - is ask not . why?'))


#negative character class
# consonant = re.compile(r'[^aeiouAE^IOU]')
# print(consonant.findall('RoboCop eats baby food. BABY ^ FOOD.'))

#caret and dollar sign
# beginswith = re.compile(r'^hello')
# print(beginswith.findall('hello, world hello1 hello2'))

# endswith = re.compile(r'\d$')
# print(endswith.findall('hello 32'))

# #wildcard character
# at = re.compile(r'..at')
# print(at.findall('the cat in the hat sat on the flat mat'))

# name = re.compile(r'first name:(.*) last name:(.*)')
# mo = name.search('first name:al last name:sweigart')
# print(mo.group(1) + mo.group(2))

#non greedy
# nongreedy = re.compile(r'<.*?>')
# mo = nongreedy.search('<to serve man>for dinner.>')
# print(mo.group())

#matching newlines with dot character
# nonewline = re.compile('.*')
# print(nonewline.search('serve the public trust.\nprotect the innocent.\nuphold the load.').group())

# newline = re.compile('.*',re.DOTALL)
# print(newline.search('serve the public trust.\nprotect the innocent.\nuphold the load.').group())

# #case insensitive
# robocop = re.compile(r'robocop',re.I)
# print(robocop.search('robOCop is a part man, part machine, all cop').group())

# substituting strings with sub()
names = re.compile(r'agent \w+')
print(names.sub('CENSORED','agent alice gave the secret documents to agent bob.'))

