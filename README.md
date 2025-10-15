# Agent4BioPhD

**AI Agents for Bioinformatics Research: Automating Literature Analysis and Computational Workflows**

A demonstration repository showing how IDE-embedded AI agents can transform bioinformatics research by seamlessly integrating literature analysis with computational tasks.

## 📅 Workshop Information

**Date:** November 7th, 2025  
**Time:** 1:30 PM - 2:30 PM  
**Format:** Online  
**Speaker:** Dr. Simon Wang, HKBU

## 🎯 Overview

This workshop demonstrates how AI agents can:
- 📚 Analyze scientific literature automatically
- 🧬 Generate bioinformatics analysis code
- 🔗 Bridge the gap between reading papers and implementing methods
- ⚡ Eliminate context-switching between tools and environments

## 📁 Repository Structure

```
Agent4BioPhD/
├── docs/                          # Workshop documentation
│   ├── Badia-i-Mompel et al 2023.md    # Case study paper
│   ├── abstractNov7.md                  # Workshop abstract
│   ├── posterNov7.md                    # Poster abstract
├── litstudy/                      # Literature analysis tool (Python)
├── motifmatchr/                   # TF motif matching tool (R)
├── scripts/                       # AI-generated demo scripts
│   └── demo1_extract_methods.py        # Automated paper analysis
├── outputs/                       # Results and visualizations
│   ├── paper_analysis_report.txt       # Generated analysis report
│   └── paper_analysis_report.json      # Structured data output
├── DEMO_PLAN.md                   # Detailed workshop plan
└── README.md                      # This file
```

## 🚀 Quick Start

### Prerequisites

1. **Create a GitHub account** (if you don't have one)
2. **Fork this repository**
3. **Install required software:**
   - Python 3.7+
   - R 4.0+
   - VS Code with GitHub Copilot

### Installation

#### Python Setup (for litstudy)
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/Agent4BioPhD.git
cd Agent4BioPhD

# Install Python dependencies
pip install litstudy pandas matplotlib networkx
```

#### R Setup (for motifmatchr)
```r
# In R console
install.packages("devtools")
devtools::install_github("GreenleafLab/motifmatchr")

# Install Bioconductor packages
if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install(c("GenomicRanges", "TFBSTools", "BSgenome.Hsapiens.UCSC.hg19"))
```

## 🔬 Case Study

We use the paper **"Gene regulatory network inference in the era of single-cell multi-omics"** by Badia-i-Mompel et al. (2023, *Nature Reviews Genetics*) to demonstrate:

1. **Automated Literature Analysis**: Extract computational methods, tools, and key concepts
2. **Tool Integration**: Connect literature insights with bioinformatics tools
3. **Workflow Generation**: Create executable code from paper descriptions

## 💡 Demo Examples

### Demo 1: Automated Paper Analysis (Already Run!)

Check out the generated report: `outputs/paper_analysis_report.txt`

**What the AI agent did:**
- ✅ Read the entire Badia-i-Mompel paper (1,803 lines)
- ✅ Identified 7 GRN inference methods
- ✅ Found 7 bioinformatics tools (including motifmatchr!)
- ✅ Extracted 7 databases and 9 experimental technologies
- ✅ Counted mentions: "single-cell" appears 104 times!
- ✅ Generated structured report in both TXT and JSON formats

**Try it yourself:**
```bash
python scripts/demo1_extract_methods.py
```

### Demo 2: Literature Network Analysis (Coming Soon)
Use `litstudy` to analyze citation networks related to gene regulatory networks.

### Demo 3: Motif Analysis Workflow (Coming Soon)
Generate R code using `motifmatchr` for transcription factor binding site prediction.

## 🛠️ Key Tools Featured

### 1. [litstudy](https://github.com/NLeSC/litstudy) - Literature Analysis
- Python package for systematic literature reviews
- Citation network analysis
- Author collaboration networks
- Topic modeling with NLP

### 2. [motifmatchr](https://github.com/GreenleafLab/motifmatchr) - TF Motif Matching
- R package for fast motif matching
- Uses MOODS library (C++ backend)
- Works with ATAC-seq/ChIP-seq peaks
- Integrates with JASPAR, TRANSFAC, HOCOMOCO databases

## 📊 What Makes AI Agents Powerful?

| Traditional Workflow | With AI Agent |
|---------------------|---------------|
| Read paper in PDF viewer | Agent reads markdown file directly |
| Google for tools manually | Agent knows tools from context |
| Copy-paste code snippets | Agent generates complete scripts |
| Debug errors via Stack Overflow | Agent debugs using documentation |
| Switch between 5+ applications | Stay in one IDE |
| Manual note-taking | Auto-generated reports |

## 🎓 Learning Objectives

By the end of this workshop, you will:
- ✅ Understand how AI agents work within IDEs
- ✅ See practical literature-to-code workflows
- ✅ Gain hands-on experience with litstudy and motifmatchr
- ✅ Appreciate efficiency gains in research workflows
- ✅ Have working examples to adapt for your research

## 📚 Additional Resources

- **Workshop Plan**: See [DEMO_PLAN.md](DEMO_PLAN.md) for detailed demo structure
- **litstudy docs**: https://nlesc.github.io/litstudy/
- **motifmatchr docs**: https://greenleaflab.github.io/motifmatchr/
- **Original Paper**: Badia-i-Mompel et al. (2023) [Nature Reviews Genetics](https://www.nature.com/articles/s41576-023-00618-5)

## 🤝 Contributing

This is a workshop repository! Feel free to:
- Try the demos and share your results
- Suggest additional demos or use cases
- Report issues or ask questions
- Fork and adapt for your own research

## 📧 Contact

**Dr. Simon Wang**  
Lecturer in English and Innovation Officer  
The Language Centre, Hong Kong Baptist University

- Email: simonwang@hkbu.edu.hk
- GitHub: [@tesolchina](https://github.com/tesolchina)

## 📄 License

See [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **litstudy** team at Netherlands eScience Center
- **motifmatchr** developers at Greenleaf Lab, Stanford
- Badia-i-Mompel et al. for the excellent review paper
- GitHub Copilot for AI assistance

---

**Ready to experience the power of AI agents in bioinformatics research?** 🚀

Fork this repo and let's get started! 
