import requests
from bs4 import BeautifulSoup
import json
import zlib
import os
import markdown2

def custom_compress(data):
    compressed = zlib.compress(data.encode('utf-8'), level=9)
    return compressed

def fetch_tweets(username):
    url = f"https://twitter.com/{username}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    tweets = []
    for tweet in soup.find_all('div', class_='tweet'):
        tweet_id = tweet['data-tweet-id']
        created_at = tweet.find('a', class_='tweet-timestamp')['title']
        tweet_text = tweet.find('p', class_='tweet-text').get_text()
        
        media_urls = []
        for media in tweet.find_all('img', class_='media-image'):
            media_urls.append(media['src'])

        tweets.append({"id": tweet_id, "created_at": created_at, "text": tweet_text, "media": media_urls})
    
    return tweets

def save_tweets(username_list):
    for username in username_list:
        tweets = fetch_tweets(username)
        tweet_json = json.dumps(tweets, separators=(',', ':'))
        compressed_tweets = custom_compress(tweet_json)
        
        os.makedirs(f"TweetVault/{username}", exist_ok=True)
        
        with open(f"TweetVault/{username}/{username}_tweets.json.zlib", 'wb') as f:
            f.write(compressed_tweets)
        
        with open(f"TweetVault/{username}/{username}_tweets.md", 'w') as f:
            for tweet in tweets:
                md_content = f"### Tweet ID: {tweet['id']}\n**Created at:** {tweet['created_at']}\n\n{tweet['text']}\n"
                for media_url in tweet['media']:
                    md_content += f"![Media]({media_url})\n"
                f.write(md_content + "\n---\n")
        
        for tweet in tweets:
            for media_url in tweet['media']:
                media_response = requests.get(media_url)
                media_filename = os.path.join(f"TweetVault/{username}", os.path.basename(media_url))
                with open(media_filename, 'wb') as f:
                    f.write(media_response.content)

if __name__ == "__main__":
    usernames = input("Enter Twitter usernames separated by commas: ").split(',')
    save_tweets(usernames)

