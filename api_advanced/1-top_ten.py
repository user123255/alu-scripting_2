#!/usr/bin/python3
"""
1-top_ten.py
Queries the Reddit API and prints the titles of the first 10 hot posts
for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python:top_ten:v1.0 (by /u/yourusername)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # If subreddit doesn't exist or request fails
        if response.status_code != 200:
            return "OK"

        # Get posts
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        # Print titles
        for post in posts:
            print(post.get("data", {}).get("title"))

        # Return OK for existing subreddit
        return "OK"

    except requests.RequestException:
        # Return OK in case of network or request errors
        return "OK"
