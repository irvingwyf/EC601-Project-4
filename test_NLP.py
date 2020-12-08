#!/usr/bin/env python
# encoding: utf-8
#Author - Yifan Wang irvingw@bu.edu

from NLP import *
import os
import json

def test_extract_text():
    url = "http://lite.cnn.com/en/article/h_75cddcd683e509affc334ff490efd8ff"
    text = extract_text(url)
    assert text != ""

def test_sentiment():
    Love = "I Love You My Darling!!!"
    Hate = "Worst challenge!"
    Lscore, Lmagnitude = sentiment(Love)
    Hscore, Hmagnitude = sentiment(Hate)
    assert Lscore > 0
    assert Lmagnitude > 0
    assert Hscore < 0
    assert Hmagnitude > 0

def test_category():
    text = "That actor on TV makes movies in Hollywood and also stars in a variety of popular new TV shows."
    result = category(text)
    for res in result.categories:
        assert res.name == "/Arts & Entertainment/TV & Video/TV Shows & Programs"

def test_extract_words():
    text = "Billionaire industrialist and genius inventor Tony Stark is kidnapped and forced to build a devastating weapon."
    result = extract_words(text)
    for entity in result.entities:
        assert entity.name in text
        assert entity.salience <= 1
        assert entity.salience >= 0

def test_entity_sentiment():
    text = "Google, headquartered in Mountain View (1600 Amphitheatre Pkwy, Mountain View, CA 940430), unveiled the new Android phone for $799 at the Consumer Electronic Show."
    result = entity_sentiment(text)
    for entity in result:
        assert entity.name in text
        assert entity.salience <= 1
        assert entity.salience >= 0
        assert abs(entity.sentiment.magnitude) <= 0.25
        assert abs(entity.sentiment.score) <= 0.25
