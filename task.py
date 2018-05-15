"""

The object of this task is to gather and analyse sentiment data around the current top Twitter trends in the UK. Using Python 3 and the library found at https://github.com/bear/python-twitter, please perform the following inside this file:

1. Create a Twitter application and API access credentials (https://python-twitter.readthedocs.io/en/latest/getting_started.html)

2. Query the Twitter API for the current top 10 trends in the UK. 

3. For each of these trends, pull the 1000 most recent tweets (as a bonus, remove retweets). You may want to limit the speed of your code here or risk Twitter rate limits.

4. Analyse each of these tweets for sentiment using the library and function provided below.

5. Export a csv file to the output_files folder which contains some statistical/aggregate information of your choice in tabular format about the top 10 trends based on their related tweets and/or their sentiment values.

6. (As an optional bonus) Produce a sentiment frequency distribution chart for each trend using the python Matplotlib library, and place them in the output_files folder. (Hint : https://stackoverflow.com/questions/22127769/python-frequency-of-occurrences)

7. Zip and return this folder containing the results and code!

For any questions / issues / problems, please do not hesitate to contact danny@moonshotcve.com

"""
import json

import twitter # https://github.com/bear/python-twitter
# Sentiment analysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

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
	'token' : '',
	'token_secret' : '',
	'consumer_key' : '',
	'consumer_secret' : ''
}

# Init sentiment analysis object
analyzer = SentimentIntensityAnalyzer()
# Compound sentiment extraction use example
# exampleCompoundSentiment = analyzer.polarity_scores("I love cats and dogs")["compound"]
# print(exampleCompoundSentiment)