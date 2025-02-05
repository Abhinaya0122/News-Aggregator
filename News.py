import requests

# Define the API key and endpoint
api_key = '24863e1e753b4669b1c7950726c4c511'
url = 'https://newsapi.org/v2/top-headlines'

# Set parameters
parameters = {
    'country': 'in',
    'apiKey': api_key
}

# Make a request
response = requests.get(url, params=parameters)

# Check the response status
if response.status_code == 200:
    data = response.json()
    for article in data['articles']:
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}\n")
else:
    print(f"Failed to fetch news: {response.status_code}")
