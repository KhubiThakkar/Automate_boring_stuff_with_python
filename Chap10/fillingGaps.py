import re
import os

folder =  '../Chap9'
folder = os.path.abspath(folder)

filePattern = re.compile(r"""^(capitalsquiz_answers)(\d)(.*?)$""")
list = os.listdir(folder)
list.sort()

num = 1

for filenames in list:    
    mo = filePattern.search(filenames)

    if mo != None:
        
        if mo.group(2) == str(num):
            num += 1
        
        else:
        
            if num == 1:
                continue
            # mo.group(2) = num
            construction = mo.group(1)+str(num)+mo.group(3)
            num += 1

            originalfilename = os.path.join(folder,mo.group())
            refilename = os.path.join(folder,construction)
            
            os.rename(originalfilename,refilename)
