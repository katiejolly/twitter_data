import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

access_token = '2832470440-hGpjl5nd1JRmJcSAt8XVZ0wM735UYyzUQ9ore4g'
access_secret = 'aMl9TlQMe8WqPK333augBnWB1vXBBcq66lOBbeXYSoKTT'
consumer_key = 'uYp7m5Yzx48FJyxQvmQWZIKDm'
consumer_secret = 'k26M1TwaFjsF9YmzmcqUKIXinIjtsz6hFju8IDNMLbKU12WqMA'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('brexit.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data")
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track = ['#Brexit, #Article50, #brexit, #TheresaMay, #BrexitDay'])
