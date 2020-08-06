import re
import requests
from bs4 import BeautifulSoup
import tweepy as tp

site = 'https://capturing-the-light.tumblr.com/tagged/frederic-bazille'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]

def twitterAPI():
    consumer_key = 'h6qdP9AktNsUXa5VhoAEz55xj'
    consumer_secret = '9gtC2lHDCQ9w3uinsJLK3VynvEVWaDreah4cTF1nRXAMV37dQE'
    access_token = '1231702850071228416-7f7ZO3FF0Yt4lm9CE5OwPaH7CSmwPS'
    access_secret = 'TjC6BvR7vjwwHqfHNSZoo7w4PG4PkpNkzrp8cntNep13C'

    auth = tp.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tp.API(auth)
    return api
api = twitterAPI()


for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    if not filename:
         print("Regex didn't match with the url: {}".format(url))
         continue
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative
            # if it is provide the base url which also happens
            # to be the site variable atm.
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)

    print(url)