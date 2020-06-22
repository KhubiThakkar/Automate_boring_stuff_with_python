#!python3
# mclip.py - A multi-clipboard program.
text={'agree':"""Yes, I agree.That sounds fine.""",'busy':"""Sorry, can we do this later this week or next week??""",'upsell':"""Would you consider making this monthly donation?"""}

import sys, pyperclip 
if len(sys.argv)<2:
    print('Usage: python mclip.py[keyphrase] - copy phrase text')
    sys.exit()
keyphrase = sys.argv[1]     #first command line arg is the keyphrase
if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print('text for '+keyphrase+' copied to clipboard.')
else:
    print('There is no text for '+keyphrase)

#you might come across an 'Pyperclip could not find a copy/paste mechanism for your system' error if you are using Linux. For that you can install xsel utility by '$ sudo apt install xsel'