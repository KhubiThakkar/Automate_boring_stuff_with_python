from pathlib import Path
import os
# print(Path('spam','bacon','eggs'))
# print(Path('spam')/'bacon'/'eggs')
# homefolder = Path('/home/khubi')
# subfolder = Path('Desktop')
# print(homefolder/subfolder)
# print(Path.cwd())
# print(Path.home())

# os.makedirs('A/B/C')

# print(Path.cwd().is_absolute())

# p = Path.cwd()/'path.py'
# print(p)
# print(p.anchor)
# print(p.name)
# print(p.stem)
# print(p.suffix)
# print(p.drive)

# path = Path('/home/khubithakkar/Desktop')
# # print(os.path.getsize(path))
# # print(os.listdir(path))
# path = path/'noobie/Automate_boring_stuff_with_python'
# print(os.listdir(path))

# totalsize = 0
# for filename in os.listdir(path):
#     totalsize = totalsize+os.path.getsize(os.path.join(path,filename))
# print(totalsize)

# print(list(path.glob('Chap?')))

# print(path.exists())
# print(path.is_file())
# print(path.is_dir())

# p = Path('spam.txt')
# p.write_text('Hello world')
# print(p.read_text())


# reading text files
# hello = open(Path.cwd()/'spam.txt','r')
# hContent = hello.read()
# print(hContent)

# sonnet = open('sonnet29.txt')
# print(sonnet.readlines())

# hello.close()

#writing text files
# baconFile = open('bacon.txt','w')
# baconFile.write('Hello World!\n I am Khubi.\n I am the Queen of your world\n All bow down to me.')
# baconFile.close()

# baconFile = open('bacon.txt','a')
# baconFile.write('\nCaio')
# baconFile.close()

import shelve
# shelfFile = shelve.open('mydata')
# cats = ['zophie','pooka','simon']
# shelfFile['cats'] = cats
# shelfFile.close()

shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()

