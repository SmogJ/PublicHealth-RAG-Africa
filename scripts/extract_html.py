import os
import requests
import pathlib
from bs4 import BeautifulSoup

def main(url):
    print(get_url(url))


def get_url(url):
    # send a get request to url
    r= requests.get(url)
    r.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

    url_status= r.status_code
    # url_headers= r.headers['content-type']
    url_content= r.text

    # Parse the HTML content
    soup= BeautifulSoup(url_content, 'html.parser')

    return url_status, soup


if __name__=="__main__":
    url= "https://www.afro.who.int/"
    main(url)
