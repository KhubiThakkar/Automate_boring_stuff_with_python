spam = ['apples','bananas','tofu','cats']
string = ''
for index,items in enumerate(spam):
    if index == len(spam)-1:
        string = string + 'and '+items
    else:
        string = string+items+', '
print(string)