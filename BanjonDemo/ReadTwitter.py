__author__ = 'lizhengning1'

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import datetime
import sys
import getopt
import socket
import requests
import csv
from flask import Flask, jsonify
from pymongo import MongoClient






app = Flask(__name__)


#Variables that contains the user credentials to access Twitter API
access_token = "2614679748-W5040iCR57Ph5MZFx1TGsT4mJCsUWzks0VFR8w5"
access_token_secret = "wCKCrx0kAcXJO1xfi8dOk7LBMnf26vAjcrm5owrguiTN5"
consumer_key = "E6doh89I7sl1FJW2kRBx0knte"
consumer_secret = "FhohecBHBpo2868LY4rt5u7AcBLEhYMRGTQQhyYsK05DYyCdrT"


#This is a basic listener that just prints received tweets to stdout.
@app.route('/', methods=['GET'])

class StdOutListener(StreamListener):
    def on_data(self, data):
        # app.run(host='0.0.0.0')
        # response = json.loads(data)
        # create an INET, STREAMing socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # now connect to the web server on port 80 - the normal http port
        host = socket.gethostbyname("127.0.0.1")
        s.connect(("127.0.0.1", 9999))
        s.send(data)
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
    stream.filter(locations=[-122.75,36.8,-121.75,37.8])



