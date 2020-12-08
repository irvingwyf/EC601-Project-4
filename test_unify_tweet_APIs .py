from unify_tweet_APIs import*
from os import path
from os import stat

def test_get_all_mentions_screen_names():
    ID = "@RobertDowneyJr"
    f = get_all_mentions_screen_names()
    assert path.exists("mention_screen_names.json")
    assert stat("mention_screen_names.json").st_size != 0

def test_get_most_recent_tweet():
    ID = "@RobertDowneyJr"
    Count = 10
    f = get_most_recent_tweet(ID, Count)
    assert path.exists("most_recent_tweets.txt")
    assert stat("mention_screen_names.json").st_size != 0

def test_get_all_retweet_screen_names():
    tweet_id = "1308813203619549184"
    Count = 7
    f = get_all_retweet_screen_names(tweet_id, Count)
    assert path.exists("retweet_screen_names.json")
    assert stat("retweet_screen_names.json").st_size != 0

def test_get_hashtag_search_tweets():
    Hashtag = "#Persona5"
    Count = 5
    Since = "2020-02-01"
    f = get_hashtag_search_tweets(Hashtag, Count, Since)
    assert path.exists("hashtag_tweets.json")
    assert stat("hashtag_tweets.json").st_size != 0

def test_get_search_tweets():
    Search = "COVID-19"
    search_type = "recent"
    Count = 8
    Until = "2020-12-01"
    f = get_search_tweets(Search, search_type, Count, Until)
    assert path.exists("search_result.json")
    assert stat("search_result.json").st_size != 0

def test_get_information_of_ID():
    ID = "@RobertDowneyJr"
    f = get_information_of_ID(ID)
    assert path.exists("user_info.json")
    assert stat("user_info.json").st_size != 0

def test_get_friend_of_ID():
    ID = "@RobertDowneyJr"
    Count = 30
    f = get_friend_of_ID(ID, Count)
    assert path.exists("friends_info.json")
    assert stat("friends_info.json").st_size != 0    

def test_get_follower_of_ID():
    ID =  "@RobertDowneyJr"
    Count = 100
    f = get_follower_of_ID(ID, Count)
    assert path.exists("followers_info.json")
    assert stat("followers_info.json").st_size != 0     

def test_get_trends_of_location():
    Boston_ID = 2367105
    Count = 6
    f = get_trends_of_location(Boston_ID, Count)
    assert path.exists("trends.json")
    assert stat("trends.json").st_size != 0 
