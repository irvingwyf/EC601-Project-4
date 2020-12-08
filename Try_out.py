from GoogleNlpAPI import *
import os
from google.oauth2 import service_account
import json

#Use github secret passed as environment var
service_account_info = json.loads(os.environ['GOOGLE_SECRET'])
credentials = service_account.Credentials.from_service_account_info(service_account_info)                                
client = language.LanguageServiceClient(credentials=credentials)

def test_analyze_overall_sentiment_positive():
    text = "Happy Birthday!"
    score, magnitude = analyze_overall_sentiment(client,text)
    # assert positive sentiment
    assert score > 0
    assert magnitude > 0

def test_analyze_overall_sentiment_negative():
    text = "Bad dog!"
    score, magnitude = analyze_overall_sentiment(client,text)
    # assert negative sentiment
    assert score < 0
    assert magnitude > 0

def test_extract_keywords():
    text = "Happy Birthday!"
    res = extract_keywords(client, text)
    for entity in res.entities:
        assert entity.name in text
        assert entity.salience <= 1
        assert entity.salience >= 0

def assert_close_to_zero_sentiment(score):
    assert abs(score) <= 0.25
    
def test_analyze_entity_sentiment_neutral():
    text = '''
Several key states, including Arizona, Georgia and Michigan,
are expected to project a winner at some point on Wednesday or Thursday.
With results from these critical states - plus the others who projected winners late on Tuesday
- we should have a clearer picture of the likely outcome.'''
    entities = analyze_entity_sentiment(client, text)
    for entity in entities:
        assert entity.name in text
        assert entity.salience <= 1
        assert entity.salience >= 0
        assert_close_to_zero_sentiment(entity.sentiment.magnitude)
        assert_close_to_zero_sentiment(entity.sentiment.score)

# Negative tests
def test_empty_string():
    entities = analyze_entity_sentiment(client, "")
    score, magnitude = analyze_overall_sentiment(client,"")
    res = extract_keywords(client, "")

def test_bad_words():
    text = 'gibberishgiberish savd sv ds vb ds b ds b'
    entities = analyze_entity_sentiment(client, text)
    score, magnitude = analyze_overall_sentiment(client,text)
    res = extract_keywords(client, text)
