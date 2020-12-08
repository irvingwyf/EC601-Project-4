#!/usr/bin/env python
# encoding: utf-8
#Author - Yifan Wang irvingw@bu.edu
import requests
import json
import os
import string
from google.cloud import language
from google.oauth2 import service_account
from google.cloud.language import enums
from google.cloud.language import types

# service_account_info = json.loads(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
# credentials = service_account.Credentials.from_service_account_info(service_account_info)                                
# client = language.LanguageServiceClient(credentials=credentials)
client = language.LanguageServiceClient.from_service_account_json('ec601-project-2-5172714cb435.json')

def extract_text(url, **data):
    timeout = data.get('timeout', 50)
    try:
        print("Performing the NLP of : {}".format(url))
        result = requests.get(url, timeout=timeout)
        text = result.text
        status = result.status_code
        if status == 200 and len(text) > 0:
            return text
        return None
    except Exception as e:
        print('Cannot extract text from url: {0}.'.format(url))
        return None

def sentiment(text):
    doc = language.types.Document(content=text,type=language.enums.Document.Type.PLAIN_TEXT)
    sent = client.analyze_sentiment(document=doc).document_sentiment
    print('Text     : {}'.format(text))
    print('Sentiment: {}, {}'.format(sent.score, sent.magnitude))
    return sent.score, sent.magnitude

def category(text):
    try:
        doc = language.types.Document(content=text,type=language.enums.Document.Type.PLAIN_TEXT)
        cats = client.classify_text(document=doc)
        for cat in cats.categories:
            print('Category name: {0}'.format(cat.name))
            print('Confidence   : {0}'.format(cat.confidence))
        return cats
    except Exception as e:
        print('Need at least 20 words to classify.')
        return None

def extract_words(text):
    doc = language.types.Document(content=text,type=language.enums.Document.Type.PLAIN_TEXT)
    result = client.analyze_entities(document=doc,encoding_type='UTF32')
    for entity in result.entities:
        print('name    : {0}'.format(entity.name))
        print('salience: {0}'.format(entity.salience))
    return result

def entity_sentiment(text):
    doc = language.types.Document(content=text,type='PLAIN_TEXT')
    result = client.analyze_entity_sentiment(document=doc,encoding_type='UTF32')
    for entity in result.entities:
        print('name     : {0}'.format(entity.name))
        print('salience : {0}'.format(entity.salience))
        print('magnitude: {0}'.format(entity.sentiment.magnitude))
        print('score    : {0}'.format(entity.sentiment.score))
    return result.entities

if __name__ == "__main__":
    # The text to analyze
    text1 = u'There will be 50 vaccination hubs in hospitals across England and dozens more across Wales and Scotland.'
    sentiment(text1)
    category(text1)
    entity_sentiment(text1)
    extract_words(text1)

    text2 = u'The logistical challenges of manufacturing and distributing tens of millions of vaccines mean the roll out will be gradual, with the most vulnerable people and health care workers first in line.'
    sentiment(text2)
    category(text2)
    entity_sentiment(text2)
    extract_words(text2)

    text3 = u'For now, it is available by invitation only for those age 80 and over, care homes staff and frontline health and social care workers.'
    sentiment(text3)
    category(text3)
    entity_sentiment(text3)
    extract_words(text3)

    url = "http://lite.cnn.com/en/article/h_75cddcd683e509affc334ff490efd8ff"
    extract_text(url)
    category("That actor on TV makes movies in Hollywood and also stars in a variety of popular new TV shows.")
