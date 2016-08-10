from time import sleep
from Authenticate import Authenticate

import tweepy
import datetime


class Actions:
    """
    Actions : This class defines all the actions that our bot can do.
    An example is : Search tweets by query strings

    TO_DO
    This class will get bigger and bigger, which will become difficult to maintain.
    So we will need to refactor actions into different domains and create a class for each domain.
    Examples are UserSpecificActions, HashTagSpecificActions, etc

    """

    def __init__(self):
        """
        Authenticates the Bot and initializes the API object.
        The API object will be used by our bot for all actions

        :return:
        """
        self.api = Authenticate.authenticate_bot()

    def create_list(self, name, description):
        """
        Creates a list under the bot's account

        :param name:
        :param description:
        :return:
        """
        try:
            self.api.create_list(name=name, mode="Public", description=description)
            print "Created list"
        except tweepy.TweepError as e:
            print e

    def get_user(self, screen_name):
        """
        Find a user

        :param screen_name:
        :return: Twitter User
        """
        try:
            return self.api.get_user(screen_name = screen_name)
        except tweepy.TweepError as e:
            print e

    def get_list(self, user, slug):
        """
        Gets a list for any user.

        :param user: The owner of the list
        :param slug: The name or ID of the list
        :return:
        """

        try:
            userlist = self.api.get_list("@"+user.screen_name, slug=slug)
            return userlist
        except tweepy.TweepError as e:
            print e

    def retweet(self, query, n=10, lang='en'):
        """
        Searches for tweets with the query string and retweets them.
        The number of tweets and the language can be specified as parameters

        :param query: search query string
        :param n: The number of tweets you want the Bot to search. Default is 10.
        :param lang: The language of the tweets. Default is english

        :return:
        """

        for tweet in tweepy.Cursor(self.api.search, q=query, lang=lang).items(n):
            try:
                print "\n\nFound tweet by ", tweet.user.screen_name
                print "Tweet is ", tweet.text
                print "Tweet status", tweet.retweeted
                if tweet.retweeted is False:
                    tweet.retweet()
            except tweepy.TweepError as e:
                print e
                sleep(1)
            except StopIteration:
                break

    def favour(self, query, n=10, lang='en'):
        """
        Searches for tweets with the query string and favourites them.
        The number of tweets and the language can be specified as parameters

        :param query: search query string
        :param n: The number of tweets you want the Bot to search. Default is 10.
        :param lang: The language of the tweets. Default is english

        :return:
        """
        for tweet in tweepy.Cursor(self.api.search, q=query, lang=lang).items(n):
            try:
                print "\n\nFound tweet by ", tweet.user.screen_name
                print "Tweet is ", tweet.text
                print "Favorite status", tweet.favorited
                if tweet.favorited is False:
                    tweet.favorite()
                    print "Favorited"
            except tweepy.TweepError as e:
                print e
                sleep(1)
            except StopIteration:
                break

    def follow(self, query, bot_name, n=10, lang='en'):
        """
        Searches for tweets with the query string and follow the users of that tweet.

        The number of tweets and the language can be specified as parameters

        :param query: search query string
        :param bot_name: bot can't follow itself
        :param n: The number of tweets you want the Bot to search. Default is 10.
        :param lang: The language of the tweets. Default is english

        :return:
        """

        for tweet in tweepy.Cursor(self.api.search, q=query, lang=lang).items(n):
            try:
                print "Tweet is ", tweet.text
                print "\n\nFound tweet by ", tweet.user.screen_name
                print "Following status", tweet.user.following
                if tweet.user.following is False and tweet.user.screen_name != bot_name:
                    tweet.user.follow()
                    print "Followed the user"
            except tweepy.TweepError as e:
                print e
                sleep(1)
            except StopIteration:
                break

    def is_within_time(self, tweet, time):
        """
        This method returns true if a tweet is within the 'time' in minutes
        i.e. if it was posted less than a 'time' minutes ago.
        :param tweet:
        :param time:
        :return:
        """
        expires = datetime.timedelta(minutes=time)
        tweet_time = tweet.created_at
        time_since_call = datetime.datetime.utcnow() - tweet_time
        return time_since_call < expires

    def get_followers(self, user):
        """
        This method returns User's followers ordered in which they were added 100 at a time

        :param user: id/screen_name/user_id
        :return:
        """
        try:
            print "User is", user
            return self.api.followers(user);
        except tweepy.TweepError as e:
            print e.reason


    def get_favorites(self, user):
        """
        This method returns the tweets objects favorited by a user
        :param user:id/screen_name
        :return:
        """
        try:
            print "User is", user
            return self.api.favorites(user)
        except tweepy.TweepError as e:
            print e.reason


    def relevant_tweets(self, tweets, time):
        """
        Returns a filtered list of tweets by time
        This filter can be modified to increase the relevance.

        :param time:
        :return:
        """
        relevant_tweets = []
        for tweet in tweets:
            if self.is_within_time(time):
                relevant_tweets.append(tweet)
        return relevant_tweets

    def get_tweets(self, query, n=10, lang='en'):
        """
        Returns n tweets for the given search term and given query lanaguage
        :param query:
        :param n:
        :param lang:
        :return:
        """
        tweets = []
        try:
            for tweet in tweepy.Cursor(self.api.search, q=query, lang=lang).items(n):
                tweets.append(tweet)
            return tweets
        except tweepy.TweepError as e:
            print e.reason
















