import pyinputplus as pyip
from pathlib import Path
import re

print('Enter the regex that needs to be searched:')
search = input()
searchRegex = re.compile(search)
p = Path.cwd()

allFiles = list(p.glob('*.txt'))

for i in range(len(allFiles)):
    data_input = open(allFiles[0])
    data_content = data_input.readlines()
    data_input.close()
    for line in data_content:
        match_objects = searchRegex.findall(line)
        if match_objects is not None:
            for match in match_objects:
                print(match)
                print('\n')
    