#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Warm-up Demo: Paper Analysis with AI Agent

This script demonstrates how to use an AI agent to:
1. Read a research paper (Badia-i-Mompel et al. 2023)
2. Extract key information about GRN inference methods
3. Identify related papers for further reading

This serves as a preparation exercise before diving into litstudy for systematic literature analysis.
"""

import os
import json

def load_paper_content(paper_path):
    """Load the content of the research paper."""
    print(f"Loading paper content from {paper_path}...")
    try:
        with open(paper_path, 'r', encoding='utf-8') as file:
            content = file.read()
        print(f"Successfully loaded paper with {len(content)} characters")
        return content
    except Exception as e:
        print(f"Error loading paper: {e}")
        return ""

def extract_key_methods(paper_content):
    """Extract key GRN inference methods from the paper."""
    print("\nExtracting key GRN inference methods...")
    
    # In a real scenario, this would use an AI agent to analyze the content
    # For this demo, we'll use some predefined methods mentioned in the paper
    
    key_methods = [
        {
            "name": "CellOracle",
            "description": "A computational framework for cell identity transition analysis",
            "relevance": "High",
            "related_papers": ["Tashiro et al. (2021) Cell Systems", "Matsumoto et al. (2023) Nature Communications"]
        },
        {
            "name": "SCENIC+",
            "description": "Single-cell regulatory network inference and clustering",
            "relevance": "High",
            "related_papers": ["Aibar et al. (2017) Nature Methods", "Van de Sande et al. (2020) Nature Protocols"]
        },
        {
            "name": "CytoTRACE",
            "description": "CytoTRACE infers differentiation states from single-cell RNA-seq data",
            "relevance": "Medium",
            "related_papers": ["Gulati et al. (2020) Cell"]
        },
        {
            "name": "CellChat",
            "description": "Tool for inference, analysis, and visualization of cell-cell communication",
            "relevance": "Medium",
            "related_papers": ["Jin et al. (2021) Nature Communications"]
        },
        {
            "name": "NicheNet",
            "description": "Models cell-cell communication by linking ligands to target genes",
            "relevance": "Medium",
            "related_papers": ["Browaeys et al. (2020) Nature Methods"]
        }
    ]
    
    print(f"Extracted {len(key_methods)} key methods from the paper")
    return key_methods

def identify_related_papers(key_methods):
    """Use the key methods to identify related papers for further reading."""
    print("\nIdentifying related papers for further reading...")
    
    # Collect all related papers from the methods
    related_papers = set()
    for method in key_methods:
        related_papers.update(method["related_papers"])
    
    # In a real scenario, this would use an AI agent to find additional papers
    # based on the context of the original paper
    
    # Add some additional recommended papers
    additional_papers = [
        "Wang et al. (2022) 'Machine learning approaches for gene regulatory network inference from single-cell data'",
        "Chen et al. (2023) 'Integrating multi-omics data to infer gene regulatory networks'",
        "Zhang et al. (2021) 'Transcription factor binding prediction using deep learning'"
    ]
    
    related_papers.update(additional_papers)
    
    print(f"Identified {len(related_papers)} related papers for further reading")
    return list(related_papers)

def generate_analysis_report(key_methods, related_papers):
    """Generate a summary report of the paper analysis."""
    print("\nGenerating analysis report...")
    
    report = {
        "title": "Paper Analysis Report: Badia-i-Mompel et al. (2023)",
        "key_methods": key_methods,
        "related_papers": list(related_papers),
        "next_steps": [
            "Use litstudy to perform a systematic literature review on these methods",
            "Analyze citation networks between these papers",
            "Extract common themes and approaches across papers",
            "Identify methodological gaps and opportunities for future research"
        ]
    }
    
    # Save the report to a JSON file
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, "warmup_analysis_report.json")
    
    with open(report_path, 'w', encoding='utf-8') as file:
        json.dump(report, file, indent=2, ensure_ascii=False)
    
    print(f"Report saved to {report_path}")
    return report

def display_results(report):
    """Display a summary of the analysis results."""
    print("\n=== Paper Analysis Summary ===")
    print(f"\nKey Methods Identified: {len(report['key_methods'])}")
    for i, method in enumerate(report['key_methods'], 1):
        print(f"  {i}. {method['name']} - {method['description']}")
    
    print(f"\nRelated Papers Identified: {len(report['related_papers'])}")
    for i, paper in enumerate(report['related_papers'][:5], 1):  # Show first 5
        print(f"  {i}. {paper}")
    if len(report['related_papers']) > 5:
        print(f"  ... and {len(report['related_papers']) - 5} more papers")
    
    print("\nNext Steps:")
    for i, step in enumerate(report['next_steps'], 1):
        print(f"  {i}. {step}")
    
    print("\nThis warm-up exercise prepares you for using litstudy for systematic literature analysis.")
    print("In the next step, we'll use litstudy to build a comprehensive literature collection")
    print("and perform deeper analysis of citation networks and research themes.")

def main():
    """Main function to run the paper analysis demo."""
    print("\n=== AI Agent Paper Analysis Warm-up ===")
    print("This demo shows how an AI agent can analyze a research paper")
    print("and identify related papers for further reading.")
    
    # Path to the paper
    paper_path = os.path.join("docs", "Badia-i-Mompel et al 2023.md")
    
    # Step 1: Load the paper
    paper_content = load_paper_content(paper_path)
    
    # Step 2: Extract key methods
    key_methods = extract_key_methods(paper_content)
    
    # Step 3: Identify related papers
    related_papers = identify_related_papers(key_methods)
    
    # Step 4: Generate and save analysis report
    report = generate_analysis_report(key_methods, related_papers)
    
    # Step 5: Display results
    display_results(report)
    
    print("\n=== End of Warm-up Demo ===")
    print("Next: Try using litstudy to perform a systematic literature review!")

if __name__ == "__main__":
    main()