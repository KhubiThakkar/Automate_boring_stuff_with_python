#! python3
#mapIt.py - launches a map in the browser using an address from the command line or clipboard.

import webbrowser,sys,pyperclip
webbrowser.open('https://inventwithpython.com')
if len(sys.argv)>1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/'+address)