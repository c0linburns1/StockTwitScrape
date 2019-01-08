#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 13:34:21 2019

@author: colinburns
"""
import re
import selenium
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import Counter

#specific location of your chromedriver executable
path = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(path)
tickers = []
driver.get('https://stocktwits.com/stream/trending')
trendingTweets = driver.find_elements_by_css_selector('.MessageStreamView__body___2giLh')
for tweet in trendingTweets:
    data = tweet.text
    #the reg expression below tries to find any words starting with $
    patt = re.search(r'[$]\w\w?\w?\w?', data)
    if patt:
        goodSymbol = str(patt.group())
        #now we have the tickers, but they have $ attached ($SQ)
        better = goodSymbol.replace("$","")
        tickers.append(better)
        
        
    else:
        print'no symbol found for this Twit'
    


uniqueSym = Counter(tickers).keys()
frequency = Counter(tickers).values()
frequentTick = frequency.index(max(frequency))
popular = str(max(frequency))
print str(uniqueSym[frequentTick]), 'was mentioned', popular, 'times'


popularStock = uniqueSym[frequentTick]




driver.close()
