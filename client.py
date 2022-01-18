import tweepy

class TwitterFactory(object):

    def __init__(self, credential):
        self.credential = credential


    def getConnection(self):
        connection = tweepy.OAuthHandler(self.credential['api_key'], self.credential['api_secret'])
        connection.set_access_token(self.credential['access_key'], self.credential['access_secret'])
        api = tweepy.API(connection)
        return api


