# all api functions used are inspired by examples provided by http://docs.tweepy.org/en/latest/install.html

import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key) # put key in doible air quotes

max_tweet = 20  

length = [0 for i in range(max_tweet)]

api = tweepy.API(auth)
c = 0
for tweet in tweepy.Cursor(api.search, q='good day').items(max_tweet):
    print(tweet.text)
    length[c] = len(tweet.text)
    c += 1

max_len = max(length)
indexed = length.index(max_len)

print( f"The longest tweet is tweet number {indexed} from the list of {max_tweet} with a length of {max_len}")