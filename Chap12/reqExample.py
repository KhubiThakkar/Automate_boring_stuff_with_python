import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoandJuliet.txt','wb')
for chunks in res.iter_content(100000):
    playFile.write(chunks)
playFile.close()