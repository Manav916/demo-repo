import requests
import random

API_KEY = 'Svsddsjnsajsgh23kjk522882b28dbsndkj'
BASE_URL = 'https://api.news.ycombinator.com'

# List of random topics
topics = ['technology', 'science', 'health', 'sports', 'business', 'entertainment']

# Choose a random topic
topic = random.choice(topics)

# Set up the parameters for the request
params = {
    'q': topic,
    'sortBy': 'publishedAt',
    'apiKey': API_KEY
}

# Make the request to the News API
response = requests.get(BASE_URL, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    news_data = response.json()
    articles = news_data['articles']

    # Print the latest news articles
    print(f"Latest news on {topic.capitalize()}:")
    for article in articles[:5]:  # Displaying the top 5 articles
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}\n")
else:
    news_data = response.json()
    print(f"Failed to fetch news. Status code: {response.status_code}, Error: {news_data.get('message', 'No error message available')}")

resposne = requests.get(BASE_URL, params=params)
print(response.status_code)
