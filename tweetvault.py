import requests
from bs4 import BeautifulSoup
import json
import zlib

# Custom compression algorithm
def custom_compress(data):
    compressed = zlib.compress(data.encode('utf-8'), level=9)
    return compressed

# Fetch tweets from a user's timeline
def fetch_tweets(username):
    url = f"https://twitter.com/{username}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    tweets = []
    for tweet in soup.find_all('div', class_='tweet'):
        tweet_id = tweet['data-tweet-id']
        created_at = tweet.find('a', class_='tweet-timestamp')['title']
        tweet_text = tweet.find('p', class_='tweet-text').get_text()
        tweets.append({"id": tweet_id, "created_at": created_at, "text": tweet_text})
    
    return tweets

# Save tweets to a super-minified JSON file
def save_tweets(username):
    tweets = fetch_tweets(username)
    tweet_json = json.dumps(tweets, separators=(',', ':'))
    compressed_tweets = custom_compress(tweet_json)
    
    with open(f"{username}_tweets.json.zlib", 'wb') as f:
        f.write(compressed_tweets)

# Example usage
username = 'user_handle'
save_tweets(username)

