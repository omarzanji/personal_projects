# This program will scrape the fuck out of RS database.
#
# Author: Omar Barazanji
# Python Version: 3.6

import urllib.request as req
import json
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs


def grab_item_id(item_name):
    with open('obj_num.json') as f:
        objects = json.load(f)

    item_id = ""
    for x in objects:
        if x['name'] == item_name:
            item_id = (x['id'])

    return item_id


def item_prices_to_array(item_url):

    # Opening up connection and grabbing the page
    client = req.urlopen(item_url)

    # Loads the content into a variable
    raw_html = client.read()

    # Closes the content
    client.close()

    # HTML parsing
    soup_html = bs(raw_html, 'html.parser')

    graph_data = str(soup_html.body.script)
    graph_data_list = graph_data.split('\t')

    key = 'average180.push'

    six_month_data = []
    for val in graph_data_list:
        if key in val:
            six_month_data.append(val)

    item_array = []
    for x in six_month_data:
        date = x[27:37]
        price = ''
        comma_count = 0
        for char in x:
            if char == ',':
                comma_count += 1
                continue
            if comma_count == 1:
                price += char
            if comma_count == 2:
                break
        item_array.append((date, price[1:]))

    return item_array


if __name__ == '__main__':

    name = input(str("Type item name here: "))
    number = grab_item_id(name)

    item_page = 'http://services.runescape.com/m=itemdb_oldschool/%s/viewitem?obj=%s' % (name, number)

    item_prices = item_prices_to_array(item_page)

    y_axis = []
    for y in item_prices:
        y_axis.append(int(y[1]))

    x_axis = []
    for x in item_prices:
        x_axis.append(x[0])

print(x_axis)
print(y_axis)

plt.plot(y_axis)
plt.show()
