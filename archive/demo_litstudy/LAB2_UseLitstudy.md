# Lab 2: Use litstudy

## Lab: Use litstudy

### Input: 
- File path: `lab2/data/Badia-i-Mompel et al 2023.md` (research paper in markdown format)
- Folder path: `lab2/data/` (for storing paper collections and search results)

### Process: 
Instructions for AI agents on how to process the input:

1. **Install and Setup litstudy**:
   - Check if litstudy is installed: `pip list | grep litstudy`
   - If not installed, install it: `pip install litstudy pandas matplotlib networkx`
   - Verify installation by importing the library

2. **Paper Collection from Existing Data**:
   - Read the Badia-i-Mompel paper from `lab2/data/Badia-i-Mompel et al 2023.md`
   - Extract key terms, methods, and concepts mentioned in the paper
   - Use litstudy to search for related papers based on these terms
   - Create a paper collection using litstudy's Collection class

3. **Literature Search and Analysis**:
   - Search for papers on "gene regulatory networks" and "single-cell" from 2020-2023
   - Collect metadata: title, authors, year, venue, abstract
   - Build a citation network to identify influential papers
   - Analyze co-authorship patterns
   - Identify top-cited papers in the collection

4. **Visualization and Reporting**:
   - Generate visualizations of:
     - Research trends over time (publication timeline)
     - Citation network graph
     - Co-authorship network
     - Topic distribution
   - Export paper collection to CSV format
   - Create a summary report with key findings

5. **Integration with AI Agent**:
   - Have the agent read litstudy documentation to understand advanced features
   - Generate code for custom analysis queries
   - Debug any errors that occur during the process
   - Adapt the workflow for different research questions

### Output: 
Designate folder path (and file paths) where the output could be delivered:

- Folder: `lab2/practice/`
  - `paper_collection.csv` - Exported paper collection with metadata
  - `citation_network.png` - Visualization of citation relationships
  - `coauthorship_network.png` - Visualization of author collaborations
  - `research_trends.png` - Timeline visualization of publications
  - `litstudy_analysis_report.txt` - Summary report of findings
  - `litstudy_analysis_report.json` - Structured data output

### Reflection Notes: 
What we learn through this lab:

- **Systematic Literature Review**: Understand how to use litstudy for systematic literature analysis
- **Citation Networks**: Learn to analyze relationships between papers through citations
- **Metadata Extraction**: See how bibliographic data can be automatically collected and structured
- **Research Trends**: Discover how to identify patterns and trends in scientific literature
- **AI Agent Integration**: Experience how agents can help with package installation, documentation reading, and code generation
- **Workflow Automation**: Learn to automate literature search and analysis tasks
- **Data Export**: Understand how to export and share literature analysis results

**Key Takeaways**:
- litstudy provides powerful tools for literature analysis that would be tedious to implement manually
- AI agents can help navigate package documentation and generate working code
- Citation networks reveal important connections between research papers
- Systematic approaches to literature review are more comprehensive than ad-hoc searches
- This workflow can be adapted for any research topic requiring literature analysis


