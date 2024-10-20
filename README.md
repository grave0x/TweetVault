# TweetVault

TweetVault is a Python script that scrapes tweets from a list of users' timelines and saves them in a highly compressed JSON format and Markdown. 

## Features
- Scrapes tweets using web scraping
- Compresses JSON data with a custom algorithm
- Saves tweets to a `.json.zlib` file and Markdown format
- Downloads media at highest quality
- Supports multiple users

## Requirements
- Python 3.x
- requests
- BeautifulSoup4
- markdown2

## Installation
1. Clone the repository:
    ```
    git clone https://github.com/your_username/TweetVault.git
    cd TweetVault
    ```
2. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

## Usage
1. Run the script:
    ```
    python tweetvault.py
    ```
2. Enter the Twitter usernames separated by commas when prompted.

## Notes
- Web scraping may be subject to rate limits or blocks by Twitter. Please ensure you comply with Twitter's terms of service.
- This script is for educational purposes only.

## License
This project is licensed under the MIT License.

