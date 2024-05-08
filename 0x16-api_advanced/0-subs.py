#!/usr/bin/python3
""" Queries the Reddit API & returns the num of subs for a given subreddit """
import requests


def number_of_subscribers(subreddit):
    """ Finds the num of subs in a subreddit """

    header = {'User-Agent': 'Basset'}
    url = "https://api.reddit.com/r/{}/about/".format(subreddit)
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        subs = response.json()["data"]["subscribers"]
    else:
        subs = 0
    return subs
