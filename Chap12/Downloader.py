#! python3
#Downloader.py - Downloads every image on Flickr matching your search input

import requests,os,sys,bs4

if len(sys.argv)<2:
    print('incorrect input')
else:
    searchWord = sys.argv[1]
    print('Going to Flickr...')
    url = 'https://www.flickr.com/search/?text='+searchWord  #starting url
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text,'html.parser')
    image_elem = soup.select('')