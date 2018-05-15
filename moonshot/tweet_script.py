import os
import json
import csv

import twitter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Define the location id for the UK
WOEID = 23424975
# Define language of tweets
LANG = "en"
# Define type of tweets we are after
TWEETS_TYPE = "recent"
# Define max number of tweets per trend
MAX_STATUSES = 1000

# API config
twitterConfig = {
    'access_token_key': os.environ.get('ACCESS_TOKEN'),
    'access_token_secret': os.environ.get('ACCESS_TOKEN_SECRET'),
    'consumer_key': os.environ.get('CONSUMER_KEY'),
    'consumer_secret': os.environ.get('CONSUMER_SECRET')
}

# Init sentiment analysis object
analyzer = SentimentIntensityAnalyzer()
# Compound sentiment extraction use example
# exampleCompoundSentiment = analyzer.polarity_scores("I love cats and dogs")["compound"]
# print(exampleCompoundSentiment)
