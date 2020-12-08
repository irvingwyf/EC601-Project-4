# https://cloud.google.com/natural-language/docs/reference/libraries#windows
# $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\username\Downloads\my-key.json"
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Return the overall sentiment of the text
def analyze_overall_sentiment(client,text):
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    print('Text: {}'.format(text))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
    return sentiment.score, sentiment.magnitude

# Find keywords with high salience in the text.
def extract_keywords(client,text):
    # https://googleapis.dev/python/language/latest/usage.html
    document = language.types.Document(
         content=text,
         type=language.enums.Document.Type.PLAIN_TEXT,
    )
    response = client.analyze_entities(
        document=document,
        encoding_type='UTF32',
    )
    for entity in response.entities:
        print('=' * 20)
        print('         name: {0}'.format(entity.name))
        print('     salience: {0}'.format(entity.salience))
    print('=' * 20)
    
    return response

def analyze_entity_sentiment(client,text):
    document = language.types.Document(
        content=text,
        type='PLAIN_TEXT',
    )
    response = client.analyze_entity_sentiment(
        document=document,
        encoding_type='UTF32',
    )
    entities = response.entities
    for entity in entities:
        print('=' * 20)
        print('         name: {0}'.format(entity.name))
        print('     salience: {0}'.format(entity.salience))
        print('    magnitude: {0}'.format(entity.sentiment.magnitude))
        print('        score: {0}'.format(entity.sentiment.score))
    print('=' * 20)

    return entities

if __name__ == "__main__":
    
    # Instantiates a client
    client = language.LanguageServiceClient()

    # The text to analyze
    text = u'The chicken laid an egg. The geese swim in the lake.'
    analyze_overall_sentiment(client, text)
    analyze_entity_sentiment(client,text)
    print()

    text = u'I hate that dog. He pees all over the house.'
    analyze_overall_sentiment(client,text)
    analyze_entity_sentiment(client,text)
    print()

    text = u'My birthday is tomorrow, I am so excited !!!!!'
    analyze_overall_sentiment(client,text)
    analyze_entity_sentiment(client,text)
    print()
