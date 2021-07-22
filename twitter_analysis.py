# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 13:18:07 2021

@author: Asus
"""

import json

credentials={}
credentials['CONSUMER_KEY']='qtoKUlNz8yU0drOoX1FaPoms8'
credentials['CONSUMER_SECRET']='wi7zVjPGddgxyUd19JEtUGIEOc9YpxdBpinf6exhZZzp2qlIsy'
credentials['ACCESS_TOKEN']='421092961-cJeov54kUYyKfgCHX1oQ4pAJVVmbLa0YELj0q7X7'
credentials['ACCESS_SECRET']='KAQ3R8wurs3rrr7VlGPqVMw42uJy1ZN0uAorJaTytLh9t'

with open("twitter_credentials.json", "w") as file:
    json.dump(credentials, file)
    
