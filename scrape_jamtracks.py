from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, urlretrieve
import http, time, random, urllib, os
p=urlopen("https://www.guitarbackingtrack.com/bts/Jamtracks.htm")
print("got p")
try:
    soup = bs(p, "html.parser")
except (http.client.IncompleteRead) as e:
    print("incomplete")
    exit()

links=[]
for link in soup.find_all('a'):
    h = link.get('href')
    if h[:6] == "/play/" :
        links.append(h)
#print(links)

for link in links:
    if os.path.isfile(str(link)[16:-4]+".mp3"):
        continue
    try:
        p2=urlopen("https://www.guitarbackingtrack.com"+link)
    except (urllib.error.HTTPError) as e:
        continue
    try:
        soup2 = bs(p2, "html.parser")
    except (http.client.IncompleteRead) as e:
        print("incomplete")
        continue

    links2=[]
    for link2 in soup2.find_all('audio'):
        links2.append(link2.get('src'))
    urlretrieve("https://www.guitarbackingtrack.com"+links2[0], str(link)[16:-4]+".mp3")
    time.sleep(0.5+0.1*random.random())
