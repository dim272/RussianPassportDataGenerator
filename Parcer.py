import requests
from bs4 import BeautifulSoup

html = requests.get('https:.......')
soup = BeautifulSoup(html.text, 'html.parser')

city = []

for i in soup.find_all("p"):
    if i.find("a") is None:
        pass
    else:
        city.append(i.find("a").get_text())

print(city)