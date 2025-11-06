# Brainstorm AI agent instructions for research
_Exported on 06/11/2025 at 23:21:41 GMT+8 from Cursor (2.0.64)_

---

**User**

suppose the input is /Users/simonwang/Documents/Usage/AIagent4bio/lab2/data/Badia-i-Mompel et al 2023.md

brainstorm 10 ideas for writing AI agent instructions that can help research students writing papers in this area 

create a new md file below 

ideas should be similar to /Users/simonwang/Documents/Usage/AIagent4bio/lab1/demo/task1.md



/Users/simonwang/Documents/Usage/AIagent4bio/lab1/practice 

---

**Cursor**


Reviewing the input paper and the example task format, then drafting 10 AI agent instruction ideas for research students.



Reading the paper in sections to understand its content, and checking the existing practice file:



Reviewing more of the paper to understand its key topics:



Creating a file with 10 AI agent instruction ideas for research students writing papers in this area:


```markdown
# 10 AI Agent Instruction Ideas for GRN Paper Writing

## Task 1: Extract and Organize GRN Inference Tools
Input: /Users/simonwang/Documents/Usage/AIagent4bio/lab2/data/Badia-i-Mompel et al 2023.md
Process: Review the paper and extract all mentioned GRN inference tools/methods (e.g., SCENIC, CellOracle, FigR, etc.). For each tool, identify: (1) the tool name, (2) the data modalities it uses (transcriptomics, chromatin accessibility, or both), (3) whether it uses linear or non-linear modeling, (4) whether it uses frequentist or Bayesian statistics, and (5) any key features mentioned. Generate a CSV file with columns: Tool_Name, Data_Modalities, Modeling_Type, Statistical_Approach, Key_Features, and place it in the folder below.
Output: /Users/simonwang/Documents/Usage/AIagent4bio/lab1/practice

## Task 2: Compile TF Binding Motif Databases and Algorithms
Input: /Users/simonwang/Documents/Usage/AIagent4bio/lab2/data/Badia-i-Mompel et al 2023.md
Process: Extract information from Box 1 about TF binding motif databases and motif matcher algorithms. Create a structured CSV file listing: (1) Database/Algorithm name, (2) Type (Database or Algorithm), (3) URL, (4) Reference number, and (5) any brief description if available. Organize the data clearly with separate sections or columns to distinguish databases from algorithms.
Output: /Users/simonwang/Documents/Usage/AIagent4bio/lab1/practice

## Task 3: Identify Experimental Validation Methods
Input: /Users/simonwang/Documents/Usage/AIagent4bio/lab2/data/Badia-i-Mompel et al 2023.md
Process: Review the "Experimental assessment of GRNs" section and extract all experimental methods mentioned for validating GRN predictions. For each method, identify: (1) the method name/technology (e.g., ChIP-seq, Hi-C, CRISPR screens), (2) what aspect of GRN it validates (TF binding, CRE activity, gene linkage, etc.), (3) any key databases or resources mentioned, and (4) advantages/limitations if discussed. Generate a CSV file with these details.
Output: /Users/simonwang/Documents/Usage/AIagent4bio/lab1/practice

## Task 4: Extract Downstream Analysis Applications
Input: /Users/simonwang/Documents/Usage/AIagent4bio/lab2/data/Badia-i-Mompel et al 2023.md
Process: Review the "Downstream GRN analyses" section and Box 2. Extract all downstream analysis types (topological analysis, comparative analysis, TF activity inference, perturbation experiments) and their applications. For each application example mentioned in Box 2, extract: (1) the biological context, (2) the tools/methods used, (3) key findings, and (4) experimental validation if mentioned. Create a structured document or CSV summarizing these applications.
Output: /Users/simonwang/Documents/Usage/AIagent4bio/lab1/practice

## Task 5: List Challenges and Future Directions
Input: /Users/simonwang/Documents/Usage/AIagent4bio/lab2/data/Badia-i-Mompel et al 2023.md
Process: Review the "Challenges and future directions" section. Extract each major challenge or future direction mentioned (e.g., integrating transcription and accessibility, scale and sparsity, 3D genome structure, benchmarking, etc.). For each, identify: (1) the challenge/direction name, (2) a brief description, (3) current limitations, (4) proposed solutions or emerging technologies, and (5) any specific tools or methods mentioned. Generate a markdown or CSV file organizing this information.
Output: /Users/simonwang/Documents/Usage/AIagent4bio/lab1/practice

## Task 6: Extract Key Methodological Comparisons
Input: /Users/simonwang/Documents/Usage/AIagent4bio/lab2/data/Badia-i-Mompel et al 2023.md
Process: Review the paper to identify comparisons between different methodological approaches (e.g., bulk vs single-cell, transcriptomics-only vs multi-omics, linear vs non-linear modeling, frequentist vs Bayesian). For each comparison, extract: (1) the compared approaches, (2) advantages of each, (3) limitations of each, (4) when to use which approach, and (5) any quantitative assessments if mentioned. Create a comparison table in CSV or markdown format.
Output: /Users/simonwang/Documents/Usage/AIagent4bio/lab1/practice

## Task 7: Compile Reference Articles by Category
Input: /Users/simonwang/Documents/Usage/AIagent4bio/lab2/data/Badia-i-Mompel et al 2023.md
Process: Review the reference section and categorize references into: (1) seminal/historical papers (e.g., lac operon), (2) method/tool papers, (3) review articles, (4) database/resource papers, (5) application/use case papers, and (6) benchmarking/validation papers. For each reference, extract: author names, year, title, journal, and assign it to the appropriate category. Generate a CSV file with columns: Reference_Number, Authors, Year, Title, Journal, Category.
Output: /Users/simonwang/Documents/Usage/AIagent4bio/lab1/practice

## Task 8: Extract Technology and Protocol Information
Input: /Users/simonwang/Documents/Usage/AIagent4bio/lab2/data/Badia-i-Mompel et al 2023.md
Process: Scan the paper for mentions of experimental technologies (e.g., scRNA-seq, scATAC-seq, ChIP-seq, Hi-C, CRISPR screens, etc.). For each technology, extract: (1) full name and abbreviation, (2) what it measures, (3) key advantages, (4) limitations or challenges, (5) cost considerations if mentioned, and (6) any emerging alternatives. Create a comprehensive technology reference table in CSV format.
Output: /Users/simonwang/Documents/Usage/AIagent4bio/lab1/practice

## Task 9: Create a Glossary of Key Terms
Input: /Users/simonwang/Documents/Usage/AIagent4bio/lab2/data/Badia-i-Mompel et al 2023.md
Process: Identify key technical terms and concepts used throughout the paper (e.g., GRN, TF, CRE, pseudotime, motif, accessibility, etc.). For each term, extract: (1) the term/acronym, (2) full expansion if applicable, (3) definition from the paper context, (4) related concepts, and (5) section where it's first introduced or explained. Generate a glossary file in markdown or CSV format, organized alphabetically.
Output: /Users/simonwang/Documents/Usage/AIagent4bio/lab1/practice

## Task 10: Extract Benchmarking and Validation Strategies
Input: /Users/simonwang/Documents/Usage/AIagent4bio/lab2/data/Badia-i-Mompel et al 2023.md
Process: Review sections discussing benchmarking, validation, and assessment of GRN inference methods. Extract: (1) different validation approaches mentioned (in silico, experimental, database-based), (2) specific benchmarks or gold standards referenced, (3) metrics or criteria for evaluation, (4) limitations of current benchmarking approaches, (5) any platforms or resources for benchmarking (e.g., Open Problems project, DREAM challenges), and (6) recommendations for best practices. Create a structured summary document or CSV file.
Output: /Users/simonwang/Documents/Usage/AIagent4bio/lab1/practice

```


Created a file with 10 AI agent instruction ideas for research students writing papers in the GRN (Gene Regulatory Network) area. Each task follows the format of `task1.md` with Input, Process, and Output sections.

The tasks cover:
1. **Tool extraction** - Organizing GRN inference methods
2. **Database compilation** - TF binding motif resources
3. **Validation methods** - Experimental techniques
4. **Applications** - Downstream analysis examples
5. **Challenges** - Future directions and limitations
6. **Method comparisons** - Different approaches
7. **Reference organization** - Categorizing citations
8. **Technology reference** - Experimental protocols
9. **Glossary creation** - Key terms and definitions
10. **Benchmarking strategies** - Validation approaches

Each task is designed to help students extract, organize, and structure information from the review paper to support their own research and writing. The file has been saved to `/Users/simonwang/Documents/Usage/AIagent4bio/lab1/practice/task_ideas_grn_paper_writing.md`.

