import tweepy
import time


def searchBot(tweets):
    i = 0
    for tweet in tweets:

        if (i is replyLimit):
            i = 0

        try:
            tweet.retweet()
            print("Retweet done!")
            #Commenting
            print("Replying to: " + tweet.user.screen_name)
            api.update_status(status = replies[i], in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
            #api.update_status('@' + tweet.user.screen_name + " You're great!", tweet.id)
            print("Replied saying: " + replies[i])
            time.sleep(sleepTime)
            i = i + 1

        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(sleepTime)

consumer_key = 'po9d4PdQ0fpTgMm5c3LJfj4jy'
consumer_secret = '28ZrSwNzk64344wMIwuYk6j32sH0Q8D3WGMrybt374amAynq3S'
key = '1221362430107930625-HCZOzlWukm2p1vtWQTEGiAQx9ToyeK'
secret = 'TrzwIr05RJb4nzyhlVoL7Z7AOV11Spimyw5mFDzBvn5Pt'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#api = tweepy.API(auth)

#hashtag = "mask"

hashtags=["COVID", "mask", "masks", "kn95"]
replyLimit = 4
replies=["COVID sucks! However, cheap KN95 masks are available at masklegal.com or @masklegal", "Get a KN95 mask at masklegal.com!", "Stay safe guys, KN95 masks at masklegal.com.", "Need KN95 masks? masklegal.com"]
tweetNumber = 5
sleepTime = 60

for tags in hashtags:
    #If its already retweeted, we dont want it to count as a tweet number
    print("Searching tag: " + tags)
    tweets = tweepy.Cursor( api.search, tags).items(tweetNumber)
    searchBot(tweets)


#for status in tweepy.Cursor(api.user_timeline).items():
    # process status here
    #process_status(status)