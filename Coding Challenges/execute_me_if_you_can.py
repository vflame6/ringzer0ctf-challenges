#!/usr/bin/python

import requests
from pwn import *
from bs4 import BeautifulSoup

URL_CHALLENGE = "http://challenges.ringzer0team.com:10121/"
URL_SOLUTION = "http://challenges.ringzer0team.com:10121/?r=%s"

def main():
    r = requests.get(URL_CHALLENGE)
    parser = BeautifulSoup(r.text, "html.parser")
    data = parser.findAll('div', class_='message')
    challenge = data[0].text.split()[4]


if __name__ == "__main__":
    main()
