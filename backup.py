#test with the main account
import requests
from bs4 import BeautifulSoup
import tweepy as tp
import os
import urllib
import urllib.request
import re

my_url = "https://capturing-the-light.tumblr.com/"

def make_soup(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    return soup

soup = make_soup(my_url)
i = 1

for img in soup.findAll('img'):
    temp = (img.get('src'))
    if temp[:1] == "/":
        image = "https://capturing-the-light.tumblr.com/" + temp
    else:
        image = temp

    nameTemp = img.get('alt')
    filename = str(i)
    i = i + 1
    if len(nameTemp) == 0:
        filename = str(i)
        i = i + 1
    else:
        filename = nameTemp
    print(image)


    imagefile = open(filename + ".jpeg",'wb')
    imagefile.write(urllib.request.urlopen(image).read())
    imagefile.close()

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
x = 1
def tweet_image(url, message):
    filename = str(x) + ".jpeg"
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")

temp = "test"
tweet_image(my_url, temp)

"""def tweet_image(url, message):
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")
"""
"""message = "TEMP"

images = []
images = soup.find_all('img', {'src':re.compile('.jpg')})
for image in images:
    print(image['src'] + '\n')
#tweet_image(url, message)"""