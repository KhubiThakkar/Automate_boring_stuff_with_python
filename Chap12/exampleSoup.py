import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(),'html.parser')
# elems = exampleSoup.select('#author')
# print(type(elems))
# print(len(elems))
# print(type(elems[0]))
# print(str(elems[0]))
# print(elems[0].getText())
# print(elems[0].attrs)

# pElems = exampleSoup.select('p')
# print(str(pElems[0]))
# print(str(pElems[1]))
# print(str(pElems[0].getText()))
# print(str(pElems[1].getText()))
# print(str(pElems[2]))

spanElem = exampleSoup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistent_address')==None)
print(spanElem.attrs)