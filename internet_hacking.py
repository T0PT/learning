import requests
from bs4 import BeautifulSoup as bs
r = requests.get('https://yandex.ru/pogoda/moscow?lat=55.753215&lon=37.622504Yandex-API-Key:')
print(r.text)
sp=bs(r.text,'html.parser')
print(str(sp.find('span',{'class':'temp__value temp__value_with-unit'})))