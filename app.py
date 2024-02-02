from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    api_key = 'AIzaSyAxmqVDlHp63qoQWbkBqWUst377Eq8nZOw'
    search_query = request.form['search_query']
    proxy_url = 'http://141.101.122.98:80'

    proxies = {
        'http': proxy_url,
        'https': proxy_url,
    }

    url = f'https://www.googleapis.com/customsearch/v1?q={search_query}&key={api_key}'

    try:
        response = requests.get(url, proxies=proxies)
        response.raise_for_status()
        search_results = response.json()
        return render_template('result.html', results=search_results)
    except requests.ex
