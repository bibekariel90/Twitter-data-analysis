# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 14:07:49 2021

@author: Asus
"""

from twython import TwythonStreamer
import csv

def process_tweet(tweet):
    d = {}
    d['hashtags'] = [hashtag['text'] for hashtag in tweet['entities']['hashtags']]
    d['date'] = tweet['created_at']
    d['text'] = tweet['text']
    d['user'] = tweet['user']['screen_name']
    d['followers'] = tweet['user']['followers_count']
    d['user_loc'] = tweet['user']['location']
    d['user_ver'] = tweet['user']['verified']
    d['device_source'] = tweet['source']
    return d


class MyStreamer(TwythonStreamer):
    
    def on_success(self, data):
        
        if data['lang'] == 'en':
            tweet_data = process_tweet(data)
            self.save_to_csv(tweet_data)
            
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()
        
    def save_to_csv(self, tweet):
        with open(r'tweets_saved4.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(list(tweet.values()))
            
import json
with open("twitter_credentials.json", "r")  as file:
    creds=json.load(file)
    
stream = MyStreamer(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'],
                    creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
stream.statuses.filter(track=['Arsenal']) 