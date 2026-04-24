import requests
import hashlib
from bs4 import BeautifulSoup 
from pathlib import Path

# ==========================
# Define HTML data directory
# ==========================
project_dir: Path= Path(__file__).resolve().parent.parent.parent # root directory of the project
# Processed data
processed_file: Path= project_dir / "data" / "html_publication" / "processed_file.jsonl"


def main():
    ...
    # 1. Import pipeline
    # 2. Save pipeline content as JSONL


# ======================================
# Save the extracted content as JSONL
# ======================================
def save_content():
    ...
    # 1. Get content from 
    # 2. Save content as JSONL


if __name__=="__main__":    main()