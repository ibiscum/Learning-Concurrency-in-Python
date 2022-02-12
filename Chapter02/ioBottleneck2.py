import urllib.request
import time
from bs4 import BeautifulSoup

linkArray = []


def get_links():
    t0 = time.time()
    req = urllib.request.urlopen('http://www.example.com')
    soup = BeautifulSoup(req.read(), features="html.parser")
    for link in soup.findAll('a'):
        linkArray.append(link.get('href'))
        print(len(linkArray))
    t1 = time.time()
    print("Total Time To Fetch Page: {} Seconds".format(t1 - t0))


get_links()
