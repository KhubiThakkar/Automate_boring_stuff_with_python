#! python3
#searchpypi.py -Opens several search results

import requests,sys,webbrowser,bs4
print('Searching...')
res = requests.get('https://pypi.org/search/?q='+ ' '.join(sys.argv[1:]))

res.raise_for_status()
soup =bs4.BeautifulSoup(res.text,'html.parser')
#open browser tab for each result
linkelems = soup.select('.package-snippet')
print(len(linkelems))
numOpen = min(5,len(linkelems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org'+linkelems[i].get('href')
    print('Opening',urlToOpen)
    webbrowser.open(urlToOpen)