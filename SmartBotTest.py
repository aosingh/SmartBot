from SmartBot import Actions

#initialize actions object
actions = Actions()

#Getting a user
user = actions.get_user(screen_name = '@awkvocado')
print user

#Create a list
#actions.create_list("Learning Twitter Day 2", "Knowing more about twitter")

# Get a list for any user
userlist = actions.get_list(user, 'learning-twitter')

# Print the member count for the list and the subscriber count
print "Running bot :@"+user.screen_name+\
              "\n Using list "+userlist.name+\
              "\n Members count :"+str(userlist.member_count)+\
              "\n Suscribers Count :"+str(userlist.subscriber_count)

#Find 15 tweets in english language, hashtag '#Science' and retweet.
#actions.retweet("#Science", n=10, lang='en')

#Find 15 tweets in english language, hashtag '#Science' and favorite them.
#actions.favour("#Science", n=10, lang='en')

#Find 15 tweets in english language, hashtag '#Science' and follow the users.
actions.follow("#Science", 'awkvocado', n=10  , lang='en')


#Get Followers for a user
for user in actions.get_followers('@awkvocado'):
    print user.screen_name


#Get Favorite tweets for a user
for status in actions.get_favorites('@awkvocado'):
    print status.id

for tweets in actions.get_tweets(query="Science", n=26):
    print tweets










