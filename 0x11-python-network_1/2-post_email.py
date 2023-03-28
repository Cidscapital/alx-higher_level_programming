#!/usr/bin/python3
"""Takes a URL and email and sends a POST request."""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    link = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    req = urllib.request.Request(link, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
