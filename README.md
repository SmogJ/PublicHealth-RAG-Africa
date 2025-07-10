# Public Health RAG for Africa

## Project Overview

This project aims to develop a Retrieval-Augmented Generation (RAG) application to provide accurate, timely, and context-specific public health information for African countries. Leveraging the power of Large Language Models (LLMs) combined with a robust retrieval system, the app will enable users to query a curated knowledge base of authoritative public health documents.

## Problem Statement

Public health information in Africa is often fragmented across various official reports, research papers, and organizational websites. This fragmentation can hinder quick access to critical data, guidelines, and localized insights, impacting decision-making for healthcare professionals, policymakers, and researchers. General-purpose LLMs may also lack the specific, up-to-date, and nuanced understanding of African public health contexts, leading to potential inaccuracies or irrelevant responses.

## Solution: A RAG App

Our RAG application addresses these challenges by:
1.  **Curating Authoritative Data:** Building a knowledge base from verified sources such as the WHO Africa office, Africa CDC, national Ministries of Health, and reputable research journals focused on Africa.
2.  **Enhancing Accuracy & Relevance:** Grounding LLM responses in retrieved, factual documents, thereby reducing hallucinations and ensuring context-specific information.
3.  **Providing Transparency:** Citing the sources for every generated answer, allowing users to verify information and explore original documents.
4.  **Focusing on Key Challenges:** Initially concentrating on **Infectious Diseases** and **Rising Non-Communicable Diseases (NCDs)**, two of the most pressing public health issues in the region.

## Project Goals

* To build an accessible and user-friendly RAG application for public health information.
* To provide factual, up-to-date, and contextually relevant answers to user queries.
* To support public health professionals, researchers, and policymakers with rapid access to critical information.
* To enhance data-driven decision-making in addressing infectious diseases and NCDs in Africa.

## Technologies Used (Initial)

* **Python:** The primary programming language.
* **Virtual Environments:** For dependency management.
* **Git & GitHub:** For version control and collaboration.
* **Web Scraping Libraries:** (e.g., `requests`, `BeautifulSoup`, `PyPDF2`) for data acquisition.
* **Natural Language Processing (NLP) Libraries:** For text processing and chunking.
* **Embedding Models:** To convert text into vector representations.
* **Vector Databases:** To store and efficiently search embeddings.
* **Large Language Models (LLMs):** For generating human-like responses.
* **Web Framework:** (e.g., Streamlit, Flask) for the user interface.
* **Cloud Computing:** (e.g., GCP) for deployment (future phase).

## How to Contribute

(Instructions on contributing will be added as the project matures.)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.