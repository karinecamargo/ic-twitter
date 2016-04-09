from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from pymongo import MongoClient
import time
client = MongoClient('localhost', 27017)
db = client.feminismo

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        try:   
            tweet = json.loads(data)
            if(tweet['lang'] == 'pt'):
                db.tweets.update({'id': tweet['id']}, tweet, upsert=True)
        except:
            print ('Perdeu-se um tweet')

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    while(True):
        try:
            consumer_key="EFjOORgYUpfWArdrcVM0tQQF2"
            consumer_secret="onKASVgnoH47kGkzmxxPZSyKrUGkk4wxV9Xtn4a556h7BswKs8"
            access_token="2162977602-err5eNtwLqxeljQtMbOBJjXgKlE4EO1Cy78eBcf"
            access_token_secret="cH8HGKLfJRjJ7QB3wTteg7xICqyTJQ9LApGNWDD0RpyNZ"
            l = StdOutListener()
            auth = OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)

            stream = Stream(auth, l)
            stream.filter(track=['feminismo','feminista','machista','machismo'])
        except:
            print ("Deu merda!!!!!!!!!!!!!!!!!!")
            print (time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))
