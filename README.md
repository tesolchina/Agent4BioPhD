# Agent4BioPhD

**AI Agents for Bioinformatics Research: Automating Literature Analysis and Computational Workflows**

A demonstration repository showing how IDE-embedded AI agents can transform bioinformatics research by seamlessly integrating literature analysis with computational tasks.

## 📅 Workshop Information

**Date:** November 7th, 2025  
**Time:** 1:30 PM - 2:30 PM  
**Format:** On-campus (Venue: OEE1017)  
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
├── demos/                         # Demo scripts for key tools
│   ├── warmup_paper_analysis.py   # AI agent paper analysis demo
│   ├── litstudy_demo.py           # Demo for literature analysis
│   ├── motifmatchr_demo.R         # Demo for motif matching
│   └── README.md                  # Demos documentation
├── docs/                          # Workshop documentation
│   ├── AI_Agent_Demo_Plan.md      # AI agent demonstration plan
│   ├── Badia-i-Mompel et al 2023.md    # Case study paper
│   ├── GRN_Literature_Analysis_Plan.md # Gene regulatory network analysis plan
│   ├── Hands_On_Exercises.md      # Workshop exercises
│   ├── LitStudyBriefing.md        # LitStudy package documentation
│   ├── abstractNov7.md            # Workshop abstract
│   ├── abstractPolyU.md           # PolyU workshop abstract
│   ├── posterNov7.md              # Poster abstract
│   ├── game/                      # Educational games
│   └── workshop/                  # Workshop materials
├── scripts/                       # Utility scripts
│   ├── demo1_extract_methods.py   # Paper analysis script
│   ├── demo2_motif_analysis.R     # Motif analysis script
│   └── demo2_prepare_analysis.py  # Analysis preparation script
├── outputs/                       # Results and examples
│   ├── example_peaks.bed          # Example genomic peaks
│   ├── example_peaks.csv          # Example data in CSV format
│   ├── integration_guide.md       # Integration documentation
│   └── paper_analysis_report.txt  # Analysis report output
├── DEMO_PLAN.md                   # Detailed workshop plan
└── README.md                      # This file
```

> Note: litstudy and motifmatchr are external packages that need to be installed separately (see installation instructions below).

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
install.packages("BiocManager")
BiocManager::install(c("motifmatchr", "GenomicRanges", "BiocParallel", 
                     "JASPAR2020", "TFBSTools", "BSgenome.Hsapiens.UCSC.hg38"))
```

### Running Demos

```bash
# Navigate to the demos directory
cd demos

# Run the warm-up paper analysis demo
python ../scripts/demo1_extract_methods.py

# Run the litstudy demo
python litstudy_demo.py

# Run the motifmatchr demo
Rscript motifmatchr_demo.R
```

See the [demos/README.md](demos/README.md) for more detailed information about each demo.

## 🔬 Case Study

We use the paper **"Gene regulatory network inference in the era of single-cell multi-omics"** by Badia-i-Mompel et al. (2023, *Nature Reviews Genetics*) to demonstrate:

1. **Automated Literature Analysis**: Extract computational methods, tools, and key concepts
2. **Tool Integration**: Connect literature insights with bioinformatics tools
3. **Workflow Generation**: Create executable code from paper descriptions

## 💡 Demo Examples

We've created three demonstration scripts that showcase different aspects of bioinformatics analysis:

1. **Warm-up Paper Analysis** - Demonstrates how an AI agent can analyze research papers and identify related literature.

2. **LitStudy Demo** - Shows how to use the litstudy package for systematic literature reviews and analysis of research trends.

3. **Motifmatchr Demo** - Demonstrates transcription factor binding site analysis using R's motifmatchr package.

See the [demos/README.md](demos/README.md) file for detailed instructions on running these demos.

### Demo 1: Automated Paper Analysis

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

## 🛠️ Key Tools Featured

### 1. [litstudy](https://github.com/NLeSC/litstudy) - Literature Analysis
- Python package for systematic literature reviews
- Citation network analysis
- Author collaboration networks
- Topic modeling with NLP

For detailed usage, see our [litstudy demo](demos/litstudy_demo.py) or visit the [official repository](https://github.com/NLeSC/litstudy).

### 2. [motifmatchr](https://github.com/GreenleafLab/motifmatchr) - TF Motif Matching
- R package for fast motif matching
- Uses MOODS library (C++ backend)
- Works with ATAC-seq/ChIP-seq peaks
- Integrates with JASPAR, TRANSFAC, HOCOMOCO databases

For detailed usage, see our [motifmatchr demo](demos/motifmatchr_demo.R) or visit the [official repository](https://github.com/GreenleafLab/motifmatchr)

## 🎯 Learning Objectives

By using this repository, you will learn to:

1. Use AI agents to analyze research papers and identify related literature
2. Perform systematic literature reviews using litstudy
3. Analyze transcription factor binding sites using motifmatchr
4. Integrate insights from literature and motif analysis for bioinformatics research
5. Combine Python and R tools in a comprehensive workflow

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
