#!/usr/bin/env python3
# Simple LitStudy Demo
# This script demonstrates the basic concepts of litstudy without requiring installation

import os
from datetime import datetime

# Define mock classes first to avoid import issues
class MockPaper:
    """Mock implementation of litstudy's Paper class."""
    def __init__(self, title, authors, publication_year, venue, abstract=""):
        self.title = title
        self.authors = authors
        self.publication_year = publication_year
        self.venue = venue
        self.abstract = abstract

class MockCollection:
    """Mock implementation of litstudy's Collection class."""
    def __init__(self, papers=None):
        self.papers = papers or []

class MockStats:
    """Mock implementation of litstudy's Stats class."""
    def __init__(self, collection):
        self.collection = collection
        self.papers = collection.papers  # Add papers attribute to match expected structure

    @staticmethod
    def publication_years(collection):
        years = [p.publication_year for p in collection.papers]
        return {year: years.count(year) for year in set(years)}

    @staticmethod
    def top_authors(collection, limit=10):
        authors = {}
        for paper in collection.papers:
            for author in paper.authors:
                authors[author] = authors.get(author, 0) + 1
        return dict(sorted(authors.items(), key=lambda x: x[1], reverse=True)[:limit])

    @staticmethod
    def venues(collection):
        venues = [p.venue for p in collection.papers]
        return {venue: venues.count(venue) for venue in set(venues)}

class MockSearch:
    """Mock implementation of litstudy's search module."""
    @staticmethod
    def search_pubmed(query, limit=5):
        """Mock implementation of PubMed search."""
        # Create some mock papers
        papers = [
            MockPaper(
                "Inference of Gene Regulatory Networks from Single-Cell Data",
                ["Author A", "Author B"],
                2022,
                "Nature Methods",
                "This paper introduces a novel method for GRN inference..."
            ),
            MockPaper(
                "Deep Learning Approaches for GRN Inference",
                ["Author F"],
                2023,
                "Neural Networks",
                "Deep learning techniques are applied to gene regulatory..."
            ),
            MockPaper(
                "Single-Cell Transcriptomics and GRN Dynamics",
                ["Author I", "Author J", "Author K", "Author L"],
                2022,
                "Cell",
                "This study investigates dynamic changes in regulatory networks..."
            ),
            MockPaper(
                "Statistical Methods for Gene Regulatory Networks",
                ["Author C", "Author D"],
                2020,
                "Bioinformatics",
                "Statistical approaches for modeling gene regulation..."
            ),
            MockPaper(
                "Comparative Analysis of GRN Inference Methods",
                ["Author E", "Author G", "Author H"],
                2021,
                "Science",
                "A comprehensive comparison of different inference techniques..."
            )
        ]
        return MockCollection(papers)

# Now try to import litstudy, falling back to mock implementation if not available
has_litstudy = False
try:
    import litstudy
    has_litstudy = True
except ImportError:
    print("litstudy is not installed. Using mock implementation for demonstration.")
    # Create a mock module
    class MockLitStudyModule:
        pass
    
    # Create instances of our mock classes
    litstudy = MockLitStudyModule()
    litstudy.search = MockSearch()
    litstudy.Stats = MockStats

def create_collection(query="gene regulatory networks"):
    """Create a collection of papers based on a search query."""
    print(f"Creating a {'mock ' if not has_litstudy else ''}collection of papers on '{query}'...")
    
    # In a real scenario, this would use actual databases
    # For this demo, we'll use our mock implementation
    if has_litstudy:
        # Real implementation would be something like:
        # collection = litstudy.search.pubmed(query, limit=5)
        # For demonstration, we'll still use our mock
        pass
    
    # Use mock implementation for both cases for consistency
    collection = MockSearch.search_pubmed(query, limit=5)
    return collection

def analyze_collection(collection):
    """Analyze a collection of papers."""
    print("\n=== Analyzing Collection ===")
    print(f"Total papers: {len(collection.papers)}")
    
    # Publication years analysis
    stats = litstudy.Stats(collection)
    years = stats.publication_years(collection)
    print("\nPublication years:")
    for year in sorted(years.keys()):
        print(f"  {year}: {years[year]} papers")
    
    # Top authors analysis
    authors = stats.top_authors(collection)
    print("\nTop authors:")
    for author, count in authors.items():
        print(f"  {author}: {count} papers")
    
    # Publication venues analysis
    venues = stats.venues(collection)
    print("\nPublication venues:")
    for venue, count in venues.items():
        print(f"  {venue}: {count} papers")

def filter_collection(collection, min_year=2022):
    """Filter a collection to include only recent papers."""
    print(f"\n=== Filtering Collection ===")
    print(f"Filtering to show only papers from {min_year} or later...")
    
    recent_papers = [p for p in collection.papers if p.publication_year >= min_year]
    filtered_collection = MockCollection(recent_papers)
    
    print(f"Number of recent papers: {len(filtered_collection.papers)}")
    print("\nRecent papers:")
    for paper in filtered_collection.papers:
        print(f"  - {paper.title} ({paper.publication_year})")
    
    return filtered_collection

def save_collection(collection):
    """Save collection information to a simple text file."""
    # Use absolute path to outputs directory
    output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs")
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Generate timestamp for filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"litstudy_simple_demo_{timestamp}.txt"
    filepath = os.path.join(output_dir, filename)
    
    # Write collection information to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("LITSTUDY SIMPLE DEMO RESULTS\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"Total papers: {len(collection.papers)}\n\n")
        f.write("PAPER LIST:\n\n")
        
        for i, paper in enumerate(collection.papers, 1):
            f.write(f"{i}. {paper.title}\n")
            f.write(f"   Authors: {', '.join(paper.authors)}\n")
            f.write(f"   Year: {paper.publication_year}\n")
            f.write(f"   Venue: {paper.venue}\n")
            f.write(f"   Abstract: {paper.abstract}\n\n")
    
    print(f"\nCollection information saved to: {filepath}")

def main():
    """Main function to run the simple litstudy demo."""
    print("=== SIMPLE LITSTUDY DEMO ===")
    print("This demo shows the basic concepts of litstudy:")
    print("1. Creating a collection of papers")
    print("2. Analyzing the collection")
    print("3. Filtering the collection")
    print("4. Saving results")
    
    # Step 1: Create a collection
    collection = create_collection()
    
    # Step 2: Analyze the collection
    analyze_collection(collection)
    
    # Step 3: Filter the collection
    filtered_collection = filter_collection(collection)
    
    # Step 4: Save the results
    save_collection(filtered_collection)
    
    print("\n=== DEMO COMPLETED ===")
    print("\nKey Concepts Demonstrated:")
    print("1. Collection: A group of papers with metadata")
    print("2. Search: Finding papers based on keywords")
    print("3. Filtering: Selecting papers based on criteria")
    print("4. Analysis: Extracting statistics from papers")
    print("5. Export: Saving results for further use")
    
    print("\nIn a real scenario, litstudy can:")
    print("- Search multiple academic databases")
    print("- Create citation networks")
    print("- Perform topic modeling")
    print("- Generate visualizations")
    print("- Export to various formats")

if __name__ == "__main__":
    main()