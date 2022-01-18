import re
from get_cred import get_secret_setting
from client import TwitterFactory
import tweepy

class QueryBuilder(object):

    def __init__(self, searchCountry):
        self.searchCountry = searchCountry

    def getQueryData(self):

        credential = {
            'api_key': get_secret_setting('API_KEY'),
            'api_secret': get_secret_setting('API_SECRET_KEY'),
            'access_key': get_secret_setting('ACCESS_KEY'),
            'access_secret': get_secret_setting('ACCESS_SECRET')
            }
        
        twitter_credential = TwitterFactory(credential)
        twitter = twitter_credential.getConnection()

        #get Keyword
        keywords = get_secret_setting('KEYWORDS')

        #get place
        places = twitter.search_geo(query = self.searchCountry, granularity = 'country')

        #getTweet
        for keyword in keywords:
            query ='{} place:{}'.format(keyword, places[0].id)
            responses = tweepy.Cursor(twitter.search_tweets, 
                                    q = query,
                                    result_type="mixed", 
                                    lang = "en").items(get_secret_setting('NUMBEROFTWEET'))
            return responses

        