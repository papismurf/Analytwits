import os
import json
import csv

import twitter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt

ACCESS_TOKEN = 'ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'ACCESS_TOKEN_SECRET'
CONSUMER_KEY = 'CONSUMER_KEY'
CONSUMER_SECRET = 'CONSUMER_SECRET'

# Define the location id for the UK
# With Yahoo Where on Earth ID
WOEID = 23424975
# Define language of tweets
LANG = "en"
# Define type of tweets we are after
TWEETS_TYPE = "recent"
# Define max number of tweets per trend
MAX_STATUSES = 1000

# API configuration
# API with request rate limited
api = twitter.Api(CONSUMER_KEY,
                  CONSUMER_SECRET,
                  ACCESS_TOKEN,
                  ACCESS_TOKEN_SECRET,
                  sleep_on_rate_limit=True)

# Check twitter account api details are correct
# print(api.VerifyCredentials())

# Query the Twitter API for the current top 10 trends in the UK.
uk_trends = api.GetTrendsWoeid(WOEID)

print(uk_trends)


# Return the 1000 most recent tweets for each trend
for trend in uk_trends:
    '''
    Extract name of each trend returned by Trend model
    and search required count value of recent tweets per trend
    '''
    trend = str(trend.name)
    count = MAX_STATUSES
    search_results = api.GetSearch(term=trend, count=count)
    print(search_results)

# Init sentiment analysis object
analyzer = SentimentIntensityAnalyzer()
# Compound sentiment extraction use example
# exampleCompoundSentiment = analyzer.polarity_scores("I love cats and dogs")["compound"]
# print(exampleCompoundSentiment)
