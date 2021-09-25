import lxml
import requests
from lxml import html

url_artist = 'https://ra.co/dj/vril'
url_artist_events = '{}/tour-dates'.format(url_artist)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

response = requests.get(url_artist_events, headers=headers)
tree = lxml.html.fromstring(response.text)

path = '/html/body/div/section[1]/div/div/div/section/div/ul/li[1]/div[1]/div[3]/ul/li[2]/div/h3/a/span'
blah = tree.xpath(path)
