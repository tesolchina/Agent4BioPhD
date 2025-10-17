# Plan to Demo LitStudy Using Badia-i-Mompel et al 2023 Paper

## 1. Demo Overview

This plan outlines how to use the `litstudy` Python package to analyze the paper "Gene regulatory network inference in the era of single-cell multi-omics" by Badia-i-Mompel et al (2023) and demonstrate key functionalities of systematic literature analysis.

## 2. Setup and Preparation

### 2.1 Required Resources
- The paper file: `/Users/simonwang/Documents/Usage/AIagent4bio/docs/Badia-i-Mompel et al 2023.md`
- A modified version of `litstudy_demo.py` that focuses on this specific paper
- Output directory for storing analysis results

### 2.2 Environment Requirements
- Python 3.6+
- `litstudy` package (or mock implementation if not available)
- Basic Python libraries: os, sys, datetime, json

## 3. Demo Implementation Steps

### Step 1: Paper Processing and Collection Creation
1. Read and parse the Badia-i-Mompel paper markdown file
2. Extract key metadata: title, authors, journal, publication year, abstract
3. Create a `litstudy.Collection` object with this paper as the primary entry
4. Add relevant metadata extracted from the paper

### Step 2: Paper Content Analysis
1. Extract key sections and subsections from the paper
2. Identify main topics and concepts (GRN inference, single-cell multi-omics, etc.)
3. Create a structured representation of the paper's content

### Step 3: Citation and Impact Analysis
1. Extract citation information from the paper metadata (293 citations mentioned)
2. Analyze the paper's impact based on the information available
3. Identify key works cited within the paper that might be relevant for follow-up

### Step 4: Topic Extraction and Categorization
1. Extract key methodologies mentioned (GENIE3, GRNBoost2, ATAC-seq, etc.)
2. Identify main application areas and biological contexts
3. Categorize the paper within the broader scientific literature

### Step 5: Visualization and Reporting
1. Create a structured report focusing on this specific paper
2. Generate visual representations of key concepts and relationships
3. Export the analysis results to a JSON file

## 4. Demo Script Implementation

### 4.1 Paper-Specific Functions
- `parse_paper_markdown()` - Extract metadata and content from the paper file
- `create_paper_collection()` - Create a collection centered on the Badia-i-Mompel paper
- `analyze_paper_content()` - Perform deeper analysis of the paper's sections

### 4.2 Modified Workflow
1. Replace the general search function with targeted paper loading
2. Add paper-specific analysis functions
3. Focus reporting on the specific paper rather than general trends

## 5. Expected Outputs

1. A JSON report file with structured analysis of the paper
2. A CSV file with the paper details
3. Console output showing key findings from the analysis
4. A summary of how litstudy can be used for focused paper analysis

## 6. Demo Script Example

The demo will be implemented in a script named `litstudy_badia_demo.py` in the `demos` directory, with the following structure:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LitStudy Demo: Analysis of Badia-i-Mompel et al (2023) Paper

This script demonstrates how to use the litstudy Python package to:
1. Process and analyze a specific research paper
2. Extract metadata and key content
3. Create a focused report on the paper's findings
4. Demonstrate literature analysis capabilities
"""

import os
import sys
from datetime import datetime

# Check if litstudy is installed (as in the original demo)
# ...

def parse_paper_markdown(file_path):
    """Parse the markdown file to extract paper metadata and content."""
    # Implementation to extract title, authors, abstract, sections, etc.
    # ...

def create_paper_collection(paper_metadata):
    """Create a litstudy collection with the Badia-i-Mompel paper."""
    # Implementation to create and populate collection
    # ...

def analyze_paper_content(collection):
    """Perform deeper analysis of the paper's content."""
    # Implementation to extract key concepts, methodologies, etc.
    # ...

# Additional functions and main workflow
# ...
```

## 7. Demo Presentation Flow

1. **Introduction** (2 min)
   - Brief overview of litstudy package capabilities
   - Introduction to the Badia-i-Mompel paper and its significance

2. **Demo Execution** (5-7 min)
   - Run the modified script
   - Show real-time paper processing and analysis

3. **Results Explanation** (3-5 min)
   - Discuss the generated report
   - Highlight key findings from the paper analysis

4. **Next Steps** (2 min)
   - Suggest how to extend this analysis with additional papers
   - Discuss integration with other tools in the repository

## 8. Extension Possibilities

- Expand the collection with papers cited by Badia-i-Mompel et al.
- Compare this paper with other recent reviews on GRN inference
- Use the paper as a seed for a broader literature analysis on single-cell multi-omics approaches to GRN inference
- Integrate the findings with motif analysis from the motifmatchr_demo.R script

## 9. Conclusion

This demo will showcase how litstudy can be effectively used for focused analysis of a specific research paper, highlighting both the package's capabilities and the key insights from the Badia-i-Mompel et al. review on gene regulatory network inference in the single-cell era.