from bs4 import BeautifulSoup
import urllib.request as urllib2
from urllib.request import Request
import json

base = 'https://www.jemoticons.com'
lang = '/en'

# scrap the front page to get the categories
req = Request(
    url=base+lang,
    headers={'User-Agent': 'Mozilla/5.0'}
)

soup = BeautifulSoup(urllib2.urlopen(req), "lxml")
categories_href = [c['href'] for c in soup.find('div', {'class': 'buttons is-centered mb-2'})]
print(len(categories_href))

# scrap all the categories

OUTPUT = {}
for category_href in categories_href:
    reqWith = Request(
    url=base+category_href,
    headers={'User-Agent': 'Mozilla/5.0'}
    )
    category_name = category_href[4:-1]
    soup = BeautifulSoup(urllib2.urlopen(reqWith), "lxml")
    emojies = [e.get_text()[3:-1] for e in soup.find('div', {'class': 'buttons is-centered'})]

    print(category_name, '\n' , emojies, '\n')
    print(emojies)
    OUTPUT[category_name] = emojies

with open('Japanese_Emoticons.json', 'w', encoding='utf-8') as f:
    json.dump(OUTPUT, f, indent=4, ensure_ascii=False)