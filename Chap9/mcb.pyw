#! python3
#mcb.pyw - saves and loads piecces of text to the clipboard.
#Usage: py.exe mcb.py save <keyword> - Saves clipboard to keyword.
#   py.exe mcb.pyw <keyword> - loads keyword to clipboard.
#   py.exe mcb.pyw list - loads all keyboards to clipboard

import shelve,pyperclip,sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
mcbShelf.close()