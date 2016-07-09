import tweepy
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


class Authenticate:
    """
    This class has methods to authenticate and return the API object.
    The returned API object will be used by our bot to perform actions like
        1. GET USER
        2. FETCH TWEETS
        3. FOLLOW USERS
        3. etc

    """

    @staticmethod
    def authenticate_bot():
        """
        Authenticate the bot: Twitter uses OAuth authentication standard.
        The following are needed to make request on behalf of the application.
        CONSUMER_KEY,
        CONSUMER_SECRET,
        ACCESS_TOKEN and
        ACCESS_TOKEN_SECRET

        :return: `API` object which can be used by SmartBot to make requests.

        :exception: `TweepError` when invalid credentials are provided.
        """
        try:
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
            auth.secure = True
            api = tweepy.API(auth)
            api.verify_credentials()
            return api
        except tweepy.TweepError as e:
            return e.reason









