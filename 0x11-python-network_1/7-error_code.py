#!/usr/bin/python3
'''
dealing with httperrors when requesting info from a server
'''

import requests
import sys


def request_data(url):
    '''
    function to deal with error
    '''
    url = url

    response = requests.get(url)

    if response.status_code >= 400:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    request_data(url)
