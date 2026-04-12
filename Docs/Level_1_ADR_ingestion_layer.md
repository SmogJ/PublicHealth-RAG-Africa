# ADR-001: Data Ingestion Architecture (Level 1)

## Status

**Accepted**

## Context

The Public Health RAG system depends on **high-quality, structured, and trustworthy data** sourced from public health authorities such as:

* World Health Organization (WHO AFRO)
* National Ministries of Health
* Africa CDC
* Scientific publications and reports

The system must support:

* Clinical-grade accuracy (e.g., dosage, treatment protocols)
* Source traceability (WHO-only, region-specific filtering)
* Structured retrieval (sections, tables, metadata-aware search)

### Current State

The system already includes:

* HTML scraper (`extract_html.py`)
* PDF downloader (`get_pdf.py`)
* Initial PDF extractor (`extract_pdf.py`)
* Organized storage:

  * `data/raw/`
  * `data/pdf_publication/`
  * `data/pdf_data/`

However, the ingestion layer currently suffers from:

1. **Schema inconsistency**

   * HTML and PDF outputs differ in structure
2. **Unstructured PDF extraction**

   * Poor handling of tables and layout
3. **Lack of data normalization**
4. **No quality validation layer**
5. **No unified processed data store**

---

## Decision

I will implement a **multi-stage, schema-driven Data Ingestion Architecture** with a unified processing pipeline.

---

## Architecture Overview (Level 1)

Diagram can be found here: [Data Ingestion Architecture Diagram](\PublicHealth-RAG-Africa\Docs\Diagrams\level1-ingestion-architecture.drawio)

---

## Components

### 1. Data Sources

#### Supported Sources:

* WHO AFRO (HTML pages, publications)
* Public health reports (PDF)
* Government health portals

#### Data Types:

* HTML articles (news, reports)
* PDF documents (guidelines, publications)

---

### 2. Scrapers / Downloaders

#### Responsibilities:

* Discover URLs
* Crawl paginated sources
* Download raw content

#### Current Implementation:

* `extract_html.py`
* `get_pdf.py`

#### Design Principle:

> Separate **discovery** from **extraction**

---

### 3. Raw Data Storage

```id="raw-structure"
data/
  raw/
    html_publication/
    pdf_publication/
```

#### Purpose:

* Store unmodified source data
* Enable reprocessing without re-scraping

---

### 4. Extraction Layer

#### Responsibilities:

* Convert raw HTML/PDF into structured data
* Extract:

  * Title
  * Content
  * Sections (future)
  * Tables (critical for clinical data)
  * Metadata (basic)

#### Technologies:

* HTML: BeautifulSoup
* PDF: `pdfplumber` (preferred over PyPDF2)

#### Output:

Intermediate structured documents

---

### 5. Cleaning & Normalization

#### Responsibilities:

* Remove:

  * Headers/footers
  * Page numbers
  * Boilerplate text
* Normalize:

  * Whitespace
  * Encoding
  * Text continuity

---

### 6. Metadata Enrichment

#### Responsibilities:

* Add structured metadata:

  * Source (WHO_AFRO, NCDC, etc.)
  * Document type (news, guideline, report)
  * Country
  * Publication date
  * Disease tags (future NLP step)

---

### 7. Quality Validation Layer (Critical)

#### Purpose:

Ensure only **high-quality, usable documents** enter the RAG system.

#### Validation Rules:

* Non-empty content
* Minimum length threshold
* Valid title
* Language check (English)
* Duplicate detection

#### Outcome:

* Accept → store
* Reject → log + skip

---

### 8. Processed Data Store (Source of Truth)

```id="processed-structure"
data/
  processed/
    all_documents.jsonl
```

#### Format:

JSON Lines (stream-friendly, scalable)

#### Canonical Document Schema:

```json
{
  "source": "WHO_AFRO",
  "doc_type": "news | publication | guideline",
  "title": "string",
  "url": "string",
  "content": "string",
  "sections": [],
  "tables": [],
  "metadata": {
    "country": "string",
    "date": "string",
    "author": "string",
    "tags": []
  }
}
```

---

## Key Design Decisions

### 1. Unified Schema Across All Sources

All documents (HTML + PDF) must conform to a single schema.

**Rationale:**

* Simplifies downstream processing
* Enables consistent chunking and retrieval

---

### 2. JSONL as Storage Format

**Rationale:**

* Efficient for large datasets
* Stream processing compatible
* Easy ingestion into vector databases

---

### 3. PDF Table Extraction as First-Class Citizen

**Rationale:**

* Clinical data (dosages, thresholds) are often in tables
* Ignoring tables leads to unsafe or incorrect answers

---

### 4. Separation of Raw vs Processed Data

**Rationale:**

* Enables reproducibility
* Supports reprocessing without re-scraping
* Critical for debugging ingestion issues

---

### 5. Early Quality Validation

**Rationale:**

* Prevents garbage-in → garbage-out
* Improves retrieval precision
* Reduces hallucination risk

---

## Consequences

### Positive

* High-quality, structured knowledge base
* Improved retrieval accuracy
* Reduced hallucinations
* Easier debugging and observability
* Scalable ingestion pipeline

---

### Trade-offs

* Increased upfront complexity
* Slower initial development
* Requires careful schema design

---

## Future Extensions (Level 2+)

* Section detection (heading-based parsing)
* Advanced table structuring (row/column semantics)
* OCR support for scanned PDFs
* Incremental ingestion (new documents only)
* Automated tagging (disease classification)
* Source credibility scoring

---

## Implementation Notes

### Immediate Next Steps

1. Define and finalize canonical schema
2. Refactor:

   * `extract_html.py` → output unified schema
   * `extract_pdf.py` → use `pdfplumber`
3. Implement processed output:

   * `data/processed/all_documents.jsonl`
4. Add basic validation checks

---

## Versioning


* Version: 1.0
* Status: Active Development Roadmap
* Owner: Jeffrey Esedo (Developer)