import snscrape.modules.twitter as sntwitter
import pandas as pd

# Get Data from Tweeter with snscrape
tweets = []
query = "food OR #food OR #recipe lang:en since:2023-01-01 until:2023-12-31"

for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i > 1000:  # The number of Tweets 
        break
    tweets.append([tweet.date, tweet.content, tweet.likeCount, tweet.retweetCount, tweet.user.followersCount])

df = pd.DataFrame(tweets, columns=["date", "content", "likes", "retweets", "followers"])
print(df.head())


# Creat lable
# def label_popularity(likes):
#     if likes < 50:
#         return "low"
#     elif likes < 200:
#         return "medium"
#     else:
#         return "high"

# df["popularity"] = df["likes"].apply(label_popularity)