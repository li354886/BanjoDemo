__author__ = 'lizhengning1'

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
import matplotlib.pyplot as plt

#Variables that contains the user credentials to access Twitter API
access_token = "2614679748-W5040iCR57Ph5MZFx1TGsT4mJCsUWzks0VFR8w5"
access_token_secret = "wCKCrx0kAcXJO1xfi8dOk7LBMnf26vAjcrm5owrguiTN5"
consumer_key = "E6doh89I7sl1FJW2kRBx0knte"
consumer_secret = "FhohecBHBpo2868LY4rt5u7AcBLEhYMRGTQQhyYsK05DYyCdrT"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])