#! python3
# madLibs.py - Changes the words in a text file.

import pyinputplus as pyip
import re

print('Enter the adjective:')
adjective = pyip.inputStr()
print('\nEnter the noun:')
noun = pyip.inputStr()
print('\nEnter the verb:')
verb = pyip.inputStr()
print('\nEnter the adverb:')
adverb = pyip.inputStr()

text = open('thesample.txt','r')
textContent = text.read()
textContent = textContent.replace('ADJECTIVE',adjective)
textContent = textContent.replace('VERB',verb)
textContent = textContent.replace('NOUN',noun)
textContent = textContent.replace('ADVERB',adverb)

text = open('thesample.txt','w')
text.write(textContent)