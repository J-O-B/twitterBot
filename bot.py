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

FILE_NAME = "last_seen.txt"


def read_last_tweet(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def store_last_seen(FILE_NAME):
    file_write = open(FILE_NAME, "w")
    file_write.write(str(last_seen_id))
    file_write.close()
    return


def reply():
    tweets = api.mentions_timeline(
        read_last_seen(FILE_NAME), tweet_mode='extended')

    for tweet in reversed(tweets):
        if '#100daysofcode' in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status(
                "@" + tweet.user.screen_name + (
                    "Keep Up The Work! (Sent From Tweepy Python Bot)",
                    tweet.id))
            api.create_favorite(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)


while True:
    reply()
    time.sleep(30)