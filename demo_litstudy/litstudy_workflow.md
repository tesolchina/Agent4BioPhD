# LitStudy Workflow Explained

## Basic Components of LitStudy

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │     │                 │
│  DATA SOURCES   │────▶│  COLLECTION     │────▶│  ANALYSIS       │────▶│  VISUALIZATION  │
│                 │     │  MANAGEMENT     │     │  & STATS        │     │  & REPORTING    │
│                 │     │                 │     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
        ▲                      │                      │                      │
        │                      │                      │                      │
        └──────────────────────┴──────────────────────┴──────────────────────┘
```

## How LitStudy Works - Step by Step

1. **Data Collection**
   - Searches academic databases (Scopus, SemanticScholar, etc.)
   - Loads papers from files (CSV, BibTeX, RIS)
   - Retrieves metadata (titles, authors, abstracts, citations)

2. **Collection Management**
   - Creates collections of papers
   - Filters papers by criteria (year, keywords, etc.)
   - Removes duplicates
   - Enhances metadata

3. **Analysis**
   - Statistical analysis (publication years, authors, venues)
   - Network analysis (citations, co-authorship)
   - Topic modeling (extract key themes)
   - Text mining (extract keywords, concepts)

4. **Visualization & Reporting**
   - Creates charts and graphs
   - Generates network visualizations
   - Produces reports with insights
   - Exports data for further analysis

## Simple Example Workflow

```python
# 1. Search for papers
docs = litstudy.search_scopus(query="gene regulatory networks")

# 2. Filter and manage
docs = docs.filter_docs(lambda d: d.publication_year >= 2020)

# 3. Analyze
year_histogram = litstudy.stats.publication_years(docs)
top_authors = litstudy.stats.top_authors(docs, limit=10)

# 4. Visualize
litstudy.plot.year_histogram(docs)
litstudy.plot.author_histogram(docs, limit=10)

# 5. Save and export
litstudy.save_csv(docs, "my_papers.csv")
```