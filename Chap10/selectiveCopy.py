#! python3
# selectiveCopy.py - walks through a folder tree and searches for files with certain file extension(.py) and copies to another folder.

import os
import re
import shutil
from pathlib import Path

def selectiveCopy(folder):

    folder = os.path.abspath(folder)
    copyLocation = os.path.dirname(folder)

    fileExtension = re.compile(r'^(.*?)\.py$')

    for foldername, subfolders, filenames in os.walk(folder):
       

        for filename in filenames:

            filename = fileExtension.search(filename)
 
            if filename == None:
                continue
            
            pathFile = os.path.join(foldername,filename.group())
            print(pathFile)

            shutil.copy(pathFile,copyLocation+'/folderCopy')
           
    print('DONE!!')

print('Enter the path for the folder...')
folder = '/home/khubithakkar/Desktop/noobie/Automate_boring_stuff_with_python/Chap9'
selectiveCopy(folder)