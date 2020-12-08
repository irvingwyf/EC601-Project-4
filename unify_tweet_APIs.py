#!/usr/bin/env python
# encoding: utf-8
#Author - Yifan Wang irvingw@bu.edu

import tweepy #https://github.com/tweepy/tweepy
import json
import csv
import os 
import io
import sys

#Twitter API credentials
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_key = os.getenv('access_key')
access_secret = os.getenv('access_secret')

#authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def get_all_mentions_screen_names():
    # fetching the statuses
    mentions_list = api.mentions_timeline()
    file = open('mention_screen_names.json', 'w') 
    print("Writing tweet objects to JSON please wait...")
    if not mentions_list:
        file.write('No mentioned history.\n')
    else:
        for mention in mentions_list: 
            json.dump(mention.user.screen_name,file,sort_keys = True,indent = 4)
            file.write('\n')
    #close the file
    print("Done")
    file.close()

def get_most_recent_tweet(ID, Count):
    #initialize a list to hold all the tweepy Tweets
    alltweets = []
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = ID, count=Count)
    #save most recent tweets
    alltweets.extend(new_tweets)
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 15
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = ID,count=Count,max_id=oldest)    
        #save most recent tweets
        alltweets.extend(new_tweets)
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 1):
            break
        print("...%s tweets downloaded so far" % (len(alltweets)))    
    #write tweet objects to JSON
    file = open('most_recent_tweets.txt', 'a+') 
    print("Writing tweet objects to TXT please wait...")
    for status in alltweets:
        json.dump(status.text,file,sort_keys = True,indent = 4)
        file.write("\n")
    #close the file
    print("Done fetching recent ",Count," tweets of ",ID)
    file.close()

def get_all_retweet_screen_names(ID, Count):
    # fetching the statuses 
    retweets_list = api.retweets(ID,count=Count) 
    file = open('retweet_screen_names.json', 'w') 
    print("Writing tweet objects to JSON please wait...")
    for retweet in retweets_list: 
        json.dump(retweet.user.screen_name,file,sort_keys = True,indent = 4)
        file.write('\n')
    #close the file
    print("Done")
    file.close()

def get_hashtag_search_tweets(Hashtag,Count,Time):
    hashtag_list = api.search(q=Hashtag,count = Count, since = Time)
    file = open('hashtag_tweets.json', 'w') 
    print("Writing tweet objects to JSON please wait...")
    for hashtag in hashtag_list: 
        json.dump(hashtag.text,file,sort_keys = True,indent = 4)
        file.write(" by: ")
        json.dump(hashtag.user.screen_name,file,sort_keys = True,indent = 4)
        file.write('\n')
    #close the file
    print("Done")
    file.close()

def get_search_tweets(Content,search_for,Count,Time):
    search_list = api.search(q=Content,result_type = search_for,count = Count, until = Time)
    file = open('search_result.json', 'w') 
    print("Writing tweet objects to JSON please wait...")
    for search in search_list: 
        json.dump(search.text,file,sort_keys = True,indent = 4)
        file.write('\n')
    #close the file
    print("Done")
    file.close()

def get_information_of_ID(ID):
    info = api.get_user(ID)
    file = open("user_info.json", 'w')
    print("Writing user information to JSON please wait...")
    file.write("The id is : " + str(info.id)) 
    file.write("\nThe id_str is : " + info.id_str) 
    file.write("\nThe name is : " + info.name) 
    file.write("\nThe screen_name is : " + info.screen_name) 
    file.write("\nThe location is : " + str(info.location)) 
    file.write("\nThe profile_location is : " + str(info.profile_location)) 
    file.write("\nThe description is : " + info.description) 
    file.write("\nThe url is : " + str(info.url)) 
    file.write("\nThe entities are : " + str(info.entities)) 
    file.write("\nIs the account protected? : " + str(info.protected)) 
    file.write("\nThe followers_count is : " + str(info.followers_count)) 
    file.write("\nThe friends_count is : " + str(info.friends_count)) 
    file.write("\nThe listed_count is : " + str(info.listed_count)) 
    file.write("\nThe account was created on : " + str(info.created_at)) 
    file.write("\nThe favourites_count is : " + str(info.favourites_count)) 
    file.write("\nThe utc_offset is : " + str(info.utc_offset)) 
    file.write("\nThe geo_enabled is : " + str(info.geo_enabled)) 
    file.write("\nThe verified is : " + str(info.verified)) 
    file.write("\nThe statuses_count is : " + str(info.statuses_count)) 
    file.write("\nThe lang is : " + str(info.lang)) 
    file.write("\nThe status ID is : " + str(info.status.id)) 
    file.write("\nThe contributors_enabled is : " + str(info.contributors_enabled)) 
    file.write("\nThe is_translator is : " + str(info.is_translator)) 
    file.write("\nThe is_translation_enabled is : " + str(info.is_translation_enabled)) 
    file.write("\nThe profile_background_color is : " + str(info.profile_background_color)) 
    file.write("\nThe profile_background_image_url is : " + str(info.profile_background_image_url)) 
    file.write("\nThe profile_background_image_url_https is : " + str(info.profile_background_image_url_https)) 
    file.write("\nThe profile_background_tile is : " + str(info.profile_background_tile)) 
    file.write("\nThe profile_image_url is : " + str(info.profile_image_url)) 
    file.write("\nThe profile_image_url_https is : " + str(info.profile_image_url_https)) 
    file.write("\nThe profile_banner_url is : " + str(info.profile_banner_url)) 
    file.write("\nThe profile_link_color is : " + str(info.profile_link_color)) 
    file.write("\nThe profile_sidebar_border_color is : " + str(info.profile_sidebar_border_color)) 
    file.write("\nThe profile_sidebar_fill_color is : " + str(info.profile_sidebar_fill_color)) 
    file.write("\nThe profile_text_color is : " + str(info.profile_text_color)) 
    file.write("\nThe profile_use_background_image is : " + str(info.profile_use_background_image)) 
    file.write("\nThe has_extended_profile is : " + str(info.has_extended_profile)) 
    file.write("\nThe default_profile is : " + str(info.default_profile)) 
    file.write("\nThe default_profile_image is : " + str(info.default_profile_image)) 
    file.write("\nIs the authenticated user following the account? : " + str(info.following)) 
    file.write("\nHas the authenticated user requested to follow the account? : " + str(info.follow_request_sent)) 
    file.write("\nAre notifications of the authenticated user turned on for the account? : " + str(info.notifications)) 
    print("Done")
    file.close()

def get_friend_of_ID(ID, Count):
    friends_list = api.friends(ID, count=Count)
    file = open("friends_info.json", 'w')
    print("Writing friends information to JSON please wait...")
    for friend in friends_list: 
        json.dump(friend.name,file,sort_keys = True,indent = 4)
        file.write('\n')
    #close the file
    print("Done")
    file.close()

def get_follower_of_ID(ID, Count):
    followers_list = api.followers(ID, count=Count)
    file = open("followers_info.json", 'w')
    print("Writing followers information to JSON please wait...")
    for follower in followers_list: 
        json.dump(follower.name,file,sort_keys = True,indent = 4)
        file.write('\n')
    #close the file
    print("Done")
    file.close()

def get_trends_of_location(ID, Count):
    '''ID is the WOEID find from https://www.findmecity.com/'''
    trends = api.trends_place(ID)
    file = open("trends.json", 'w')
    print("Writing trends to JSON please wait...")
    trend_names = trends[0]
    for trend in trend_names["trends"][:Count]:
        json.dump(trend["name"],file,sort_keys = True,indent = 4)
        file.write('\n')
    #close the file
    print("Done")
    file.close()

if __name__ == "__main__":
    ID = "@RobertDowneyJr"
    retweet = "1308813203619549184"
    Count = 5
    Hashtag = "#Persona5"
    Boston = 2367105
    Search = "Covid-19"
    get_all_retweet_screen_names(retweet, Count)
    get_all_mentions_screen_names()
    get_most_recent_tweet(ID, Count)
    get_hashtag_search_tweets(Hashtag,Count,"2020-02-01")
    get_search_tweets(Search,"recent",Count,"2020-12-01")
    get_information_of_ID(ID)
    get_friend_of_ID(ID, Count)
    get_follower_of_ID(ID, Count)
    get_trends_of_location(Boston, Count)




