#!/usr/bin/python3
'''
posting data to a server
'''

import urllib.request
import urllib.parse
import sys


def post_data(url, email):
    '''
    function to post data to a given url
    '''
    url = url
    data = {'email': email}

    data = urllib.parse.urlencode(data).encode('ascii')

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        email_info = response.read().decode('utf-8')
    print(email_info)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_data(url, email)
