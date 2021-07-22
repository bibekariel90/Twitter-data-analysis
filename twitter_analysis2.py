# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 13:24:50 2021

@author: Asus
"""

from twython import Twython
import json

with open("twitter_credentials.json", "r") as file:
    creds=json.load(file)
    
python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

query={'q': 'European Super league',
        'result_type': 'mixed',
        'lang': 'en',
        'since': "2021-04-17"
        }

sample_return = python_tweets.search(**query)

import pandas as pd
#Creating a dictionary
dict_={'user': [], 'date': [], 'text': [], 'favorite_count': [], 'source':[], 'verified':[]}

for status in python_tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])
    dict_['source'].append(status['source'])
    dict_['verified'].append(status['user']['verified'])
    
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
df.to_csv('new_data.csv')
# from bs4 import BeautifulSoup
# df['source'] = df['source'].apply(lambda x: BeautifulSoup(x).get_text())
# devices = list(set(df[df['source'].str.startswith('Twitter')]['source']))
# df = df[df['source'].isin(devices)]
