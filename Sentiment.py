import tweepy
from textblob import TextBlob

consumer_key = 'dzJCt3APhvvLPEKtkyTAiZ1X5'
consumer_secret = '3fQmNbQn6GEhpooR86Rp1OyZPTxWosPSVmIP40kjooQG2Ch5IN'
access_token = '614505666-zW7Ips7POK4GUHvcLEurcXFXGtBtybJGqEAcoOEN'
access_secret = 'JQwnpAaB17rh07JVpx3KZO6HZop1GQVDBhUJRzfmGP3Rn'

consumer_key = '3iLMEd4wo22QUfvFx1odgjikC'
consumer_secret = 'mH20Um1RPWmcS6diMFmXgKfrmJMbwbrZngBnkfnKLfZoq6rej6'
access_token = '614505666-CuRv0Tyhdn32aHpiA3n62f91vE54pUT9X5vPQbot'
access_secret = 'iA35TDLHZSB9f16Kd79vzwODOjbZWYe0KOKEOqzzFh0fM'

consumer_key = 'QfaFNRkAVUX4UEvNPhT7mRcqN'
consumer_secret = 'IjsKJBoMT9sUfLrOmPTQaQOMIE6F15H3dXuNL2Mjk1U0p0OBt9'
access_token = '614505666-lkLLZX3A1je2GLVVspEmrDFshCdi3Ctxv8Jn2ViH'
access_secret = 'V1OA2c3cIN7p1Y9SbNgUoV570YzMhquiSBnOj4SeBzWND'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

ct = 0
sumSent=0
dates = []
sentiments = []
posCount = 0
negCount = 0
while ct < 500:
    for tweet in tweepy.Cursor(api.search, q="Bradley Beal",since="2017-10-18", until="2018-4-13",lang="en").items():
        date = tweet.created_at
        analysis = TextBlob(tweet.text)
        thisSent = analysis.sentiment.polarity
        sentiments.append(thisSent)
        dates.append(date)
        if thisSent != 0 and thisSent:   # not including neutral tweets (news reports)
            sumSent+= thisSent
            print(thisSent)
            # print(date)
            # print(thisSent)
            if thisSent < 0:
                negCount += 1
            elif thisSent > 0:
                posCount += 1
            ct+=1
print(sumSent/ct)
print(ct)
