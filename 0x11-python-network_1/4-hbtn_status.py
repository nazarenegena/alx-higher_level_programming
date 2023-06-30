#!/usr/bin/python3
"""the script entails:
- Fetches https://alx-intranet.hbtn.io/status.
- a URL requirement,
- a request sent to the URL
"""
import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
