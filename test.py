import snscrape.modules.twitter as sntwitter

# Testing snscrape by fetching a single tweet
for tweet in sntwitter.TwitterSearchScraper("AI").get_items():
    print(tweet.content)
    break