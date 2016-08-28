#!/usr/bin/env python3

"""
Druckspatz listens to on or more strings via twitter's streaming api. Once the
string occurs the tweet gets printed via the standard printer on a unix system.
"""

# sys to access command line arguments
import sys
# Import the necessary methods from tweepy library to acces twitter's api
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
# JSON to handle the json response
import json
# DateTime to correctly format the date
import datetime
from datetime import date
# Jinja2 to render the html template
import jinja2
# PDFKit to convert html to pdf
import pdfkit
# Subprocess to execute the lpr command to print the pdf
import subprocess
# Import credentials for twitter api
import twitter_cfg as cfg


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def __init__(self):
        self.templateLoader = jinja2.FileSystemLoader(searchpath="tweet")
        self.templateEnv = jinja2.Environment(loader=self.templateLoader)
        self.template = self.templateEnv.get_template("tweet.tpl")

        self.pdf_options = {
            'page-width': '55mm',
            'margin-top': '5mm',
            'margin-right': '1mm',
            'margin-bottom': '1mm',
            'margin-left': '5mm',
        }

    def on_data(self, data):
        tweet = json.loads(data)
        tweet_time = datetime.date.fromtimestamp(int(tweet["timestamp_ms"])//1000)
        templateVars = {
            'avatar' : tweet['user']['profile_image_url_https'],
            'name' : tweet["user"]["name"],
            'screen_name' : "@" + tweet["user"]["screen_name"],
            'date' : date.strftime(tweet_time, "%b %d"), 
            'tweet' : tweet["text"]
        }
        self.render_html(templateVars)
        self.convert_html_2_pdf()
        self.print_pdf()
        return True

    def on_error(self, status):
        print(status)
    
    def render_html(self, templateVars):
        html_file = open('tweet/tweet.html', 'w')
        html = self.template.render(templateVars)
        html_file.write(html)
    
    def convert_html_2_pdf(self):
        pdfkit.from_file('tweet/tweet.html', \
        	'/home/pi/druckspatz/tweet/tweet.pdf', options=self.pdf_options)
    
    def print_pdf(self):
        subprocess.run(["/usr/bin/lpr", "tweet/tweet.pdf"])


if __name__ == '__main__':

    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(cfg.consumer_key, cfg.consumer_secret)
    auth.set_access_token(cfg.access_token, cfg.access_token_secret)
    stream = Stream(auth, l)
    
    # Remove first element from argv list
    args = sys.argv
    args.pop(0)
    
    # If no search tearm is given just exit
    if len(args) == 0:
        print("Search parameters are missing.\nUsage: python3 druckspatz.py '#tag' <<searchTerm> ...>.\nTerms starting with '#' have to be escaped by '.")
        sys.exit()

    # This line filters Twitter Streams to capture data by the keywords: '#nochNtest'
    # 
    # In the JSON-Response one can access
    # the text via 'text',
    # the user name via 'user' -> 'screen_name'
    # the users name via 'user' -> 'name'
    # the profile image via 'user' -> profile_image_url(_https)
    # the timestamp via 'timestamp_ms' (comes as a string)
    stream.filter(track=args)
