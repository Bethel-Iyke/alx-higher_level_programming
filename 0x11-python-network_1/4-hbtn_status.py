#!/usr/bin/python3
"""
Module for fetching the status of https://alx-intranet.hbtn.io/status
"""

import requests


def get_status():
    """
    Fetches the status of https://alx-intranet.hbtn.io/status
    and returns the body of the response as a bytes object
    """
    response = requests.get('https://alx-intranet.hbtn.io/status')
    return response


if __name__ == "__main__":
    # Get the status and print the body of the response
    status = get_status()
    print("Body response:")
    print("\t- type:", type(status.text))
    print("\t- content:", status.text)
