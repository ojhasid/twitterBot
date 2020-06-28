import tweepy
import time

consumer_key = 'po9d4PdQ0fpTgMm5c3LJfj4jy'
consumer_secret = '28ZrSwNzk64344wMIwuYk6j32sH0Q8D3WGMrybt374amAynq3S'
key = '1221362430107930625-HCZOzlWukm2p1vtWQTEGiAQx9ToyeK'
secret = 'TrzwIr05RJb4nzyhlVoL7Z7AOV11Spimyw5mFDzBvn5Pt'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
FILE_NAME = 'lastSeen.txt'
#api.update_status('Works')
#tweets = api.mentions_timeline()
#print(tweets[0].text)


#Go on twitter
#Go to trending
#Find the keywords
#Comment on them

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')


def reply():
    for tweet in reversed(tweets):
        if '#ultimatebot' in tweet.full_text.lower():
            print(str(tweet.id) + ': ' + tweet.full_text)
            #Reply
            api.update_status('@' + tweet.user.screen_name + " Auto reply works!! :)", tweet.id)
            #like
            like(tweet.id)
            #retweet
            retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)
    return

def like(tweetID):
    api.create_favorite(tweetID)
    return


def retweet(tweetID):

    api.retweet(tweetID)
    return


while True:
    reply()
    time.sleep(2)
