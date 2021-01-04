#!/usr/bin/python3.8

import tweepy

# Authenticate to Twitter. (Should normally be in a config file)
auth = tweepy.OAuthHandler("REDACTED",
    "REDACTED")
auth.set_access_token("REDACTED,
    "REDACTED")

api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")



# Bot Start
def check_trump_tweets(api, since_id):
    timeStamp = datetime.now()
    print(timeStamp + " - Checking for new Tweets")

# Grabs 10 most recent tweet ID's, not including Retweets or likes
hisTweets = api.user_timeline(screen_name = 'realDonaldTrump', count = 10, include_rts = False)
tweetIdList = []
for status in hisTweets:
    tweetIdList.append(status.id)

# Grab the most recent tweet
recentTweetId = max(tweetIdList)
lastReadTweetIdFile = open("/home/jwheeler/scripts/tweepy_bots/trump_recent_tweet.txt", "r")
lastReadTweetId = lastReadTweetIdFile.read()

# Check if a new tweet was made
if recentTweetId > int(lastReadTweetId):
    print("A new tweet was posted")
    print("New Recent Tweet Id - " + str(recentTweetId))

    # Write latest Tweet ID to file
    f = open("/home/jwheeler/scripts/tweepy_bots/trump_recent_tweet.txt", "w")
    f.write(str(recentTweetId))
    f.close()

    # Respond to the tweet
    api.update_status('@realDonaldTrump Please make sure you research these claims before sharing.', recentTweetId)

else:
    print("No new tweets! Waiting till next run.")
