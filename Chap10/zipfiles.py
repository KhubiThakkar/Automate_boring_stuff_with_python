import zipfile,os

from pathlib import Path
p = Path('/home/khubithakkar/Desktop/OnlineClass')

exampleZip = zipfile.ZipFile(p/'standard5.zip')
print(exampleZip.namelist())

spaminfo = exampleZip.getinfo('eemh1dd/eemh101.pdf')
print(spaminfo.file_size)
print(spaminfo.compress_size)
print('compressed file is %sx smaller' %round(spaminfo.file_size/spaminfo.compress_size,2))

