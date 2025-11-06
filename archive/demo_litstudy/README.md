# AI Agent for Bioinformatics: Demo Scripts

This directory contains demo scripts that showcase how to use two key tools for bioinformatics research:

1. **litstudy** - A Python package for systematic literature analysis
2. **motifmatchr** - An R package for transcription factor binding site analysis

Additionally, we've included a warm-up demo that shows how to use an AI agent to analyze research papers before diving into the more specialized tools.

## Demo Scripts

### 1. Warm-up Paper Analysis
**File:** `warmup_paper_analysis.py`

This script demonstrates how to use an AI agent to:
- Read a research paper (Badia-i-Mompel et al. 2023)
- Extract key information about GRN inference methods
- Identify related papers for further reading

This serves as preparation before using the more advanced tools.

### 2. LitStudy Demo
**File:** `litstudy_demo.py`

This script demonstrates how to use the litstudy Python package to:
- Search for academic papers related to gene regulatory networks
- Fetch and analyze paper metadata
- Generate visualizations of research trends
- Create a paper collection for further analysis

Note: The demo can run with mock data if litstudy is not installed, but for full functionality, you should install the package.

### 3. Motifmatchr Demo
**File:** `motifmatchr_demo.R`

This script demonstrates how to use the motifmatchr R package to:
- Load DNA sequence data
- Fetch transcription factor motif databases
- Identify transcription factor binding sites
- Visualize and analyze motif matches

Note: Similar to the litstudy demo, this script includes mock data for demonstration purposes.

## Installation Requirements

### For LitStudy Demo

```bash
# Install litstudy package
pip install litstudy

# Optional: Install additional packages for full functionality
pip install pandas matplotlib networkx
```

For more information about litstudy, visit the official GitHub repository:
[https://github.com/NLeSC/litstudy](https://github.com/NLeSC/litstudy)

### For Motifmatchr Demo

```r
# Install BiocManager if not already installed
if (!requireNamespace("BiocManager", quietly = TRUE)) {
    install.packages("BiocManager")
}

# Install required packages
BiocManager::install(c('motifmatchr', 'GenomicRanges', 'BiocParallel', 
                      'JASPAR2020', 'TFBSTools', 'BSgenome.Hsapiens.UCSC.hg38'))
```

For more information about motifmatchr, visit the official GitHub repository:
[https://github.com/GreenleafLab/motifmatchr](https://github.com/GreenleafLab/motifmatchr)

## Running the Demos

### Python Demos

```bash
# Navigate to the demos directory
cd demos

# Run the warm-up demo
python warmup_paper_analysis.py

# Run the litstudy demo
python litstudy_demo.py
```

### R Demo

```bash
# Run the motifmatchr demo
Rscript motifmatchr_demo.R
```

## Output Files

All demos will save their output files to the `outputs/` directory, which will be created if it doesn't exist. The outputs include:

- Analysis reports in JSON format
- Paper collections in CSV format
- Motif analysis results

## Workflow Suggestion

1. Start with the warm-up demo to understand how to analyze research papers
2. Move to the litstudy demo to perform systematic literature analysis
3. Use the motifmatchr demo to analyze transcription factor binding sites
4. Combine insights from both specialized tools for comprehensive research

## Notes

- The demos are designed to be educational and demonstrate the core functionality of each tool
- For real research applications, you would typically use additional features and customize the workflows
- Both demos include error handling and can run with mock data if the required packages are not installed

## Next Steps

After exploring these demos, you might want to:

1. Use your own research papers with the warm-up demo
2. Configure the litstudy demo to search specific academic databases
3. Apply the motifmatchr demo to your own genomic regions of interest
4. Combine the tools in a pipeline for end-to-end analysis

## Additional Resources

- [litstudy Documentation](https://github.com/NLeSC/litstudy/wiki)
- [motifmatchr Documentation](https://bioconductor.org/packages/release/bioc/html/motifmatchr.html)
- [JASPAR Database](http://jaspar.genereg.net/)