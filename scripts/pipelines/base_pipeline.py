import requests
import hashlib
from bs4 import BeautifulSoup 
from pathlib import Path

# ==========================
# Define Extracted data file
# ==========================
project_dir: Path= Path(__file__).resolve().parent.parent.parent # root directory of the project
# Processed data
processed_file: Path= project_dir / "data" / "html_publication" / "processed_file.jsonl"


# # def main(kwargs):
#     ...


# ==========================
# Clean Content
# ==========================
    # 1. get content form jsonl file
    # 2. select only the content field from the jsonl file
    # Clean the content
        # remove spacing and new lines
        # remove html tags
        # remove special characters


# ======================================
# Save the Processed content as JSONL
# ======================================
def save_content():
    ...
    # 1. Get content from 
    # 2. Save content as JSONL


# if __name__=="__main__":    main()