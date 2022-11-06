import requests
from bs4 import BeautifulSoup

for i in range(100):
    r = requests.get(url='http://mercury.picoctf.net:29649/check', cookies={'name': str(i)})
    soup = BeautifulSoup(r.text, 'html.parser')
    for p in soup.find_all('p'):
        print(p.text)
