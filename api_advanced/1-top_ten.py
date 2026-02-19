#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the top 10 hot posts
for a subreddit.

Provides the function `top_ten(subreddit)` which prints the titles of the
first 10 hot posts for the given subreddit. Always returns "OK".
"""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a subreddit.

    Args:
        subreddit (str): Name of the subreddit to query.

    Returns:
        str: Always returns "OK" after printing titles (or if subreddit is invalid).
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
        # Network or request error
        return "OK"

    if response.status_code != 200:
        # Subreddit doesn't exist or is inaccessible
        return "OK"

    try:
        children = response.json().get("data", {}).get("children", [])
    except ValueError:
        # JSON decoding error
        return "OK"

    # Print titles if available
    for child in children:
        title = child.get("data", {}).get("title")
        if title:
            print(title)

    return "OK"


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        sys.exit(1)

    subreddit = sys.argv[1]
    result = top_ten(subreddit)
    print(result)
