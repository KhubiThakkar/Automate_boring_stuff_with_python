import re
def newstrip(stri,word = None):
    if word == None:
        patternleft = re.compile(r'^\s*')
        patternright = re.compile(r'^\s$')
        stri = re.sub(patternleft,'',stri)
        stri = re.sub(patternright,'',stri)
        print(stri) 
    else:
     
        pattern = re.compile(word)
        stri = re.sub(pattern,'',stri)
        print(stri)  

newstrip(' hello HEYY   ')
print(' hello HEYY   ')