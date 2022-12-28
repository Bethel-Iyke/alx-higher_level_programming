#!/usr/bin/python3
'''
posting data to a server
'''

import requests
import sys


def post_data(url, email):
    '''
    function to post data to a given url
    '''
    url = url

    request = requests.post(url, data={'email': email})
    print(request.text)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_data(url, email)
