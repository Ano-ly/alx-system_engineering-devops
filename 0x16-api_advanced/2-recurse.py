#!/usr/bin/python3
"""Print top ten subreddit posts"""


def my_recursive(subreddit, after_, hot_list=[]):
    """Recursive function"""

    import requests
    SECRET_KEY = 'faESoE9-rCRtzLnGeQALlTEz4kpUdA'
    CLIENT_ID = 'hh1yZIcidmIZtJEuP5O8dA'

    authing = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
    info = {'grant_type': 'password', 'username': 'girl-anomaly',
            'password': 'amarachi23'}
    header_list = {'User-Agent': 'OneAPI/0.0.1'}
    resp = requests.post('https://www.reddit.com/api/v1/access_token',
                         auth=authing,
                         data=info,
                         headers=header_list)
    MY_TOKEN = resp.json()['access_token']
    new_headers = {**header_list,
                   **{'Authorization': 'bearer {}'.format(MY_TOKEN)}}

    the_resp = requests.get('https://oauth.reddit.com/r/{}/hot.json'
                            .format(subreddit),
                            headers=header_list, params={'after': after_},
                            allow_redirects=False)
    is_resp = requests.get('https://oauth.reddit.com/r/{}/search.json'
                           .format(subreddit),
                           headers=header_list)
    if the_resp.status_code != 200 or is_resp.status_code != 200:
        return (None)
    else:
        after_ = the_resp.json()['data']['after']
        for i in the_resp.json()['data']['children']:
            hot_list.append((i['data']['title']))
        print(hot_list)
        print()
        print(len(hot_list))
        if not after_:
            return (hot_list)
        return (my_recursive(subreddit, after_, hot_list))


def recurse(subreddit):
    """Actual task recursive function"""

    return (my_recursive(subreddit, None, []))
