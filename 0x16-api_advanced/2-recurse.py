#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. If no results
are found for the given subreddit, the function should return None.

Hint: The Reddit API uses pagination for separating pages of responses.

Requirements:
    - Prototype: def recurse(subreddit, hot_list=[])
    - Note: You may change the prototype, but it must be able to be called
      with just a subreddit supplied. AKA you can add a counter, but it must
      work without supplying a starting value in the main.
    - If not a valid subreddit, return None.
    - NOTE: Invalid subreddits may return a redirect to search results. Ensure
      that you are not following redirects.
Your code will NOT pass if you are using a loop and not recursively calling
the function! This /can/ be done with a loop but the point is to use a
recursive function. :)
"""
import requests


def add_title(hot_list, hot_posts):
    """ Adds item into a list """
    if len(hot_posts) == 0:
        return
    hot_list.append(hot_posts[0]['data']['title'])
    hot_posts.pop(0)
    add_title(hot_list, hot_posts)


def recurse(subreddit, hot_list=None, after=None):
    """Returns a list of all hot articles for a given subreddit"""
    if hot_list is None:
        hot_list = []
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    params = {
        "after": after
    }
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        hot_posts = data['data']['children']
        add_title(hot_list, hot_posts)
        after = data["data"]["after"]
        if not after:
            return hot_list
        return recurse(subreddit, hot_list=hot_list, after=after)
    return None
