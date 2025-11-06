#!/usr/bin/env python3
"""
Extract review articles from the references section of the paper.
"""

import re
import csv

# Read the paper file
input_file = "/Users/simonwang/Documents/Usage/AIagent4bio/lab1/data/Badia-i-Mompel et al 2023.md"

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the References section
ref_start = content.find("References")
if ref_start == -1:
    print("Error: Could not find References section")
    exit(1)

# Extract references section (from "References" to "Acknowledgements" or end of file)
ref_section = content[ref_start:]
ack_start = ref_section.find("Acknowledgements")
if ack_start != -1:
    ref_section = ref_section[:ack_start]

# Patterns to identify review articles
review_patterns = [
    r'Nat\. Rev\.',  # Nature Reviews journals
    r'Annu\. Rev\.',  # Annual Review journals
    r'Trends',  # Trends journals
    r'This.*review',  # Explicit mentions
    r'extensive review',  # Explicit mentions
    r'reviewed elsewhere',  # Explicit mentions
]

# List to store review articles
review_articles = []

# Split references by lines and process
lines = ref_section.split('\n')
current_ref = None
in_reference = False

for i, line in enumerate(lines):
    line = line.strip()
    
    # Skip empty lines and metadata lines
    if not line or line in ['Article', 'CAS', 'PubMed', 'Google Scholar', 'References']:
        continue
    
    # Skip citation counts and other metadata
    if re.match(r'^\d+[,\d]*$', line) or line.startswith('Download references'):
        continue
    
    # Check if this line starts a new reference (author names pattern)
    # Pattern: LastName, FirstInitial. & LastName, FirstInitial.
    if re.match(r'^[A-Z][a-z]+.*,.*[A-Z]\.', line) or re.match(r'^[A-Z][a-z]+.*et al\.', line):
        # Save previous reference if it was a review
        if current_ref and current_ref.get('is_review'):
            review_articles.append(current_ref)
        
        # Start new reference
        current_ref = {
            'full_text': line,
            'is_review': False,
            'authors': '',
            'title': '',
            'journal': '',
            'year': '',
            'volume': '',
            'pages': ''
        }
        in_reference = True
        
        # Check if this line contains review indicators
        for pattern in review_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                current_ref['is_review'] = True
                break
        
        # Try to extract author names
        author_match = re.match(r'^([^\.]+)\.', line)
        if author_match:
            current_ref['authors'] = author_match.group(1).strip()
    
    elif in_reference and current_ref:
        # Continue building the reference
        current_ref['full_text'] += ' ' + line
        
        # Check for review indicators in this line
        for pattern in review_patterns:
            if re.search(pattern, line, re.IGNORECASE):
                current_ref['is_review'] = True
                break
        
        # Try to extract journal, year, volume, pages
        # Pattern: Journal Name Volume, Pages (Year)
        journal_match = re.search(r'\.\s+([^\.]+)\.?\s+(\d+)[,\s]+([\d–-]+)\s+\((\d{4})\)', line)
        if journal_match:
            current_ref['journal'] = journal_match.group(1).strip()
            current_ref['volume'] = journal_match.group(2).strip()
            current_ref['pages'] = journal_match.group(3).strip()
            current_ref['year'] = journal_match.group(4).strip()
        
        # Try to extract title (between authors and journal)
        # Title is usually between the first period and the journal name
        if not current_ref['title']:
            title_match = re.search(r'\.\s+([^\.]+(?:\.[^\.]+)*?)\.\s+[A-Z]', current_ref['full_text'])
            if title_match:
                potential_title = title_match.group(1).strip()
                # Filter out common non-title patterns
                if len(potential_title) > 10 and not re.match(r'^[A-Z]\.', potential_title):
                    current_ref['title'] = potential_title

# Don't forget the last reference
if current_ref and current_ref.get('is_review'):
    review_articles.append(current_ref)

# Now let's do a more comprehensive search by looking at all references
# and checking each one for review indicators
all_refs = []
current_ref_text = ""
collecting = False

for line in lines:
    line = line.strip()
    
    if not line or line in ['Article', 'CAS', 'PubMed', 'Google Scholar', 'References']:
        continue
    
    if re.match(r'^\d+[,\d]*$', line) or line.startswith('Download references'):
        if collecting and current_ref_text:
            all_refs.append(current_ref_text)
            current_ref_text = ""
            collecting = False
        continue
    
    # Check if this looks like the start of a reference
    if re.match(r'^[A-Z][a-z]+.*,.*[A-Z]\.', line) or re.match(r'^[A-Z][a-z]+.*et al\.', line):
        if collecting and current_ref_text:
            all_refs.append(current_ref_text)
        current_ref_text = line
        collecting = True
    elif collecting:
        current_ref_text += " " + line

# Add the last one
if collecting and current_ref_text:
    all_refs.append(current_ref_text)

# Now check each reference for review indicators
review_articles_comprehensive = []

for ref_text in all_refs:
    is_review = False
    review_reason = ""
    
    # Check for review journal patterns
    if re.search(r'Nat\. Rev\.', ref_text):
        is_review = True
        review_reason = "Nature Reviews journal"
    elif re.search(r'Annu\. Rev\.', ref_text):
        is_review = True
        review_reason = "Annual Review journal"
    elif re.search(r'Trends\s+[A-Z]', ref_text):
        is_review = True
        review_reason = "Trends journal"
    elif re.search(r'This.*review|extensive review|reviewed elsewhere', ref_text, re.IGNORECASE):
        is_review = True
        review_reason = "Explicitly marked as review"
    
    if is_review:
        # Parse the reference more carefully
        # Pattern: Authors. Title. Journal Volume, Pages (Year)
        # Extract authors (everything up to first period)
        author_match = re.match(r'^([^\.]+)\.', ref_text)
        authors = author_match.group(1).strip() if author_match else ""
        
        # Extract title - between authors and journal
        # Look for pattern: Authors. Title. Journal
        title_match = re.search(r'^[^\.]+\.\s+([^\.]+(?:\.[^\.]+)*?)\.\s+(?:Nat\.|Annu\.|Trends|Mol\.|Cell|Genet|Biol|Med|Methods)', ref_text)
        title = ""
        if title_match:
            potential_title = title_match.group(1).strip()
            # Clean up title - remove common suffixes
            potential_title = re.sub(r'\s+(CAS|PubMed|Google Scholar).*$', '', potential_title)
            if len(potential_title) > 10 and not re.match(r'^[A-Z]\.\s+[A-Z]\.', potential_title):
                title = potential_title
        
        # Extract journal, volume, pages, year
        # Pattern for standard citations: Journal Volume, Pages (Year)
        journal_match = re.search(r'\.\s+((?:Nat\.\s+Rev\.|Annu\.\s+Rev\.|Trends)\s+[^\.]+?)\.?\s+(\d+)[,\s]+([^\s\(]+)\s+\((\d{4})\)', ref_text)
        journal = ""
        volume = ""
        pages = ""
        year = ""
        
        if journal_match:
            journal = journal_match.group(1).strip()
            volume = journal_match.group(2).strip()
            pages = journal_match.group(3).strip()
            year = journal_match.group(4).strip()
        else:
            # Try alternative pattern for DOI references
            doi_match = re.search(r'\.\s+((?:Nat\.\s+Rev\.|Annu\.\s+Rev\.|Trends)\s+[^\.]+?)\.?\s+https?://', ref_text)
            if doi_match:
                journal = doi_match.group(1).strip()
            year_match = re.search(r'\((\d{4})\)', ref_text)
            if year_match:
                year = year_match.group(1)
        
        review_articles_comprehensive.append({
            'authors': authors,
            'title': title,
            'journal': journal,
            'volume': volume,
            'pages': pages,
            'year': year,
            'full_citation': ref_text,
            'review_reason': review_reason
        })

# Write to CSV
output_file = "/Users/simonwang/Documents/Usage/AIagent4bio/lab1/demo/review_articles.csv"

with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['authors', 'title', 'journal', 'volume', 'pages', 'year', 'full_citation', 'review_reason']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for article in review_articles_comprehensive:
        writer.writerow(article)

print(f"Found {len(review_articles_comprehensive)} review articles")
print(f"CSV file saved to: {output_file}")

