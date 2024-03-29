#!/usr/bin/python3
"""Script that displays the X-Request-Id header variable of a request to
a given url
Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    link = sys.argv[1]

    r = requests.get(link)
    print(r.headers.get("X-Request-Id"))
