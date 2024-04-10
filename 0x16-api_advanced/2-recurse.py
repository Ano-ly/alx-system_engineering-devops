#!/usr/bin/python3
"""Print top ten subreddit posts"""


def my_recursive(subreddit, count, hot_list=[]):
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
                            headers=header_list, params={'count': count})
    if the_resp.status_code != 200:
        return (hot_list)
    else:
        count = len(the_resp.json()['data']['children'])
        for i in the_resp.json()['data']['children']:
            if i['data']['title'] in hot_list:
                return (hot_list)
            hot_list.append((i['data']['title']))
        return (my_recursive(subreddit, count, hot_list))


def recurse(subreddit):
    """Actual task recursive function"""

    count = 0
    return (my_recursive(subreddit, count, []))
