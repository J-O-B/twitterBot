import tweepy
import time

"""Need to update keys with approval"""
consumer_key = 1
consumer_secret = 1


key = 1
secret = 1


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

hashtag1 = "#coder"
hashtag2 = "#coding"
hashtag3 = "#programming"
hashtag4 = "#developer"
hashtag5 = "#javascript"
tweetNumber = 2
tweets1 = tweepy.Cursor(api.search, hashtag1).item(tweetNumber)
tweets2 = tweepy.Cursor(api.search, hashtag2).item(tweetNumber)
tweets3 = tweepy.Cursor(api.search, hashtag3).item(tweetNumber)
tweets4 = tweepy.Cursor(api.search, hashtag4).item(tweetNumber)
tweets5 = tweepy.Cursor(api.search, hashtag5).item(tweetNumber)


def searchBot1():
    for tweet in tweets1:
        try:
            tweet.retweet()
            time.sleep(15)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(15)


searchBot1()


def searchBot2():
    for tweet in tweets2:
        try:
            tweet.retweet()
            time.sleep(15)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(15)


searchBot2()


def searchBot3():
    for tweet in tweets3:
        try:
            tweet.retweet()
            time.sleep(15)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(15)


searchBot3()


def searchBot4():
    for tweet in tweets4:
        try:
            tweet.retweet()
            time.sleep(15)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(15)


searchBot4()


def searchBot5():
    for tweet in tweets5:
        try:
            tweet.retweet()
            time.sleep(15)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(15)


searchBot5()
