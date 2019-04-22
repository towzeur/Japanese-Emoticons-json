from bs4 import BeautifulSoup
import urllib.request as urllib2
import json

base = 'https://www.lennyfaces.net'

# scrap the front page to get the categories
soup = BeautifulSoup(urllib2.urlopen(base), "lxml")
categories_href = [c for c in soup.find_all('div', {'class': 'buttons is-centered'})[1]]

for c in categories_href:
    print(c['href'])

exit()
# scrap all the categories
OUTPUT = {}
for category_href in categories_href:
    category_name = category_href[4:-1]
    soup = BeautifulSoup(urllib2.urlopen(base + category_href), "lxml")
    emojies = [e.get_text()[3:-1] for e in soup.find('div', {'class': 'buttons is-centered'})]

    print(category_name, '\n' , emojies, '\n')
    print(emojies)
    OUTPUT[category_name] = emojies

with open('Japanese_Emoticons.json', 'w', encoding='utf-8') as f:
    json.dump(OUTPUT, f, indent=4, ensure_ascii=False)
