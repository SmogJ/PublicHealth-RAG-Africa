import sys
import re
import requests
from bs4 import BeautifulSoup, SoupStrainer
from extract_html import get_page_urls, get_all_content_urls



pub_url= "https://www.afro.who.int/publications"


def get_pdf(pub_url):

    pages= get_page_urls(pub_url)

    pdf_page_urls= get_all_content_urls(pages[:1])

    
    for page in pdf_page_urls:
        print(get_pdf_page_content(page))




def get_pdf_page_content(urls):
    pages= urls
    return pages


    # try:
        # r = requests.get(pdf_urls, timeout=10)
        # r.raise_for_status()

        # soup = BeautifulSoup(r.text, 'html.parser')

        # # Find the main content of the story itself.
        # pdf_content = soup.find("article", "publication is-promoted full clearfix")

        # If the original structure is not found, try the alternative
        # if not pdf_content:
        #     pdf_content = soup.find("article", class_="publication full clearfix")

        # if pdf_content:
        #     # We get all the pdf title, date and time, article body
        #     pdf_title= pdf_content.find("h3", "publication-title")

    #     return pdf_content

    # except requests.exceptions.RequestException as e:
    #     print(f"Error getting content from {pdf_urls}: {e}")
    #     return None


if __name__=="__main__":
    get_pdf(pub_url)