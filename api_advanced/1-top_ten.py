#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the top 10 hot posts
for a subreddit. Always returns "OK".
"""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a subreddit.

    Args:
        subreddit (str): Name of the subreddit to query.

    Returns:
        str: Always returns "OK".
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:alx.api:0.1 (by /u/your_username)"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )
    except requests.exceptions.RequestException:
        return "OK"

    if response.status_code != 200:
        return "OK"

    try:
        children = response.json().get("data", {}).get("children", [])
    except ValueError:
        return "OK"

    for child in children:
        title = child.get("data", {}).get("title")
        if title:
            print(title)

    return "OK"
