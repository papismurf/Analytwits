import os
import json
import csv

import twitter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt

ACCESS_TOKEN = '276176566-rCDQiAgggd4cIqeiHIN8Z18iHMgXyEnH5ZbDIf1R'
ACCESS_TOKEN_SECRET = 'v4f3Ql6QnBNmLz6acDZPmkGhiXsuMJRyZWAkcalesIb2w'
CONSUMER_KEY = 'nJIXAllPVZGtKpQJmnH2q8YbC'
CONSUMER_SECRET = 'O6YzlUQwUOaKEMhBFo6whuULxbtfmLDPCImSTGSmduWD9a2XFK'

# Define the location id for the UK
WOEID = 23424975
# Define language of tweets
LANG = "en"
# Define type of tweets we are after
TWEETS_TYPE = "recent"
# Define max number of tweets per trend
MAX_STATUSES = 1000

# API config
# API with request rate limited
api = twitter.Api(CONSUMER_KEY,
                  CONSUMER_SECRET,
                  ACCESS_TOKEN,
                  ACCESS_TOKEN_SECRET,
                  sleep_on_rate_limit=True)

print(api.VerifyCredentials())

# Query the Twitter API for the current top 10 trends in the UK.
uk_trends = api.GetTrendsWoeid(WOEID)
print(uk_trends)


# Return the 1000 most recent tweets for each trend

for trend in uk_trends:
    count = MAX_STATUSES
    trend = trend
    search_results = api.GetSearch(term=trend, count=count)
    print(search_results)

# Init sentiment analysis object
analyzer = SentimentIntensityAnalyzer()
# Compound sentiment extraction use example
# exampleCompoundSentiment = analyzer.polarity_scores("I love cats and dogs")["compound"]
# print(exampleCompoundSentiment)
