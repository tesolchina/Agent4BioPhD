# Jupyter Notebook Plan: Gene Regulatory Network Inference Literature Analysis

## Based on: Badia-i-Mompel et al. 2023 "Gene regulatory network inference in the era of single-cell multi-omics"

---

## Notebook Title
**"Systematic Analysis of Gene Regulatory Network Inference Methods: A Multi-Omics Perspective"**

## Objective
Create a comprehensive, reproducible literature analysis using LitStudy to:
1. Map the landscape of GRN inference methods from single-cell multi-omics data
2. Identify key methods, researchers, and trends mentioned in the Badia-i-Mompel review
3. Analyze citation networks to understand methodological lineages
4. Discover thematic clusters in GRN research
5. Provide quantitative insights to complement the qualitative review

---

## Notebook Structure

### Section 1: Introduction and Setup
**Goals**: 
- Introduce the research question
- Reference the Badia-i-Mompel et al. 2023 review
- Import libraries and configure environment

**Key Content**:
```markdown
# Gene Regulatory Network Inference: A Bibliometric Analysis

This notebook performs a systematic literature analysis to complement the review by 
Badia-i-Mompel et al. (2023) on GRN inference in the single-cell multi-omics era.

**Research Questions:**
1. What is the temporal evolution of GRN inference methods?
2. Who are the key contributors and research networks?
3. What are the main methodological themes?
4. How are methods being validated and benchmarked?
5. What are emerging trends and gaps?
```

**Code Cells**:
- Import litstudy, pandas, matplotlib, seaborn, networkx
- Set visualization parameters
- Define helper functions for the analysis

---

### Section 2: Data Collection Strategy
**Goals**: 
- Define search queries based on the review paper
- Collect papers from multiple sources
- Document search strategy for reproducibility

**Key Queries**:
Based on the paper's scope, construct searches for:

1. **Core GRN Methods**: 
   - "gene regulatory network" AND "inference"
   - "GRN" AND "single-cell"
   - "transcription factor" AND "target gene prediction"

2. **Technology-Specific**:
   - "scRNA-seq" AND "gene regulatory network"
   - "scATAC-seq" AND "chromatin accessibility"
   - "multimodal" AND "single-cell" AND "GRN"

3. **Specific Methods** (from Table 1):
   - SCENIC, SCENIC+, CellOracle, Pando, FigR, GRaNIE, ANANSE
   - Inferelator, GLUE, scMEGA, Dictys, DIRECT-NET
   - ATAC2GRN, LISA, SPIDER

**Code Strategy**:
```python
# Primary search: Core GRN papers
query_core = '("gene regulatory network" OR "GRN") AND ("inference" OR "reconstruction")'
docs_core = litstudy.search_scopus(query_core, year_range=(2015, 2024))

# Single-cell specific
query_sc = '"single-cell" AND "gene regulatory network"'
docs_sc = litstudy.search_scopus(query_sc, year_range=(2018, 2024))

# Multi-omics methods
query_multiomics = '("scRNA-seq" OR "scATAC-seq") AND "multimodal" AND "GRN"'
docs_multiomics = litstudy.search_scopus(query_multiomics, year_range=(2019, 2024))

# Combine and deduplicate
docs_all = docs_core | docs_sc | docs_multiomics
```

**Data Sources**:
- Primary: Scopus (most comprehensive metadata)
- Secondary: SemanticScholar (open access, good for citations)
- Supplementary: CrossRef, PubMed exports
- Manual: CSV of methods from Table 1 in the paper

---

### Section 3: Data Refinement and Quality Control
**Goals**:
- Enhance metadata quality
- Filter irrelevant papers
- Create curated subsets

**Processing Steps**:

1. **Metadata Enhancement**:
```python
# Refine with Scopus for complete metadata
docs_refined, docs_notfound = litstudy.refine_scopus(docs_all)
print(f"Refined: {len(docs_refined)}, Not found: {len(docs_notfound)}")
```

2. **Quality Filters**:
```python
# Remove papers without abstracts (needed for NLP)
docs_with_abstract = docs_refined.filter_docs(lambda d: d.abstract is not None)

# Focus on recent era (post-2015 for single-cell boom)
docs_filtered = docs_with_abstract.filter_docs(lambda d: d.publication_year >= 2015)

# Optional: Filter by citation count (>10 for established methods)
docs_impactful = docs_filtered.filter_docs(lambda d: d.citation_count > 10)
```

3. **Create Thematic Subsets**:
```python
# Methods papers (contain "method", "tool", "algorithm")
docs_methods = docs_filtered.filter_docs(
    lambda d: any(kw in d.title.lower() for kw in ['method', 'tool', 'algorithm', 'framework'])
)

# Review papers
docs_reviews = docs_filtered.filter_docs(
    lambda d: any(kw in d.title.lower() for kw in ['review', 'survey', 'benchmark'])
)

# Application papers
docs_applications = docs_filtered - docs_methods - docs_reviews
```

---

### Section 4: Temporal Analysis - Evolution of GRN Methods
**Goals**:
- Track publication trends over time
- Identify key inflection points
- Correlate with technology developments

**Analyses**:

1. **Publication Timeline**:
```python
# Overall trend
litstudy.plot_year_histogram(docs_filtered, vertical=True, title="GRN Papers by Year")

# By category
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
litstudy.plot_year_histogram(docs_methods, ax=axes[0], title="Methods")
litstudy.plot_year_histogram(docs_reviews, ax=axes[1], title="Reviews")
litstudy.plot_year_histogram(docs_applications, ax=axes[2], title="Applications")
```

2. **Technology Adoption Timeline**:
```python
# Track mentions of key technologies
technologies = {
    'scRNA-seq': lambda d: 'scrna' in d.abstract.lower(),
    'scATAC-seq': lambda d: 'scatac' in d.abstract.lower(),
    'Multi-omics': lambda d: any(kw in d.abstract.lower() for kw in ['multimodal', 'multi-omics', 'paired profiling']),
    'Deep Learning': lambda d: any(kw in d.abstract.lower() for kw in ['deep learning', 'neural network', 'transformer'])
}

# Create timeline
timeline_data = {}
for tech, predicate in technologies.items():
    counts_by_year = defaultdict(int)
    for doc in docs_filtered:
        if doc.abstract and predicate(doc):
            counts_by_year[doc.publication_year] += 1
    timeline_data[tech] = counts_by_year

# Plot stacked area chart
```

**Interpretations**:
- Identify the 2018-2020 period as the "single-cell multi-omics boom"
- Note the emergence of deep learning methods post-2020
- Correlate with key method publications (SCENIC: 2017, SCENIC+: 2022, etc.)

---

### Section 5: Authorship and Collaboration Analysis
**Goals**:
- Identify key researchers and groups
- Map collaboration networks
- Understand institutional contributions

**Analyses**:

1. **Top Authors**:
```python
litstudy.plot_author_histogram(docs_filtered, limit=20, 
                                title="Top 20 Authors in GRN Research")
```

2. **Top Institutions**:
```python
litstudy.plot_affiliation_histogram(docs_filtered, limit=15,
                                     title="Leading Research Institutions")
```

3. **Geographic Distribution**:
```python
# Country analysis
litstudy.plot_country_histogram(docs_filtered, limit=15)

# Continent view
litstudy.plot_continent_histogram(docs_filtered)
```

4. **Co-authorship Network**:
```python
# Build network of frequent collaborators
coauthor_graph = litstudy.build_coauthorship_network(docs_filtered, min_publications=3)

# Visualize with communities highlighted
litstudy.plot_network(coauthor_graph, 
                      max_edges=200,
                      title="GRN Research Collaboration Network",
                      iterations=1000)
```

**Key Insights to Extract**:
- Identify the Saez-Rodriguez group (authors of the review paper)
- Note connections between method developers and application researchers
- Observe geographic clusters (e.g., European vs. North American approaches)

---

### Section 6: Citation Network Analysis
**Goals**:
- Identify seminal papers
- Understand methodological lineages
- Find hidden gems (under-cited but important)

**Analyses**:

1. **Most Cited Papers**:
```python
# Extract top cited papers
top_cited = sorted(docs_filtered.docs, key=lambda d: d.citation_count or 0, reverse=True)[:20]

# Create summary table
citation_df = pd.DataFrame([
    {
        'Title': doc.title,
        'Authors': ', '.join([a.name for a in doc.authors[:3]]),
        'Year': doc.publication_year,
        'Citations': doc.citation_count,
        'Venue': doc.venue
    }
    for doc in top_cited
])
```

2. **Co-Citation Network**:
```python
# Papers cited together indicate thematic similarity
cocitation_graph = litstudy.build_cocitation_network(docs_filtered, 
                                                       min_cocitations=3)

# Visualize and identify clusters
litstudy.plot_network(cocitation_graph, 
                      max_edges=500,
                      title="Co-Citation Network: Methodological Families")
```

3. **Bibliographic Coupling**:
```python
# Papers sharing references indicate similar foundations
coupling_graph = litstudy.build_bibliographic_coupling_network(docs_filtered, 
                                                                 min_coupling=5)

# Identify method families
litstudy.plot_network(coupling_graph, max_edges=300)
```

4. **Citation Trajectory Analysis**:
```python
# Track citation accumulation over time for key methods
key_papers = ['SCENIC', 'CellOracle', 'SCENIC+', 'Pando']  # Filter by title keywords
# Plot citation growth curves
```

**Expected Findings**:
- SCENIC (2017) as a foundational paper
- Cluster of TF binding motif papers (JASPAR, HOCOMOCO)
- Separation between bulk and single-cell method lineages
- Emergence of benchmarking papers (BEELINE, etc.)

---

### Section 7: Topic Modeling and Thematic Analysis
**Goals**:
- Automatically discover research themes
- Validate against paper's manual categorization
- Identify emerging topics not covered in review

**Workflow**:

1. **Corpus Preparation**:
```python
# Build corpus from abstracts
corpus = litstudy.build_corpus(
    docs_filtered, 
    ngram_threshold=0.85,  # Detect bigrams like "transcription_factor"
    min_word_length=3,
    remove_stopwords=True
)

# Examine word distribution
word_dist = litstudy.compute_word_distribution(corpus)
print("Top 50 terms:")
print(word_dist.head(50))

# Visualize
litstudy.plot_word_distribution(corpus, limit=50, vertical=True)
```

2. **Topic Modeling with NMF**:
```python
# Train model with 12 topics (aligned with paper's taxonomy)
num_topics = 12
topic_model = litstudy.train_nmf_model(corpus, num_topics, max_iter=500)

# Display topics with representative terms
for i in range(num_topics):
    print(f"\nTopic {i+1}: {topic_model.best_tokens_for_topic(i, n=10)}")
```

3. **Topic Interpretation**:
Expected topics based on paper content:
- **Topic 1**: Transcriptomics inference (scRNA-seq, expression, SCENIC)
- **Topic 2**: Chromatin accessibility (ATAC-seq, peaks, motifs)
- **Topic 3**: Multi-omics integration (paired, multimodal, joint)
- **Topic 4**: TF binding prediction (motifs, JASPAR, ChIP-seq)
- **Topic 5**: Benchmarking (ground truth, evaluation, accuracy)
- **Topic 6**: Single-cell technologies (droplet, 10X, sequencing)
- **Topic 7**: Network inference algorithms (Bayesian, regression, random forest)
- **Topic 8**: Cell types and differentiation (development, trajectory, fate)
- **Topic 9**: Disease applications (cancer, disease, pathology)
- **Topic 10**: 3D genome structure (Hi-C, loops, TADs)
- **Topic 11**: Deep learning (neural networks, transformers)
- **Topic 12**: Validation experiments (CRISPR, perturbation, knockout)

4. **Topic Visualization**:
```python
# Word clouds for each topic
plt.figure(figsize=(20, 12))
litstudy.plot_topic_clouds(topic_model, ncols=4)

# Document-topic landscape
plt.figure(figsize=(15, 15))
litstudy.plot_embedding(corpus, topic_model, 
                        title="GRN Research Landscape")
```

5. **Topic Trends Over Time**:
```python
# Assign dominant topic to each paper
topic_assignments = topic_model.get_document_topics(corpus)

# Track topic popularity over time
topic_timeline = defaultdict(lambda: defaultdict(int))
for doc, topic_dist in zip(docs_filtered.docs, topic_assignments):
    dominant_topic = np.argmax(topic_dist)
    topic_timeline[dominant_topic][doc.publication_year] += 1

# Plot heatmap or line plot
```

**Validation Against Paper**:
- Compare discovered topics with paper's Table 1 categorization
- Check if NLP identifies the same method families
- Note any unexpected themes

---

### Section 8: Method-Specific Deep Dive
**Goals**:
- Analyze papers for specific methods from Table 1
- Compare method characteristics
- Track adoption and citations

**Approach**:

1. **Extract Method Papers**:
```python
# Create a mapping of methods from Table 1
methods_table = {
    'SCENIC+': ['SCENIC+', 'Bravo González-Blas'],
    'CellOracle': ['CellOracle', 'Kamimoto'],
    'Pando': ['Pando', 'Fleck'],
    'FigR': ['FigR', 'Kartha'],
    'GRaNIE': ['GRaNIE', 'Peidli'],
    'ANANSE': ['ANANSE', 'Xu'],
    'Inferelator': ['Inferelator', 'Arrieta-Ortiz'],
    'scMEGA': ['scMEGA', 'Zhao'],
    'Dictys': ['Dictys', 'Wang'],
    # ... add all 20+ methods
}

# Filter papers for each method
method_papers = {}
for method, keywords in methods_table.items():
    method_papers[method] = docs_filtered.filter_docs(
        lambda d: any(kw.lower() in d.title.lower() for kw in keywords)
    )
```

2. **Method Comparison Table**:
```python
# Create comparison of methods
comparison_data = []
for method, papers in method_papers.items():
    if len(papers) > 0:
        main_paper = papers.docs[0]  # Assume first is the main method paper
        comparison_data.append({
            'Method': method,
            'Year': main_paper.publication_year,
            'Citations': main_paper.citation_count,
            'Authors': len(main_paper.authors),
            'Venue': main_paper.venue
        })

comparison_df = pd.DataFrame(comparison_data).sort_values('Year')
```

3. **Method Adoption Analysis**:
```python
# Track citations of method papers over time
# Search for papers citing each method
# Plot adoption curves
```

---

### Section 9: Venue and Publication Analysis
**Goals**:
- Identify key journals and conferences
- Understand publication patterns
- Guide where to submit future work

**Analyses**:

1. **Top Venues**:
```python
litstudy.plot_source_histogram(docs_filtered, limit=20,
                                title="Top Publication Venues")
```

2. **Venue Types**:
```python
litstudy.plot_source_type_histogram(docs_filtered,
                                     title="Publication Types")
```

3. **Venue-Topic Analysis**:
```python
# Cross-reference venues with topics
# Create heatmap of venue-topic associations
```

**Expected Findings**:
- Nature Methods, Nature Biotechnology, Nature Communications as top journals
- Genome Research, Genome Biology for computational methods
- RECOMB, ISMB for conference papers
- Shift from bulk (pre-2018) to single-cell venues (post-2018)

---

### Section 10: Gap Analysis and Future Directions
**Goals**:
- Identify under-explored areas
- Compare paper's discussion with literature data
- Generate research recommendations

**Analyses**:

1. **Under-Cited Important Papers**:
```python
# Papers with high betweenness centrality but low citations
# Calculate network centrality metrics
centrality = nx.betweenness_centrality(cocitation_graph)

# Find papers with high centrality but low citations
hidden_gems = []
for node, cent in centrality.items():
    doc = [d for d in docs_filtered.docs if d.title == node][0]
    if cent > 0.1 and doc.citation_count < 20:
        hidden_gems.append((doc, cent))
```

2. **Emerging Themes**:
```python
# Topics growing fastest in recent years
recent_papers = docs_filtered.filter_docs(lambda d: d.publication_year >= 2022)
recent_corpus = litstudy.build_corpus(recent_papers)
recent_model = litstudy.train_nmf_model(recent_corpus, num_topics=8)

# Compare with overall topics to find new themes
```

3. **Gap Identification**:
```python
# Underrepresented areas from the paper's discussion:
gaps_keywords = [
    ('spatial omics', ['spatial', 'spatial transcriptomics', 'imaging']),
    ('metabolomics', ['metabolome', 'metabolomics']),
    ('protein dynamics', ['proteomics', 'protein abundance']),
    ('clinical translation', ['clinical', 'patient', 'therapy'])
]

# Count papers in each gap area
gap_analysis = {}
for gap_name, keywords in gaps_keywords:
    count = sum(1 for doc in docs_filtered.docs 
                if doc.abstract and any(kw in doc.abstract.lower() for kw in keywords))
    gap_analysis[gap_name] = count

# Visualize gaps
```

4. **Synthesis with Paper's "Challenges and Future Directions"**:
Compare paper's identified challenges with literature coverage:
- Scale and sparsity of single-cell data
- Integration of transcription and accessibility
- 3D genome structure
- TF binding prediction refinement
- Emerging multi-omics technologies
- Benchmarking standards

---

### Section 11: Validation and Quality Control
**Goals**:
- Ensure analysis validity
- Cross-check findings with paper
- Document limitations

**Checks**:

1. **Coverage Validation**:
```python
# Verify we captured papers from Table 1
table1_methods = ['SCENIC+', 'CellOracle', 'Pando', ...]  # All methods
found_methods = []
missing_methods = []

for method in table1_methods:
    papers = docs_filtered.filter_docs(
        lambda d: method.lower() in d.title.lower()
    )
    if len(papers) > 0:
        found_methods.append(method)
    else:
        missing_methods.append(method)

print(f"Found: {len(found_methods)}/{len(table1_methods)}")
print(f"Missing: {missing_methods}")
```

2. **Citation Cross-Check**:
```python
# Verify top-cited papers match known important works
known_important = [
    'SCENIC',  # Aibar et al. 2017
    'WGCNA',  # Langfelder & Horvath
    'ATAC-seq',  # Buenrostro et al.
]
# Check if these appear in our top-cited list
```

3. **Temporal Validation**:
```python
# Ensure timeline aligns with known method publication dates
method_timeline = {
    'SCENIC': 2017,
    'pySCENIC': 2020,
    'SCENIC+': 2022,
    'CellOracle': 2020,
    # ...
}
# Verify our data matches these dates
```

---

### Section 12: Summary and Insights
**Goals**:
- Synthesize key findings
- Create actionable recommendations
- Generate figures for publication

**Final Outputs**:

1. **Executive Summary Table**:
```python
summary_stats = {
    'Total Papers Analyzed': len(docs_filtered),
    'Date Range': f"{min(d.publication_year for d in docs_filtered.docs)}-{max(d.publication_year for d in docs_filtered.docs)}",
    'Unique Authors': len(set(a.name for d in docs_filtered.docs for a in d.authors)),
    'Countries Represented': len(set(d.country for d in docs_filtered.docs if d.country)),
    'Methods Identified': len(method_papers),
    'Average Citations': np.mean([d.citation_count for d in docs_filtered.docs if d.citation_count]),
}
```

2. **Key Findings**:
- Growth rate of GRN papers (% increase per year)
- Most influential authors and institutions
- Dominant methodological approaches
- Geographical distribution insights
- Emerging vs. established topics

3. **Recommendations**:
- Best venues for different types of contributions
- Under-explored research directions
- Potential collaborators
- Methods needing benchmarking

4. **Publication-Quality Figures**:
```python
# Generate final figures with publication styling
# - Timeline with annotations of key methods
# - Co-citation network with highlighted communities
# - Topic evolution heatmap
# - Geographic collaboration map
```

---

## Technical Requirements

### Data Sources
- **Required**: Scopus API key (for complete metadata)
- **Optional**: SemanticScholar API (open access)
- **Manual**: CSV file with Table 1 methods from paper

### Computational Resources
- **RAM**: ~8GB (for large document sets and NLP)
- **Time**: ~2-3 hours for complete analysis
- **Storage**: ~500MB for cached data

### Python Environment
```bash
pip install litstudy pandas numpy matplotlib seaborn networkx pyvis gensim wordcloud
```

---

## Expected Outputs

### 1. Interactive HTML Files
- `grn_cocitation_network.html` - Interactive citation network
- `grn_coauthorship_network.html` - Collaboration network
- `grn_topic_landscape.html` - Document embedding

### 2. Publication Figures (PNG/PDF)
- Timeline of GRN research (2015-2024)
- Top authors/institutions bar charts
- Topic word clouds (4x3 grid)
- Geographic heatmap
- Method comparison table

### 3. Data Tables (CSV)
- Complete bibliography with metadata
- Top 50 cited papers
- Method characteristics comparison
- Author collaboration matrix
- Venue statistics

### 4. Summary Report (Markdown)
- Executive summary
- Key findings by section
- Research recommendations
- Gap analysis results

---

## Validation Against Badia-i-Mompel et al. 2023

### Cross-Checks
1. ✓ Methods in our analysis match Table 1
2. ✓ Key papers appear in top-cited list
3. ✓ Timeline aligns with technology developments
4. ✓ Topics match paper's categorization
5. ✓ Challenges identified are consistent

### Novel Contributions
1. Quantitative collaboration networks
2. Citation trajectory analysis
3. Geographic distribution insights
4. Temporal topic evolution
5. Hidden gem identification
6. Venue-topic associations

---

## Reproducibility Notes

### Documentation
- All queries saved with timestamps
- API parameters logged
- Random seeds set for topic modeling
- Version info for all packages
- Data provenance tracked

### Replication
```python
# Include at top of notebook
import sys
import litstudy

print(f"Python version: {sys.version}")
print(f"LitStudy version: {litstudy.__version__}")
print(f"Analysis date: {datetime.now()}")
print(f"Scopus query date: [YYYY-MM-DD]")
```

---

## Timeline for Notebook Development

1. **Setup** (30 min): Environment, imports, data collection
2. **Data Collection** (1-2 hours): Query APIs, load files, refine metadata
3. **Basic Statistics** (30 min): Year, author, venue histograms
4. **Network Analysis** (1 hour): Build and visualize networks
5. **Topic Modeling** (1 hour): Corpus building, NMF training
6. **Deep Dives** (1-2 hours): Method analysis, gaps, validation
7. **Synthesis** (1 hour): Summary, figures, recommendations
8. **Documentation** (30 min): Markdown narratives, reproducibility info

**Total Estimated Time**: 6-9 hours

---

## Success Criteria

✓ Covers all major themes from Badia-i-Mompel et al. 2023  
✓ Identifies 20+ methods from Table 1  
✓ Generates publication-quality visualizations  
✓ Provides novel quantitative insights  
✓ Fully reproducible with documented queries  
✓ Actionable recommendations for researchers  
✓ Interactive outputs for exploration  

---

## Next Steps

1. **Set up Scopus API access** (or use SemanticScholar as alternative)
2. **Create initial notebook structure** with sections
3. **Test queries** to estimate data coverage
4. **Iteratively refine** filters and parameters
5. **Validate** against known papers/methods
6. **Generate figures** and polish visualizations
7. **Write narratives** connecting to paper's content
8. **Peer review** for accuracy and completeness

---

## Appendix: Key Terms for Queries

### Core Concepts
- gene regulatory network, GRN, transcription factor, TF-gene interaction
- cis-regulatory element, CRE, enhancer, promoter
- chromatin accessibility, open chromatin, ATAC-seq
- single-cell RNA-seq, scRNA-seq, transcriptomics
- multi-omics, multimodal profiling, paired data

### Methods/Algorithms
- network inference, graph reconstruction, causal inference
- co-expression, correlation network, WGCNA
- regression, Bayesian inference, random forest
- motif enrichment, TF binding prediction, PWM
- deep learning, neural network, graph neural network

### Applications
- cell differentiation, development, trajectory
- cell type identification, cell state
- disease, cancer, pathway analysis
- perturbation, CRISPR screen, knockout

### Technologies
- 10X Genomics, multiome, paired-tag
- ChIP-seq, CUT&Tag, Hi-C
- spatial transcriptomics, imaging
- benchmarking, ground truth, validation

---

This plan provides a comprehensive roadmap for creating a systematic, data-driven analysis that complements and extends the Badia-i-Mompel et al. 2023 review with quantitative bibliometric insights.
