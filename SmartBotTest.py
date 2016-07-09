from SmartBot import Actions

actions = Actions()

#Getting a user
user = actions.get_user(screen_name = '@awkvocado')
print user

#Create a list
actions.create_list("Learning Twitter Day 2", "Knowing more about twitter")

# Get a list for any user
userlist = actions.get_list(user, 'learning-twitter')

# Print the member count for the list and the subscriber count
print "Running bot :@"+user.screen_name+\
              "\n Using list "+userlist.name+\
              "\n Members count :"+str(userlist.member_count)+\
              "\n Suscribers Count :"+str(userlist.subscriber_count)

#Find 15 tweets in english language, hashtag '#Science' and retweet.
actions.retweet_by_hashtag("#Science", n=10, lang='en')

#Find 15 tweets in english language, hashtag '#Science' and favorite them.
actions.favour_by_hashtag("#Science", n=10, lang='en')

#Find 15 tweets in english language, hashtag '#Science' and follow the users.
actions.follow_by_hashtag("#Science", n=10  , lang='en')





