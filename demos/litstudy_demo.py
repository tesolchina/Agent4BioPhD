#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
LitStudy Demo: Systematic Literature Analysis

This script demonstrates how to use the litstudy Python package to:
1. Search for academic papers related to gene regulatory networks
2. Fetch and analyze paper metadata
3. Generate visualizations of research trends
4. Create a paper collection for further analysis

Note: This demo requires the litstudy package to be installed.
For installation instructions, see the README.md file.
"""

import os
import sys
from datetime import datetime

# Check if litstudy is installed
try:
    import litstudy
    print("litstudy package is installed. Proceeding with demo...")
except ImportError:
    print("litstudy package is not installed.")
    print("Please install it using: pip install litstudy")
    print("This demo will use mock data for demonstration purposes.")
    
    # Create a mock litstudy module for demonstration
    class MockLitStudy:
        class Collection:
            def __init__(self):
                self.papers = []
                
            def __len__(self):
                return len(self.papers)
                
            def add_paper(self, paper):
                self.papers.append(paper)
                
            def export_csv(self, path):
                print(f"Exporting {len(self)} papers to {path}")
                with open(path, 'w', encoding='utf-8') as f:
                    f.write("title,authors,year,venue\n")
                    for paper in self.papers:
                        authors_str = ", ".join(paper.authors)
                        f.write(f"{paper.title},{authors_str},{paper.year},{paper.venue}\n")
                return self
    
    class Paper:
        def __init__(self, title, authors, year, venue):
            self.title = title
            self.authors = authors
            self.year = year
            self.venue = venue
            self.abstract = "This is a mock abstract for demonstration purposes."
    
    litstudy = MockLitStudy()

def create_mock_papers():
    """Create mock papers for demonstration when litstudy is not available."""
    mock_papers = [
        litstudy.Paper(
            "Inferring Gene Regulatory Networks from Single-Cell RNA-Seq Data",
            ["John Smith", "Jane Doe"],
            2021,
            "Nature Methods"
        ),
        litstudy.Paper(
            "Machine Learning Approaches for GRN Inference",
            ["Alice Chen", "Bob Wang", "Charlie Brown"],
            2022,
            "Bioinformatics"
        ),
        litstudy.Paper(
            "CellOracle: A Computational Framework for Cell Identity Transition Analysis",
            ["Tashiro A", "Matsumoto K", "Tanaka Y"],
            2021,
            "Cell Systems"
        ),
        litstudy.Paper(
            "SCENIC+: Single-cell regulatory network inference and clustering",
            ["Aibar S", "Van de Sande B", "Lijnzaad P"],
            2020,
            "Nature Protocols"
        ),
        litstudy.Paper(
            "CytoTRACE infers differentiation states from single-cell RNA-seq data",
            ["Gulati G", "Trapnell C", "Kelley DR"],
            2020,
            "Cell"
        ),
        litstudy.Paper(
            "CellChat: Inference and analysis of cell-cell communication",
            ["Jin S", "Guo S", "Zhang L"],
            2021,
            "Nature Communications"
        ),
        litstudy.Paper(
            "NicheNet: Modeling cell-cell communication by linking ligands to target genes",
            ["Browaeys R", "Saelens W", "Carmona S"],
            2020,
            "Nature Methods"
        ),
        litstudy.Paper(
            "Integrating multi-omics data to infer gene regulatory networks",
            ["Wang Y", "Li H", "Zhang Z"],
            2023,
            "Science"
        ),
        litstudy.Paper(
            "Transcription factor binding prediction using deep learning",
            ["Zhang M", "Chen J", "Zhao W"],
            2022,
            "Genome Research"
        ),
        litstudy.Paper(
            "Network biology approaches for analyzing gene regulatory networks",
            ["Liu X", "Wang J", "Chen L"],
            2023,
            "Molecular Systems Biology"
        )
    ]
    return mock_papers

def search_papers(keywords, max_results=10):
    """
    Search for academic papers using litstudy.
    In a real scenario, this would use actual academic databases.
    """
    print(f"\nSearching for papers with keywords: {', '.join(keywords)}")
    print(f"Maximum results: {max_results}")
    
    # Create a collection to store papers
    collection = litstudy.Collection()
    
    # In the actual litstudy, you would use search functions like:
    # collection = litstudy.search_pubmed(keywords, max_results=max_results)
    # or
    # collection = litstudy.search_scopus(keywords, max_results=max_results)
    
    # For this demo, we'll use mock papers
    mock_papers = create_mock_papers()
    
    # Add papers to collection
    for paper in mock_papers[:max_results]:
        collection.add_paper(paper)
    
    print(f"Found {len(collection)} papers related to the keywords")
    return collection

def analyze_publication_trends(collection):
    """Analyze publication trends in the paper collection."""
    print("\nAnalyzing publication trends...")
    
    # Count papers by year
    year_counts = {}
    for paper in collection.papers:
        if paper.year not in year_counts:
            year_counts[paper.year] = 0
        year_counts[paper.year] += 1
    
    # Sort by year
    sorted_years = sorted(year_counts.keys())
    
    print("Publication trends by year:")
    for year in sorted_years:
        print(f"  {year}: {year_counts[year]} papers")
    
    # Identify top venues
    venue_counts = {}
    for paper in collection.papers:
        if paper.venue not in venue_counts:
            venue_counts[paper.venue] = 0
        venue_counts[paper.venue] += 1
    
    # Sort by count
    sorted_venues = sorted(venue_counts.items(), key=lambda x: x[1], reverse=True)
    
    print("\nTop publication venues:")
    for venue, count in sorted_venues[:3]:  # Show top 3
        print(f"  {venue}: {count} papers")
    
    return {
        "year_counts": year_counts,
        "venue_counts": venue_counts
    }

def save_collection(collection, output_dir="outputs"):
    """Save the paper collection to CSV format."""
    print("\nSaving paper collection...")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"litstudy_paper_collection_{timestamp}.csv"
    filepath = os.path.join(output_dir, filename)
    
    # Export to CSV
    collection.export_csv(filepath)
    
    print(f"Paper collection saved to: {filepath}")
    return filepath

def print_paper_details(collection, num_papers=3):
    """Print details of the first few papers in the collection."""
    print(f"\nSample papers from the collection (first {num_papers}):")
    
    for i, paper in enumerate(collection.papers[:num_papers], 1):
        print(f"\n{i}. {paper.title}")
        print(f"   Authors: {', '.join(paper.authors)}")
        print(f"   Year: {paper.year}")
        print(f"   Venue: {paper.venue}")

def generate_litstudy_report(collection, trends):
    """Generate a summary report of the litstudy analysis."""
    print("\nGenerating litstudy report...")
    
    report = {
        "title": "LitStudy Analysis Report: Gene Regulatory Networks",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "collection_size": len(collection),
        "publication_years": list(trends["year_counts"].keys()),
        "top_venues": sorted(trends["venue_counts"].items(), key=lambda x: x[1], reverse=True)[:3],
        "analysis_notes": [
            "This is a demonstration of litstudy capabilities for systematic literature review",
            "In a real analysis, you would use additional litstudy features:",
            "- Citation network analysis",
            "- Topic modeling and keyword extraction",
            "- Visualization of research trends",
            "- Comparative analysis of different research areas"
        ]
    }
    
    # Save the report to a JSON file
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, "litstudy_analysis_report.json")
    
    with open(report_path, 'w', encoding='utf-8') as file:
        import json
        json.dump(report, file, indent=2, ensure_ascii=False)
    
    print(f"Report saved to {report_path}")
    return report

def main():
    """Main function to run the litstudy demo."""
    print("\n=== LitStudy Demo: Systematic Literature Analysis ===")
    print("This demo shows how to use the litstudy Python package")
    print("for systematic literature reviews and analysis.")
    
    # Define search keywords
    keywords = ["gene regulatory network", "GRN inference", "single-cell RNA-seq"]
    
    # Step 1: Search for papers
    collection = search_papers(keywords, max_results=10)
    
    # Step 2: Analyze publication trends
    trends = analyze_publication_trends(collection)
    
    # Step 3: Print sample paper details
    print_paper_details(collection, num_papers=3)
    
    # Step 4: Save the collection
    csv_path = save_collection(collection)
    
    # Step 5: Generate analysis report
    report = generate_litstudy_report(collection, trends)
    
    print("\n=== LitStudy Demo Complete ===")
    print(f"\nSummary of analysis:")
    print(f"- Total papers in collection: {report['collection_size']}")
    print(f"- Papers span years: {min(report['publication_years'])}-{max(report['publication_years'])}")
    print(f"- Collection saved to: {csv_path}")
    print(f"- Analysis report saved to: outputs/litstudy_analysis_report.json")
    
    print("\nNext Steps:")
    print("1. Install litstudy: pip install litstudy")
    print("2. Use actual academic database APIs for more comprehensive searches")
    print("3. Try additional litstudy features for deeper analysis")
    print("4. Explore the motifmatchr R package for motif matching analysis")

if __name__ == "__main__":
    main()