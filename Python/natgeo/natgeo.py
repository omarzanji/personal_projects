# Scrapes NatGeo pic of the day and puts in folder.

# Author: Omar Barazanji
# Date: 8/20/20

import requests
import urllib
from bs4 import BeautifulSoup

url = 'https://www.nationalgeographic.com/photography/photo-of-the-day/2018/08/france-carmague-horses/'

# Fetch content
page = requests.get(url)

# Extracting HTML code
soup = BeautifulSoup(page.text, 'lxml')

image_loc = soup.findAll('div', {'class' : 'parsys iparsys content'})

image_json = str(image_loc[0])

index = 0
for x in image_json:
    if 'endpoint' in image_json[index : index+8]:
        img_json = image_json[index+11:]
        break
    index += 1

index = 0
for x in img_json:
    if x == ',':
        json_link = img_json[:index-1]
        break
    index += 1

# Fetch json content
page2 = requests.get(json_link)

json_data = page2.json()

for x in json_data['items']:
    urllib.urlretrieve(x['originalUrl'], 'DailyPhoto.jpg')
    break

