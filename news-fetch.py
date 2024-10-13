import requests
import random

BASE_URL = 'https://api.news.ycombinator.com'

# Make the request to the News API
response = requests.get(BASE_URL)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    news_data = response.json()
    articles = news_data['articles']

    # Print the latest news articles
    for article in articles[:5]:  # Displaying the top 5 articles
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}\n")
else:
    news_data = response.json()
    print(f"Failed to fetch news. Status code: {response.status_code}, Error: {news_data.get('message', 'No error message available')}")
