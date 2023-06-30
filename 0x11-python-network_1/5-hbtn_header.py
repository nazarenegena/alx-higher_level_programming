#!/usr/bin/python3
"""the script entails:
- displays X-Request-Id header var of request to a given URL.
- a URL requirement,
- a request sent to the URL
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
