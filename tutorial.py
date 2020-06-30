import requests
from bs4 import BeautifulSoup as bs
import tweepy as tp
import time
import os

#Source: https://www.youtube.com/watch?v=MN_1wOxIfRU


def twitterAPI():
    consumer_key = os.environ.get('CONSUMER_KEY')
    consumer_secret = os.environ.get('CONSUMER_SECRET')
    access_token = os.environ.get('ACCESS_TOKEN')
    access_secret = os.environ.get('ACCESS_SECRET')

    auth = tp.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tp.API(auth)
    return api

api = twitterAPI()
url = "https://www.tumblr.com/search/impressionism"
page = requests.get(url)
soup = bs(page.text, 'html.parser')

#get by tag
image_tags = soup.find_all('img')


#Global int
"""count = 3
maxI = 39"""

"""def get_images():
    for image in image_tags:
        try:
            url = image['src']
            source = requests.get(url)
            if source.status_code == 200:
                #Rename the file
                with open('art-' + str(x) + '.jpg', 'wb') as f:
                    f.write(requests.get(url).content)
                    print("Getting " + str(x))
                    f.close()
                    x += 1
        except:
            pass
"""
def make_tweet():
    count = 0
    maxI = 39
    for image in image_tags:
        file_name = "art-" + str(count) + ".jpg"
        print("Tweeting: " + file_name)
        api.update_with_media(file_name, "test")
        time.sleep(600)
        count += 1
        if count == maxI:
            pass

"""file_name = "art-" + str(1) + ".jpg"
api.update_with_media(file_name, "test")"""

make_tweet()