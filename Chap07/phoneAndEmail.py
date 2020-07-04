#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip,re

phoneregx = re.compile(r'''((\d{3}|\(\d{3}\))?        (\s|-|\.)?      (\d{3})     (\s|-|\.)     (\d{4})     (\s*(ext|x|ext.)\s(\d{2,5}))?)''',re.VERBOSE)

emailregx = re.compile(r'''(\w+@\w+\.\w{2,4})''')

text = str(pyperclip.paste())
matches = []
for groups in phoneregx.findall(text):
    phonenum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phonenum = 'x'+groups[8]
    matches.append(phonenum)
for groups in emailregx.findall(text):
    matches.append(groups)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard')
    print('\n'.join(matches))
else:
    print('no matches found.')