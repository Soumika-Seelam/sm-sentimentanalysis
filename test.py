import snscrape.modules.twitter as sntwitter
import ssl

# Disable SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

for tweet in sntwitter.TwitterSearchScraper("AI").get_items():
    print(tweet.content)
    break
