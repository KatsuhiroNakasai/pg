import time
import requests
from bs4 import BeautifulSoup
url = 'https://suumo.jp/jj/bukken/ichiran/JJ010FJ001/?ar=040&bs=020&ta=17&jspIdFlg=patternShikugun&sc=17201&kb=1&kt=9999999&km=1&tb=0&tt=9999999&hb=0&ht=9999999&ekTjCd=&ekTjNm=&tj=0&kw=1'
r = requests.get(url)
#html = 'https://news.yahoo.co.jp'
soup =BeautifulSoup(r.content, "html.parser")

#print(soup.find('ul', 'newsFeed_list').text)
#print(soup.find_all('li'))
ret = soup.find_all('span', {'class':'dottable-value'})

#ret = soup.find_all('span')
for i in range(5):
    print(ret[i].text)
    time.sleep(2)

#print(ret)
"""
print(ret[0])
print(ret[1])
print(ret[2])
print(ret[3])
print(ret[4])

for newslist in soup.find('li'):
    sleep(3)
    print(newslist)
"""
