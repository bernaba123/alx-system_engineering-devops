#!/usr/bin/python3
"""Function that queries Reddit API
   prints titles: first 10 hot posts listed
"""
import requests


def top_ten(subreddit):
    """first 10 hot posts listed"""
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    Headers = {"User-Agent": "Custom"}
    payload = {"limit": "10"}
    hot = requests.get(URL, headers=Headers, params=payload,
                       allow_redirects=False)
    if hot.status_code != 200:
        print("None")
    else:
        hot_list = hot.json().get("data").get("children")
        hot_titles = [post.get("data").get("title") for post in hot_list]
        print(*hot_titles, sep='\n')
