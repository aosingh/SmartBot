from time import sleep
from Authenticate import Authenticate

import tweepy


class Actions:
    """
    Actions : This class defines all the actions that our bot can do.
    An example is : Search tweets by certain hashtags

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



    def retweet_by_hashtag(self, hash_tag, n=10, lang='en'):
        """
        This method searches for tweets with certain hashtags and retweets them.

        The number of tweets and the language can be specified as parameters

        :param hash_tag: Bot will search tweets for this hashtag
        :param n: The number of tweets you want the Bot to search. Default is 10.
        :param lang: The language of the tweets. Default is english

        :return:
        """

        for tweet in tweepy.Cursor(self.api.search, q=hash_tag, lang=lang).items(n):
            try:
                print "\n\nFound tweet by ", tweet.user.screen_name
                print "Tweet is ", tweet.text
                if tweet.retweeted is False:
                    tweet.retweet()
            except tweepy.TweepError as e:
                print e
                sleep(10)
            except StopIteration:
                break



    def favour_by_hashtag(self, hash_tag, n=10, lang='en'):
        """
        This method searches for tweets with certain hashtags and favourites them.

        The number of tweets and the language can be specified as parameters

        :param hash_tag: Bot will search tweets by this hashtag
        :param n: The number of tweets you want the Bot to search. Default is 10.
        :param lang: The language of the tweets. Default is english

        :return:
        """
        for tweet in tweepy.Cursor(self.api.search, q=hash_tag, lang=lang).items(n):
            try:
                print "\n\nFound tweet by ", tweet.user.screen_name
                print "Tweet is ", tweet.text
                if tweet.favorite is False:
                    tweet.favorite()
                    print "Favorited"
            except tweepy.TweepError as e:
                print e
                sleep(10)
            except StopIteration:
                break

    def follow_by_hashtag(self, hash_tag, n=10, lang='en'):
        """
        This method searches for tweets with certain hashtags and follow the users of that tweet.

        The number of tweets and the language can be specified as parameters

        :param hash_tag: Bot will search tweets by this hashtag
        :param n: The number of tweets you want the Bot to search. Default is 10.
        :param lang: The language of the tweets. Default is english

        :return:
        """

        for tweet in tweepy.Cursor(self.api.search, q=hash_tag, lang=lang).items(n):
            try:
                print "Tweet is ", tweet.text
                print "\n\nFound tweet by ", tweet.user.screen_name
                if tweet.user.following is False:
                    tweet.user.follow()
                    print "Followed the user"
            except tweepy.TweepError as e:
                print e
                sleep(10)
            except StopIteration:
                break











