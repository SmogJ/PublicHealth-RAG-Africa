import os
import requests
import pathlib
from bs4 import BeautifulSoup

def main():
    print(get_url())

def get_url():
    r= requests.get("https://www.afro.who.int/")
    url_status= r.status_code
    return url_status



if __name__=="__main__":
    main()