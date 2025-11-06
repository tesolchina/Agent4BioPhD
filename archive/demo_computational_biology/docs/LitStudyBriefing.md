# LitStudy Package Briefing

## Overview
**LitStudy** is a Python package designed for systematic literature analysis within Jupyter Notebooks. It enables researchers to gather, analyze, and visualize scientific publications through metadata extraction, network analysis, and natural language processing.

## Core Capabilities

### 1. Data Collection & Management
- **Multiple Data Sources**: Supports Scopus, SemanticScholar, CrossRef, DBLP, arXiv, IEEE Xplore, Springer Link, and file formats (CSV, BibTeX, RIS)
- **Document Set Operations**: Union, intersection, difference operations on document collections
- **Metadata Extraction**: Retrieves titles, authors, venues, abstracts, citations, and references
- **Refinement**: Enhances metadata by cross-referencing with comprehensive databases (e.g., Scopus)
- **Filtering & Deduplication**: Smart filtering based on various criteria and automatic duplicate removal

### 2. Statistical Analysis (`litstudy.stats` & `litstudy.plot`)
Generates histograms and visualizations for:
- Publication years
- Authors and co-authorship patterns
- Affiliations and institutions
- Countries and continents
- Publication venues and source types
- Languages
- Number of authors per paper

### 3. Network Analysis (`litstudy.network`)
Constructs and visualizes bibliometric networks:
- **Citation Networks**: Shows which papers cite which
- **Co-citation Networks**: Papers cited together by other works
- **Bibliographic Coupling**: Papers sharing common references
- **Co-authorship Networks**: Collaboration patterns between researchers
- **Interactive Visualizations**: Uses pyvis for interactive HTML-based network graphs
- **Layout Algorithms**: ForceAtlas2 and spring layout for optimal positioning

### 4. Natural Language Processing (`litstudy.nlp`)
- **Corpus Building**: Converts abstracts/text into analyzable corpus
- **Text Preprocessing**: 
  - Stopword removal
  - N-gram detection (bigrams, trigrams)
  - Smart stemming
  - Outlier filtering
- **Topic Modeling**: 
  - Non-negative Matrix Factorization (NMF)
  - Latent Dirichlet Allocation (LDA)
  - Topic coherence analysis
- **Visualizations**:
  - Word clouds for topics
  - Word frequency distributions
  - Document-topic embeddings (2D landscape plots)

### 5. Core Data Structures (`litstudy.types`)

#### DocumentSet
- Immutable collection of Document objects
- Associated pandas DataFrame for metadata
- Supports set operations (union, intersection, difference)
- Methods for filtering, property addition/removal, and transformation

#### Document
- Represents individual publications
- Contains metadata: title, authors, abstract, DOI, year, venue, citations, etc.
- Supports various bibliographic formats

## How It Works: Typical Workflow

```python
# 1. Load documents from various sources
docs_scopus = litstudy.search_scopus(query="gene regulatory networks")
docs_csv = litstudy.load_csv("my_papers.csv")

# 2. Combine and filter
docs = docs_scopus | docs_csv  # Union
docs = docs.filter_docs(lambda d: d.publication_year >= 2020)

# 3. Refine with better metadata
docs_refined, docs_notfound = litstudy.refine_scopus(docs)

# 4. Statistical analysis
litstudy.plot_year_histogram(docs_refined)
litstudy.plot_author_histogram(docs_refined, limit=20)

# 5. Network analysis
cocitation_graph = litstudy.build_cocitation_network(docs_refined)
litstudy.plot_network(cocitation_graph, max_edges=500)

# 6. Topic modeling
corpus = litstudy.build_corpus(docs_refined, ngram_threshold=0.85)
topic_model = litstudy.train_nmf_model(corpus, num_topics=10)
litstudy.plot_topic_clouds(topic_model)
```

## Application to Gene Regulatory Network Research

### Why LitStudy is Valuable for GRN Literature Review

The Badia-i-Mompel et al. 2023 paper "Gene regulatory network inference in the era of single-cell multi-omics" presents a comprehensive review of:
- GRN inference methods from transcriptomics and chromatin accessibility data
- Classification of methods (Table 1 lists 20+ tools)
- Integration of multi-omics data
- Benchmarking challenges
- Applications and future directions

**LitStudy can systematically analyze this research landscape by:**

1. **Tracking Method Evolution**: Analyze temporal trends in GRN inference method development
2. **Identifying Research Hubs**: Map co-authorship networks and institutional collaborations
3. **Technology Clustering**: Group papers by methodology (SCENIC+, CellOracle, Pando, etc.)
4. **Citation Analysis**: Identify seminal papers and methodological lineages
5. **Topic Discovery**: Automatically identify emerging themes (e.g., "deep learning GRN", "multimodal integration", "benchmarking")
6. **Geographic Patterns**: Understand global distribution of GRN research

### Key Research Questions LitStudy Can Address

1. **Method Development Timeline**: When did multimodal GRN inference methods emerge?
2. **Citation Impact**: Which papers are most influential in the field?
3. **Collaboration Networks**: Who are the key research groups and their connections?
4. **Technology Adoption**: How quickly are new technologies (scATAC-seq, paired profiling) being adopted?
5. **Methodological Themes**: What are the main approaches (Bayesian vs. frequentist, linear vs. non-linear)?
6. **Application Domains**: Which biological systems are most studied (development, disease, cell types)?

## Technical Architecture

### Key Dependencies
- **pandas**: Data manipulation and metadata storage
- **networkx**: Network construction and analysis
- **pyvis**: Interactive network visualization
- **gensim**: NLP and topic modeling
- **matplotlib/seaborn**: Statistical plots
- **wordcloud**: Topic visualization

### Data Flow
```
Raw Sources → Document Objects → DocumentSet → Analysis
                                      ↓
                            Additional Metadata (DataFrame)
                                      ↓
                        Statistics / Networks / NLP
```

### Extensibility
- Custom data sources via abstract base classes
- Pluggable preprocessing pipelines for NLP
- Flexible filtering predicates
- Custom network metrics and layouts

## Strengths & Limitations

### Strengths
✓ Unified interface for multiple data sources  
✓ Reproducible workflows in Jupyter  
✓ Rich visualization capabilities  
✓ No-code statistical analysis  
✓ Handles large document collections  
✓ Interactive network exploration  

### Limitations
✗ Some data sources require API keys/subscriptions (Scopus)  
✗ NLP limited to English text  
✗ Topic modeling requires manual parameter tuning  
✗ Network visualization can be slow for large graphs  
✗ No built-in citation context analysis  
✗ Limited full-text analysis (primarily abstracts)  

## Best Practices

1. **Start Broad, Refine Iteratively**: Begin with comprehensive searches, then filter
2. **Use Multiple Sources**: Cross-validate with different databases
3. **Refine Metadata**: Always use `refine_scopus` or similar for complete metadata
4. **Document Exclusions**: Keep track of filtered documents
5. **Experiment with Topic Numbers**: Try different numbers of topics (5-20 range)
6. **Validate Networks**: Check network components and isolated nodes
7. **Save Intermediate Results**: Cache document sets to avoid re-querying APIs

## Application Plan: GRN Literature Analysis

A detailed implementation plan has been created in `GRN_Literature_Analysis_Plan.md` that demonstrates how to apply LitStudy to analyze the gene regulatory network inference literature landscape described in Badia-i-Mompel et al. 2023.

### Plan Highlights

The notebook plan includes **12 comprehensive sections**:

1. **Introduction & Setup** - Research questions and environment
2. **Data Collection** - Multi-source query strategy for GRN papers
3. **Data Refinement** - Quality control and subsetting
4. **Temporal Analysis** - Evolution of GRN methods over time
5. **Authorship Analysis** - Key researchers and collaboration networks
6. **Citation Networks** - Methodological lineages and seminal papers
7. **Topic Modeling** - Automatic theme discovery with 12 topics
8. **Method Deep Dive** - Analysis of 20+ specific tools from Table 1
9. **Venue Analysis** - Publication patterns and strategic outlets
10. **Gap Analysis** - Under-explored areas and future directions
11. **Validation** - Quality checks against the review paper
12. **Summary** - Actionable insights and recommendations

### Expected Deliverables

**Visualizations**:
- Interactive co-citation and co-authorship networks (HTML)
- Publication timeline with technology milestones
- Topic word clouds and document landscape
- Geographic distribution maps

**Data Products**:
- Complete annotated bibliography (CSV)
- Method comparison tables
- Citation trajectory data
- Collaboration matrices

**Insights**:
- Quantitative validation of review's categorization
- Hidden gem papers (high impact, under-cited)
- Emerging themes not yet mainstream
- Geographic and institutional patterns
- Venue-topic associations for publication strategy

### Integration with the Review Paper

The plan is designed to:
- ✓ **Complement** the qualitative review with quantitative data
- ✓ **Validate** the paper's method categorization (Table 1)
- ✓ **Extend** the analysis with network and temporal perspectives
- ✓ **Identify** gaps and opportunities for future research
- ✓ **Provide** reproducible, updateable framework

### Estimated Effort

- **Data Collection**: 1-2 hours (with API access)
- **Analysis Execution**: 3-4 hours
- **Interpretation & Writing**: 2-3 hours
- **Total**: 6-9 hours for complete analysis

### Prerequisites

- Scopus API key (or SemanticScholar alternative)
- Python environment with LitStudy and dependencies
- 8GB RAM, ~500MB storage
- Jupyter Notebook or JupyterLab

### Key Research Questions Addressed

1. **When** did multi-omics GRN methods emerge and evolve?
2. **Who** are the leading researchers and institutions?
3. **What** are the main methodological themes and families?
4. **Where** is GRN research geographically concentrated?
5. **How** are methods being validated and benchmarked?
6. **Why** are certain approaches more influential?

## Conclusion

LitStudy provides a powerful, programmatic approach to literature analysis that combines quantitative bibliometrics with qualitative insights from NLP. For systematic reviews like the GRN inference landscape described in Badia-i-Mompel et al. 2023, it offers reproducible, data-driven methods to understand research trends, identify gaps, and guide future investigations.

The detailed plan in `GRN_Literature_Analysis_Plan.md` provides a concrete roadmap for implementing a comprehensive literature analysis that will:
- Generate quantitative evidence to support or challenge qualitative claims
- Reveal hidden patterns in collaboration and citation networks
- Identify emerging trends and under-explored opportunities
- Create actionable recommendations for researchers entering the field
- Establish a reproducible framework that can be updated as the field evolves
