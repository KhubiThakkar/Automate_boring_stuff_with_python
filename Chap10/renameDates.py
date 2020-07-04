#! python3
#renameDates.py - renames filenames with american dates to european date format

import shutil,os,re

datePattern = re.compile("""^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$""",re.VERBOSE)
for amerfilenames in os.listdir('.'):
    mo = datePattern.search(amerfilenames)

    if mo == None:
        continue
    else:
        beforepart = mo.group(1)
        monthpart = mo.group(2)
        datepart = mo.group(4)
        yearpart = mo.group(6)
        afterpart = mo.group(8)
        

        eurofilename=beforepart+datepart+'-'+monthpart+'-'+yearpart+afterpart

        absWorkingDir=os.path.abspath('.')
        amerfilenames = os.path.join(absWorkingDir,amerfilenames)
        eurofilename = os.path.join(absWorkingDir,eurofilename)

        print('renaming' + amerfilenames+'to'+eurofilename)
        shutil.move(amerfilenames,eurofilename)


