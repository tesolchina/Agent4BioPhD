#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web Crawler for Downloading Review Article Full Texts

This script reads a CSV file of review articles and attempts to download
full texts from various sources including DOI links, PubMed Central, and
publisher websites.
"""

import os
import csv
import re
import time
import requests
from urllib.parse import urlparse, unquote
from pathlib import Path
import json
import sys

# Try to import BeautifulSoup, but make it optional
try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False
    print("Warning: BeautifulSoup4 not installed. Some PDF link extraction features may be limited.")
    print("Install with: pip install beautifulsoup4")

# Configuration
INPUT_CSV = "/Users/simonwang/Documents/Usage/AIagent4bio/lab2/data/review_articles.csv"
OUTPUT_DIR = "/Users/simonwang/Documents/Usage/AIagent4bio/lab2/demo/Reviews"
DELAY_BETWEEN_REQUESTS = 2  # seconds to wait between requests

# Headers to mimic a browser
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}

def extract_doi(citation):
    """Extract DOI from citation string."""
    # Pattern 1: https://doi.org/10.xxxx/xxxxx
    doi_pattern1 = r'https?://doi\.org/(10\.\d+/[^\s\)]+)'
    match = re.search(doi_pattern1, citation)
    if match:
        return match.group(1)
    
    # Pattern 2: doi:10.xxxx/xxxxx
    doi_pattern2 = r'doi[:\s]+(10\.\d+/[^\s\)]+)'
    match = re.search(doi_pattern2, citation, re.IGNORECASE)
    if match:
        return match.group(1)
    
    return None

def extract_pubmed_id(citation):
    """Extract PubMed ID from citation string."""
    # Look for "PubMed" followed by potential ID
    pubmed_pattern = r'PubMed[^\d]*(\d+)'
    match = re.search(pubmed_pattern, citation)
    if match:
        return match.group(1)
    return None

def sanitize_filename(filename):
    """Create a safe filename from article title."""
    # Remove or replace invalid characters
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    filename = re.sub(r'\s+', '_', filename)
    filename = filename[:200]  # Limit length
    return filename

def download_from_doi(doi):
    """Attempt to download PDF from DOI."""
    try:
        # Try direct DOI resolution
        doi_url = f"https://doi.org/{doi}"
        print(f"  Attempting DOI resolution: {doi_url}")
        
        session = requests.Session()
        session.headers.update(HEADERS)
        
        # Follow redirects to get the actual publisher page
        response = session.get(doi_url, allow_redirects=True, timeout=30)
        
        if response.status_code == 200:
            final_url = response.url
            print(f"  Resolved to: {final_url}")
            
            # Try to find PDF link on the page
            if 'pdf' in final_url.lower() or final_url.endswith('.pdf'):
                return download_pdf(final_url, session)
            
            # Try common PDF URL patterns
            pdf_urls = [
                final_url.replace('/article/', '/article/pdf/'),
                final_url.replace('/abs/', '/pdf/'),
                final_url + '.pdf',
                final_url.replace('/full/', '/pdf/'),
            ]
            
            for pdf_url in pdf_urls:
                try:
                    pdf_response = session.head(pdf_url, timeout=10)
                    if pdf_response.status_code == 200 and 'pdf' in pdf_response.headers.get('content-type', '').lower():
                        return download_pdf(pdf_url, session)
                except:
                    continue
            
            # Try to extract PDF link from HTML
            if HAS_BS4:
                soup = BeautifulSoup(response.text, 'html.parser')
                # Look for PDF links
                pdf_links = soup.find_all('a', href=re.compile(r'\.pdf|pdf', re.I))
                for link in pdf_links:
                    href = link.get('href', '')
                    if href:
                        if not href.startswith('http'):
                            href = requests.compat.urljoin(final_url, href)
                        try:
                            return download_pdf(href, session)
                        except:
                            continue
        
        return None
    except Exception as e:
        print(f"  Error downloading from DOI: {e}")
        return None

def download_from_pubmed(pubmed_id):
    """Attempt to download from PubMed Central if available."""
    try:
        # Check if paper is in PubMed Central (open access)
        pmc_url = f"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{pubmed_id}/"
        session = requests.Session()
        session.headers.update(HEADERS)
        
        response = session.get(pmc_url, timeout=30)
        if response.status_code == 200:
            # Try to get PDF
            pdf_url = f"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{pubmed_id}/pdf/"
            pdf_response = session.head(pdf_url, timeout=10)
            if pdf_response.status_code == 200:
                return download_pdf(pdf_url, session)
        
        # Try regular PubMed
        pubmed_url = f"https://pubmed.ncbi.nlm.nih.gov/{pubmed_id}/"
        response = session.get(pubmed_url, timeout=30)
        if response.status_code == 200 and HAS_BS4:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Look for full text links
            fulltext_links = soup.find_all('a', string=re.compile(r'full.?text|pdf', re.I))
            for link in fulltext_links:
                href = link.get('href', '')
                if href and 'pdf' in href.lower():
                    if not href.startswith('http'):
                        href = requests.compat.urljoin(pubmed_url, href)
                    return download_pdf(href, session)
        
        return None
    except Exception as e:
        print(f"  Error downloading from PubMed: {e}")
        return None

def download_pdf(url, session=None):
    """Download PDF from URL."""
    try:
        if session is None:
            session = requests.Session()
            session.headers.update(HEADERS)
        
        response = session.get(url, stream=True, timeout=30)
        if response.status_code == 200:
            content_type = response.headers.get('content-type', '').lower()
            if 'pdf' in content_type:
                return response.content
            # Sometimes PDFs are served with wrong content-type
            if len(response.content) > 1000:  # Reasonable size for PDF
                return response.content
        return None
    except Exception as e:
        print(f"    Error downloading PDF: {e}")
        return None

def download_from_semantic_scholar(title, authors):
    """Attempt to download from Semantic Scholar (for open access papers)."""
    try:
        # Search Semantic Scholar API
        search_query = f"{title} {authors}".strip()
        api_url = "https://api.semanticscholar.org/graph/v1/paper/search"
        
        params = {
            'query': search_query[:100],  # Limit query length
            'limit': 1
        }
        
        session = requests.Session()
        session.headers.update({'User-Agent': HEADERS['User-Agent']})
        
        response = session.get(api_url, params=params, timeout=30)
        if response.status_code == 200:
            data = response.json()
            if data.get('data') and len(data['data']) > 0:
                paper = data['data'][0]
                # Check if open access PDF is available
                if 'openAccessPdf' in paper and paper['openAccessPdf']:
                    pdf_url = paper['openAccessPdf'].get('url')
                    if pdf_url:
                        print(f"  Found open access PDF on Semantic Scholar")
                        return download_pdf(pdf_url, session)
        return None
    except Exception as e:
        print(f"  Error searching Semantic Scholar: {e}")
        return None

def save_article_metadata(row, output_dir):
    """Save article metadata as JSON."""
    metadata_file = os.path.join(output_dir, f"{sanitize_filename(row.get('title', 'unknown'))}_metadata.json")
    with open(metadata_file, 'w', encoding='utf-8') as f:
        json.dump(row, f, indent=2, ensure_ascii=False)
    return metadata_file

def process_article(row, output_dir):
    """Process a single article and attempt to download full text."""
    title = row.get('title', 'Unknown Title')
    authors = row.get('authors', '')
    citation = row.get('full_citation', '')
    journal = row.get('journal', '')
    year = row.get('year', '')
    
    print(f"\nProcessing: {title[:80]}...")
    print(f"  Authors: {authors[:60]}...")
    print(f"  Journal: {journal}, Year: {year}")
    
    # Create safe filename
    safe_title = sanitize_filename(title or f"{authors}_{year}")
    if not safe_title or safe_title == 'Unknown_Title':
        safe_title = f"article_{hash(citation) % 10000}"
    
    downloaded = False
    
    # Try DOI first
    doi = extract_doi(citation)
    if doi:
        print(f"  Found DOI: {doi}")
        pdf_content = download_from_doi(doi)
        if pdf_content:
            pdf_file = os.path.join(output_dir, f"{safe_title}.pdf")
            with open(pdf_file, 'wb') as f:
                f.write(pdf_content)
            print(f"  ✓ Downloaded PDF: {pdf_file}")
            downloaded = True
            time.sleep(DELAY_BETWEEN_REQUESTS)
    
    # Try PubMed if not downloaded
    if not downloaded:
        pubmed_id = extract_pubmed_id(citation)
        if pubmed_id:
            print(f"  Found PubMed ID: {pubmed_id}")
            pdf_content = download_from_pubmed(pubmed_id)
            if pdf_content:
                pdf_file = os.path.join(output_dir, f"{safe_title}.pdf")
                with open(pdf_file, 'wb') as f:
                    f.write(pdf_content)
                print(f"  ✓ Downloaded PDF: {pdf_file}")
                downloaded = True
                time.sleep(DELAY_BETWEEN_REQUESTS)
    
    # Try Semantic Scholar for open access
    if not downloaded and title:
        print(f"  Searching Semantic Scholar...")
        pdf_content = download_from_semantic_scholar(title, authors)
        if pdf_content:
            pdf_file = os.path.join(output_dir, f"{safe_title}.pdf")
            with open(pdf_file, 'wb') as f:
                f.write(pdf_content)
            print(f"  ✓ Downloaded PDF from Semantic Scholar: {pdf_file}")
            downloaded = True
            time.sleep(DELAY_BETWEEN_REQUESTS)
    
    # Save metadata regardless
    save_article_metadata(row, output_dir)
    
    if not downloaded:
        print(f"  ✗ Could not download full text (may be behind paywall or not available)")
        # Save citation info as text file
        citation_file = os.path.join(output_dir, f"{safe_title}_citation.txt")
        with open(citation_file, 'w', encoding='utf-8') as f:
            f.write(f"Title: {title}\n")
            f.write(f"Authors: {authors}\n")
            f.write(f"Journal: {journal}\n")
            f.write(f"Year: {year}\n")
            f.write(f"\nFull Citation:\n{citation}\n")
            if doi:
                f.write(f"\nDOI: {doi}\n")
            if pubmed_id:
                f.write(f"PubMed ID: {pubmed_id}\n")
        print(f"  ✓ Saved citation info: {citation_file}")
    
    return downloaded

def main():
    """Main function to process all articles."""
    print("=" * 80)
    print("Review Article Full Text Downloader")
    print("=" * 80)
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR}")
    
    # Read CSV file
    print(f"\nReading CSV file: {INPUT_CSV}")
    articles = []
    try:
        with open(INPUT_CSV, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            articles = list(reader)
        print(f"Found {len(articles)} articles to process")
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return
    
    # Process each article
    downloaded_count = 0
    failed_count = 0
    
    for i, row in enumerate(articles, 1):
        print(f"\n{'='*80}")
        print(f"Article {i}/{len(articles)}")
        print(f"{'='*80}")
        
        try:
            if process_article(row, OUTPUT_DIR):
                downloaded_count += 1
            else:
                failed_count += 1
        except Exception as e:
            print(f"  ✗ Error processing article: {e}")
            failed_count += 1
        
        # Be respectful with rate limiting
        if i < len(articles):
            time.sleep(DELAY_BETWEEN_REQUESTS)
    
    # Summary
    print(f"\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    print(f"Total articles: {len(articles)}")
    print(f"Successfully downloaded: {downloaded_count}")
    print(f"Not available/failed: {failed_count}")
    print(f"\nOutput directory: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()

