#!/usr/bin/env python
# encoding: utf-8
#Author - Yifan Wang irvingw@bu.edu

from tweets_nlp import *
from os import path
from os import stat

def test_analyze_tweets():
    ID = "@Twitter"
    Count = 1
    analyze_tweets(ID, Count)
    assert path.exists("tweet.txt")
    assert stat("tweet.txt").st_size != 0
    with open("tweet.txt", 'r') as tweet:
        lines = [i for i in tweet.readlines() if len(i)>1]
    assert len(lines) >= 1

