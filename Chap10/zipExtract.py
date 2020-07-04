import zipfile,os
from pathlib import Path
p = Path('/home/khubithakkar/Desktop/OnlineClass')
exampleZip = zipfile.ZipFile(p/'standard5.zip')
# exampleZip.extractall()
# exampleZip.close()

exampleZip.extract('eemh1dd/eemh101.pdf')
exampleZip.close()