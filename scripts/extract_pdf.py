import sys
import re
import requests
from bs4 import BeautifulSoup, SoupStrainer
from extract_html import get_page_urls, get_all_content_urls


pub_url= "https://www.afro.who.int/publications"

def get_pdf():
    print(get_pagination())


def get_pagination():
    """Scrape URLs across paginated results."""
    pages= get_page_urls(pub_url)
    
    pdf_urls= get_all_content_urls(pages)

    return pdf_urls


if __name__=="__main__":
    get_pdf()