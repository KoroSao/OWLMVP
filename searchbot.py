import tweepy 
import time

consumer_key = #insert key
consumer_secret = #insert key
key = #insert key
secret = #insert key

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

hashtag = "FiatLux"
tweetnumber = 10



def searchBot():
    tweets =  tweepy.Cursor(api.search, hashtag).items(tweetnumber)
    print(tweets)
    for tweet in tweets:
        try: 
            tweet.retweet()
            print("Retweet done !")
            api.create_favorite(tweet.id)
            #api.update_status("@" + tweet.user.screen_name + " XZI Power #FiatLux", tweet.id )
            api.update_with_media('xzi.png', "@" + tweet.user.screen_name + " #XZIPower", tweet.id)
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

searchBot()

