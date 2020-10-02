#sorting patterns of text and finding them
import re

contents = '''
Cielo.McGlynn@desiree.org
Micaela@rossie.us
Kaylie_Jones@deion.info
'''

pattern = re.compile(r'[a-zA-Z]+.[a-zA-Z]+@[A-Za-z]+\.[a-z]+')
matches = pattern.finditer(contents)
for match in matches:
        print(match)
# with open('sorted_database.text','r') as f:
#     contents = f.read()
#     
    
    # with open('sorted_database.csv','w') as newf:
    #     fieldnames = ['Full Name','phone','Country','Email']
    #     csv_writer = csv.DictWriter(newf,fieldnames=fieldnames, delimiter = '\n')

    #     for line in csv_reader:
    #         csv_writer.writerow(line)
