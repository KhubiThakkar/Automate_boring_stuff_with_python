#! python3
#NOT WORKING -- as the link is not loading even directly in browser
# downloadXkcd.py - Downloads every single XKCD comic
import os, requests, bs4
url = 'https://xkdc.com'
os.makedirs('xkdc',exist_ok=True)
while not url.endswith('/1/'):
    #download the page
    print(url)
    print('Downloading page %s...'%url)
    res = requests.get(url)
    res.raise_for_status()
    #find the url of the comic image
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image...')
    else:
        comicURL = 'https:'+comicElem[0].get('src')
        #download the image
        print('Downloading image %s...'%comicURL)
        res = requests.get(comicURL)
        res.raise_for_status()
        #save image to ./xdkc
        imageFIle = open(os.path.join('xkdc',os.path.basename(comicURL)),'wb')
        for chunk in res.iter_content(100000):
            imageFIle.write(chunk)
        imageFIle.close()
    #get the prev link
    prevLink =soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com'+prevLink.get('href')

print('Done.')