from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

raw_html = urlopen("https://www.fortuneconferences.com/the-ceo-initiative-2018/2018-members-and-speakers/", timeout = 5)
html = BeautifulSoup(raw_html, "lxml")
file = open('out.csv', 'w')

for box in html.find_all('dl'):
    txt = box.find('dd')
    title = txt.find('i').get_text()
    file.write(box.find('dt').get_text().replace(",", " -") + ",")
    file.write(re.search(r'\S(\S*\s?)*\S', txt.get_text().replace(title, "")).group(0).replace(",", "") + ",")
    file.write(title.replace(",", " -") + ",\n")
    