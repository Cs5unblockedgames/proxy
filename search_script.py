import requests

# Replace with your actual API key and search query
api_key = 'AIzaSyAxmqVDlHp63qoQWbkBqWUst377Eq8nZOw'
search_query = 'Your search query'

# Replace with your proxy information
proxy_url = 'http://141.101.122.98:80'

# Set up the proxy
proxies = {
    'http': proxy_url,
    'https': proxy_url,
}

# Construct the API request URL
url = f'https://www.googleapis.com/customsearch/v1?q={search_query}&key={api_key}'

# Make the request through the proxy
try:
    response = requests.get(url, proxies=proxies)
    response.raise_for_status()  # Check for HTTP errors
    search_results = response.json()
    print(search_results)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
