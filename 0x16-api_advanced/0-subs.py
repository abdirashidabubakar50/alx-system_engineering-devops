#!/usr/bin/python3
"""This model defines a function that queries
the Reddit API and returns the number of subscribers for a given subreddit
"""
import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyAppName/1.0 (Contact: contact@example.com)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        elif response.status_code == 404:
            return 0
        else:
            return 0
    except requests.RequestException:
        return 0