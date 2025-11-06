# AI Agent Demo Plan for November 7th Workshop

## Overview
This document outlines a practical demonstration of how AI agents can seamlessly integrate literature analysis with computational bioinformatics workflows, using the Badia-i-Mompel et al. (2023) paper as a case study.

## Demo Repositories Cloned
- ✅ **litstudy** (Python): `/workspaces/Agent4BioPhD/litstudy/`
- ✅ **motifmatchr** (R): `/workspaces/Agent4BioPhD/motifmatchr/`

## Demo Structure (60 minutes)

### Part 1: Introduction (5 minutes)
**Objective**: Show the challenge of switching between reading papers and implementing methods

**Traditional Workflow Problems**:
- Reading a paper in PDF viewer
- Switching to browser to search for tools
- Copy-pasting code snippets
- Manually installing packages
- Trial-and-error debugging
- Lost context between tasks

**AI Agent Solution**: Stay in one IDE, agent handles everything

---

### Part 2: Literature Analysis with AI Agent + litstudy (20 minutes)

#### Demo 2.1: Automated Paper Analysis
**Task**: Extract key information from Badia-i-Mompel paper

**AI Agent Actions**:
1. Read the paper markdown file
2. Extract:
   - Key methods mentioned (WGCNA, GENIE3, GRNBoost2)
   - Tools and databases (ChIP-seq, ATAC-seq, motifmatchr)
   - Important citations
3. Generate structured summary

**Command to Agent**:
```
"Read the Badia-i-Mompel paper and create a structured summary of:
1. Main computational methods for GRN inference
2. All bioinformatics tools mentioned
3. Key databases referenced
4. Top 5 most cited papers"
```

#### Demo 2.2: Literature Network Analysis
**Task**: Use litstudy to analyze citation networks related to gene regulatory networks

**AI Agent Actions**:
1. Explore litstudy example notebook
2. Adapt code to search for papers on "gene regulatory networks" and "single-cell"
3. Generate citation network visualization
4. Identify most influential papers and authors

**Command to Agent**:
```
"Using litstudy, create a Python script that:
1. Searches for papers on 'gene regulatory networks' from 2020-2023
2. Analyzes citation patterns
3. Identifies top 10 most cited papers
4. Creates a co-authorship network visualization"
```

**Expected Output**:
- Python script generated automatically
- Packages installed automatically
- Visualizations saved to `/workspaces/Agent4BioPhD/outputs/`

---

### Part 3: Domain-Specific Bioinformatics Analysis (25 minutes)

#### Demo 3.1: Understanding motifmatchr from Paper Context
**Task**: Extract motif matching information from the paper and explore motifmatchr

**AI Agent Actions**:
1. Search paper for references to motif matching (Box 1 in paper)
2. Identify motifmatchr as a key tool
3. Read motifmatchr README and vignette
4. Explain how motifmatchr relates to the paper's methods

**Command to Agent**:
```
"In the Badia-i-Mompel paper, find all references to transcription factor binding motif analysis. 
Then explore the motifmatchr repository and explain how this tool implements the concepts 
discussed in the paper."
```

#### Demo 3.2: Generate Motif Analysis Workflow
**Task**: Create an R workflow for TF motif analysis

**AI Agent Actions**:
1. Study motifmatchr documentation
2. Generate example R script for:
   - Loading example motifs
   - Defining genomic regions
   - Running motif matching
   - Visualizing results
3. Add comments explaining each step in context of the paper

**Command to Agent**:
```
"Create an R script using motifmatchr that demonstrates transcription factor motif matching 
as described in the Badia-i-Mompel paper. Include:
1. Example genomic regions (ATAC-seq peaks)
2. Load TF binding motifs from JASPAR
3. Run motif matching
4. Generate summary statistics
5. Visualize top matches"
```

**Expected Output**:
- Complete R script with extensive comments
- Installation commands for required packages
- Example output interpretation

#### Demo 3.3: Integrated Workflow
**Task**: Combine literature search with computational analysis

**AI Agent Actions**:
1. Use litstudy to find papers that cite motifmatchr
2. Extract methods from those papers
3. Generate a comparative analysis script
4. Create a summary report

**Command to Agent**:
```
"Create an integrated workflow that:
1. Uses litstudy to find recent papers citing motifmatchr
2. Extracts common use cases from their abstracts
3. Generates a report comparing different applications
4. Creates example code for the top 3 use cases"
```

---

### Part 4: Agent Capabilities Showcase (10 minutes)

#### Demo 4.1: Rapid Prototyping
**Show how agent can**:
- Read documentation instantly
- Generate working code without manual typing
- Install dependencies automatically
- Debug errors in real-time
- Adapt code to different data formats

#### Demo 4.2: Cross-Language Integration
**Task**: Bridge Python (litstudy) and R (motifmatchr)

**Command to Agent**:
```
"Create a workflow where:
1. Python script uses litstudy to find papers on ATAC-seq peak analysis
2. Extract genomic coordinates from paper supplementary data
3. Save coordinates in a format readable by R
4. R script uses motifmatchr to analyze these peaks
5. Python script visualizes the final results"
```

#### Demo 4.3: Documentation Generation
**Task**: Auto-generate workshop documentation

**Command to Agent**:
```
"Create a tutorial document explaining:
1. How to install both litstudy and motifmatchr
2. Step-by-step workflow from literature search to motif analysis
3. Common pitfalls and solutions
4. Further resources and citations"
```

---

## Key Messages to Convey

### What AI Agents Can Do:
✅ **Read and understand** scientific papers in the workspace
✅ **Navigate** complex codebases and documentation
✅ **Generate** working code from natural language descriptions
✅ **Install** and configure tools automatically
✅ **Debug** errors using documentation and code context
✅ **Integrate** multiple tools and languages seamlessly
✅ **Create** documentation and tutorials
✅ **Maintain context** across all tasks - no switching needed

### What Makes This Powerful for Bioinformatics:
- Papers often describe methods but lack implementation details
- Tools are scattered across languages (R, Python, Perl, etc.)
- Documentation is spread across README files, vignettes, papers
- AI agents can synthesize all this information instantly
- Reduces time from "reading about a method" to "trying it out"

---

## Technical Requirements

### Software:
- VS Code with GitHub Copilot
- Python 3.7+ (for litstudy)
- R 4.0+ (for motifmatchr)
- Git

### Python Packages:
```bash
pip install litstudy pandas matplotlib networkx
```

### R Packages:
```r
install.packages("devtools")
devtools::install_github("GreenleafLab/motifmatchr")
BiocManager::install(c("GenomicRanges", "TFBSTools", "BSgenome.Hsapiens.UCSC.hg19"))
```

### Workshop Repository Contents:
```
Agent4BioPhD/
├── docs/
│   ├── Badia-i-Mompel et al 2023.md
│   ├── abstractNov7.md
│   └── posterNov7.md
├── litstudy/
├── motifmatchr/
├── scripts/          # AI-generated scripts will go here
├── outputs/          # Visualizations and results
└── README.md
```

---

## Participant Hands-On Activities

### Beginner Level:
1. Ask agent to explain a specific method from the paper
2. Have agent generate a simple literature search
3. Modify agent-generated code with guidance

### Intermediate Level:
1. Ask agent to compare two methods from the paper
2. Generate custom analysis scripts
3. Integrate tools in a mini-pipeline

### Advanced Level:
1. Design complex multi-step workflows
2. Adapt methods to novel datasets
3. Create reproducible research pipelines

---

## Expected Outcomes

By the end of the workshop, participants will:
1. Understand how AI agents work within IDEs
2. See practical examples of literature-to-code workflows
3. Gain experience with litstudy and motifmatchr
4. Appreciate the efficiency gains in research workflows
5. Have working examples they can adapt for their research

---

## Demo Script Checklist

- [ ] Test all AI agent commands beforehand
- [ ] Prepare fallback code snippets if agent is slow
- [ ] Have example outputs ready to show
- [ ] Create "what could go wrong" scenarios
- [ ] Prepare Q&A about agent limitations
- [ ] Show version control of agent-generated code
- [ ] Demonstrate debugging with agent help

---

## Follow-Up Resources

1. Workshop repository: https://github.com/tesolchina/Agent4BioPhD
2. litstudy documentation: https://nlesc.github.io/litstudy/
3. motifmatchr documentation: https://greenleaflab.github.io/motifmatchr/
4. Original paper: Badia-i-Mompel et al. (2023) Nature Reviews Genetics
5. GitHub Copilot documentation for researchers

---

## Notes for Instructor

**Timing Tips**:
- Allow 5 minutes buffer for technical issues
- Have pre-run examples ready as backup
- Keep one browser tab open with paper for reference
- Record demo for sharing afterward

**Engagement Strategies**:
- Ask participants what they'd like agent to do next
- Show both successes and failures (learning opportunities)
- Invite participants to suggest modifications in real-time
- Share common pitfalls and how agent helps solve them

**Key Talking Points**:
- Agent is a tool, not a replacement for understanding
- Always validate agent-generated code
- Use version control for all agent changes
- Agent is best for boilerplate, setup, and exploration
- Critical thinking still required for research design
