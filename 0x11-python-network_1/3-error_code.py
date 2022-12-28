#!/usr/bin/python3
'''
dealing with httperrors when requesting info from a server
'''

import urllib.request
import urllib.error
import sys


def request_data(url):
    '''
    function to deal with error
    '''
    url = url

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
    else:
        print(body)


if __name__ == "__main__":
    url = sys.argv[1]
    request_data(url)
