import requests
r = requests.get('https://suumo.jp/jj/bukken/ichiran/JJ010FJ001/?ar=040&bs=020&ta=17&jspIdFlg=patternShikugun&sc=17201&kb=1&kt=9999999&km=1&tb=0&tt=9999999&hb=0&ht=9999999&ekTjCd=&ekTjNm=&tj=0&kw=1')

print(r.headers)
print('---------------')

        
