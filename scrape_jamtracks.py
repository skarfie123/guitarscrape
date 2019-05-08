#Imports
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, urlretrieve
import http, time, random, urllib, os

#Open main page
p=urlopen("https://www.guitarbackingtrack.com/bts/Jamtracks.htm")
print("got p")
#Read main page
try:
    soup = bs(p, "html.parser")
except (http.client.IncompleteRead) as e:
    print("incomplete")
    exit()

#Get links to each track
links=[]
for link in soup.find_all('a'):
    h = link.get('href')
    if h[:6] == "/play/" :
        links.append(h)

#Iterate through each link
for link in links:
    #Skip if already downloaded
    if os.path.isfile(str(link)[16:-4]+".mp3"):
        continue
    #Open track page
    try:
        p2=urlopen("https://www.guitarbackingtrack.com"+link)
    except (urllib.error.HTTPError) as e:
        continue
    #Read track page
    try:
        soup2 = bs(p2, "html.parser")
    except (http.client.IncompleteRead) as e:
        print("incomplete")
        continue

    #Get links to each audiofile (should just be one)
    links2=[]
    for link2 in soup2.find_all('audio'):
        links2.append(link2.get('src'))
    #Download the audio file
    urlretrieve("https://www.guitarbackingtrack.com"+links2[0], str(link)[16:-4]+".mp3")
    #Delay to not overload the website
    time.sleep(0.5+0.1*random.random())
