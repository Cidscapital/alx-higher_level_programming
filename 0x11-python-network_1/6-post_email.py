#!/usr/bin/python3
"""Script that sends a POST request to a given URL with a given email
and displays the body of the response
Usage: ./6-post_email.py <URL> <email>
"""
import sys
import requests


if __name__ == "__main__":
    link = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(link, data=value)
    print(r.text)
