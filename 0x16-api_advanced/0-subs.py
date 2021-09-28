#!/usr/bin/python3
""" Function that queries Reddit API. Returns number subscribers
    (not active usrs, total subs) for a given subreddit.
    If an invalid subreddit is given, function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    URL = "https://www.reddit.com/r/{}/about.json"
    Headers = {"User-Agent": "Custom"}
    response = requests.get(URL.format(subreddit), headers=Headers)
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers', 0)
