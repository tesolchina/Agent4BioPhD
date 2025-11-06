# File path for task documentation
_Exported on 06/11/2025 at 23:51:21 GMT+8 from Cursor (2.0.64)_

---

**User**

/Users/simonwang/Documents/Usage/AIagent4bio/lab4/demo/task4.md

---

**Cursor**


Reading `task4.md` to understand the task.



Breaking this into sub-tasks:
1. Read the paper to understand its focus
2. Clone the ToolUniverse repository
3. Explore the repository structure
4. Identify tools relevant to the paper
5. Select the top 10 most relevant tools
6. Gather detailed information about each tool
7. Generate a markdown report

Starting with the paper and cloning the repository.



Exploring the ToolUniverse repository structure to identify relevant tools:



Exploring the tools directory to find relevant tools:



Searching the tools directory for relevant tools:



Reviewing relevant tool files to gather information:



Creating a TODO list and gathering more tool information:



Searching for additional relevant tools and checking the data directory for tool metadata:



Checking JSON metadata files for tool details, then compiling the report:



Checking the packages directory:



Checking the single-cell tools JSON and compiling the report:



Compiling the report with the top 10 most relevant tools:


```markdown
# Tool Exploration Report: Gene Regulatory Network Inference from Single-Cell Multi-Omics Data

**Paper**: Gene regulatory network inference in the era of single-cell multi-omics  
**Authors**: Badia-i-Mompel et al. (2023)  
**Source Repository**: ToolUniverse (https://github.com/mims-harvard/ToolUniverse)  
**Date**: Generated from ToolUniverse exploration

---

## Executive Summary

This report identifies and describes the **10 most relevant tools** from ToolUniverse for research related to gene regulatory network (GRN) inference from single-cell multi-omics data, as described in the Badia-i-Mompel et al. (2023) review paper. The tools are categorized by their primary function and relevance to the paper's key themes: single-cell transcriptomics, chromatin accessibility analysis, transcription factor binding prediction, multi-omics integration, and network analysis.

---

## Top 10 Most Relevant Tools

### 1. pySCENIC - Single-Cell Regulatory Network Inference

**Relevance**: ⭐⭐⭐⭐⭐ (Directly mentioned in the paper)  
**Category**: GRN Inference / Single-Cell Regulatory Networks  
**Tool Type**: Python Package

#### Description
pySCENIC is the Python implementation of SCENIC (Single-CEll regulatory Network Inference and Clustering), a method specifically designed for inferring gene regulatory networks from single-cell RNA-seq data. The paper mentions SCENIC as one of the first GRN inference methods tailored to scRNA-seq data, which generates cell type-specific GRNs by exploiting TF-gene co-expression patterns and pruning edges based on TF binding motif enrichment.

#### Key Features
- Infers co-expression modules using GRNBoost2 or GENIE3
- Prunes modules using cis-regulatory footprint analysis
- Calculates cellular enrichment scores (AUCell) for regulon activity
- Identifies cell states and types based on regulatory activity
- Works with single-cell expression data

#### Installation
```bash
pip install pyscenic
# or
conda install -c bioconda pyscenic
```

#### Usage Example
```python
import pandas as pd
from pyscenic.utils import modules_from_adjacencies
from pyscenic.prune import prune2df, df2regulons
from pyscenic.aucell import aucell

# Load expression data (genes x cells)
ex_matrix = pd.read_csv('expression_matrix.csv', index_col=0)

# Step 1: Infer co-expression modules (requires GRNBoost2)
# adjacencies = grnboost2(ex_matrix, tf_names=tf_names)

# Step 2: Prune modules for targets with cis-regulatory footprints
# Requires motif databases (e.g., JASPAR) and cis-regulatory regions
# df = prune2df(dbs, modules, motif_annotations)
# regulons = df2regulons(df)

# Step 3: Calculate cellular enrichment (AUCell)
# auc_matrix = aucell(ex_matrix, regulons)
```

#### Workflow Steps
1. Prepare expression matrix (genes × cells)
2. Download motif databases and TF annotations
3. Run GRNBoost2 to infer co-expression modules
4. Prune modules using `prune2df()` with motif data
5. Score regulon activity using `aucell()` for enrichment

#### Documentation
- **Documentation**: https://pyscenic.readthedocs.io/
- **Repository**: https://github.com/aertslab/pySCENIC
- **Keywords**: regulatory networks, transcription factors, single-cell, gene regulation, SCENIC

#### Relevance to Paper
The paper extensively discusses SCENIC as a key method for single-cell GRN inference, mentioning it 8 times. It's highlighted as one of the first methods to leverage both TF-gene co-expression and motif enrichment for cell type-specific GRN inference.

---

### 2. Scanpy - Scalable Single-Cell Analysis in Python

**Relevance**: ⭐⭐⭐⭐⭐ (Essential for single-cell data processing)  
**Category**: Single-Cell Genomics / Data Analysis  
**Tool Type**: Python Package

#### Description
Scanpy is a scalable toolkit for analyzing single-cell gene expression data. It provides comprehensive preprocessing, visualization, clustering, trajectory inference, and differential expression testing for datasets with more than one million cells. While not directly a GRN inference tool, it's essential for preprocessing single-cell data before GRN inference.

#### Key Features
- Preprocessing: filtering, normalization, log transformation
- Dimensionality reduction: PCA, UMAP, t-SNE
- Clustering: Leiden, Louvain algorithms
- Trajectory inference: pseudotime analysis
- Differential expression testing
- Visualization tools
- Integration with multi-omics data

#### Installation
```bash
pip install scanpy
# or
conda install -c conda-forge scanpy
```

#### Usage Example
```python
import scanpy as sc
import pandas as pd

# Read 10X data
adata = sc.read_10x_mtx('filtered_feature_bc_matrix/')
adata.var_names_unique()

# Basic preprocessing
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)

# Find highly variable genes and cluster
sc.pp.highly_variable_genes(adata)
sc.pp.pca(adata)
sc.pp.neighbors(adata)
sc.tl.umap(adata)
sc.tl.leiden(adata)

# Visualize
sc.pl.umap(adata, color='leiden')
```

#### Quick Start
1. Install: `pip install scanpy`
2. Read data: `sc.read_10x_mtx()` or `sc.read_h5ad()`
3. Preprocess: filter cells/genes, normalize, log transform
4. Analyze: PCA, neighbors, UMAP, clustering
5. Visualize: `sc.pl.umap()`, `sc.pl.violin()`

#### Documentation
- **Documentation**: https://scanpy.readthedocs.io/
- **Repository**: https://github.com/scverse/scanpy
- **Keywords**: single-cell, RNA-seq, clustering, trajectory inference, differential expression

#### Relevance to Paper
The paper emphasizes the importance of single-cell technologies (mentioned 104 times) for GRN inference. Scanpy is the standard tool for preprocessing and analyzing single-cell RNA-seq data, which is a prerequisite for most GRN inference methods discussed in the paper.

---

### 3. Arboreto / GRNBoost2 - Gene Regulatory Network Inference

**Relevance**: ⭐⭐⭐⭐⭐ (Directly mentioned in the paper)  
**Category**: GRN Inference  
**Tool Type**: Python Package

#### Description
Arboreto provides GRNBoost2, a faster implementation of GENIE3 for gene regulatory network inference. The paper mentions GRNBoost2 as a key method that distinguishes TFs from target genes and trains models to predict target gene expression based on TF expression, introducing putative causal relationships.

#### Key Features
- Fast GRN inference from expression data
- Distinguishes TFs from target genes
- Introduces directed, causal relationships
- Faster than original GENIE3
- Used as a component in SCENIC workflow

#### Installation
```bash
pip install arboreto
# or
conda install -c bioconda arboreto
```

#### Usage Example
```python
from arboreto.algo import grnboost2
import pandas as pd

# Load expression matrix (genes x cells)
ex_matrix = pd.read_csv('expression_matrix.csv', index_col=0)

# List of transcription factor gene names
tf_names = ['TF1', 'TF2', 'TF3', ...]  # Your TF list

# Infer regulatory network
adjacencies = grnboost2(
    ex_matrix,
    tf_names=tf_names,
    verbose=True
)

# adjacencies is a DataFrame with columns: TF, target, importance
```

#### Documentation
- **Repository**: https://github.com/aertslab/arboreto
- **Keywords**: GRN inference, GENIE3, gene regulatory networks, transcription factors

#### Relevance to Paper
The paper mentions GRNBoost2 multiple times as a key method for GRN inference. It's described as a faster implementation that turns undirected co-expression interactions into directed regulatory connections, which is fundamental to the GRN inference workflow.

---

### 4. scVelo - RNA Velocity Analysis in Single Cells

**Relevance**: ⭐⭐⭐⭐ (Trajectory inference for GRN analysis)  
**Category**: Single-Cell Dynamics / Trajectory Inference  
**Tool Type**: Python Package

#### Description
scVelo is a Python library for RNA velocity analysis to study cellular dynamics and trajectory inference in single-cell RNA sequencing data. It estimates future cell states based on spliced/unspliced mRNA ratios, which is relevant for understanding dynamic GRN changes during cell differentiation and development.

#### Key Features
- RNA velocity estimation from spliced/unspliced mRNA
- Trajectory inference and cell fate prediction
- Dynamic modeling of gene expression
- Integration with scanpy workflows
- Visualization of velocity fields

#### Installation
```bash
pip install scvelo
# or
conda install -c conda-forge scvelo
```

#### Usage Example
```python
import scvelo as scv
import scanpy as sc

# Load data with spliced/unspliced information
adata = scv.datasets.pancreatic_endocrinogenesis()

# Preprocess data
scv.pp.filter_and_normalize(adata, min_shared_counts=20, n_top_genes=2000)
scv.pp.moments(adata, n_pcs=30, n_neighbors=30)

# Compute velocity and velocity graph
scv.tl.velocity(adata)
scv.tl.velocity_graph(adata)

# Plot velocity field
scv.pl.velocity_embedding_stream(adata, basis='umap')
```

#### Quick Start
1. Install: `pip install scvelo`
2. Import: `import scvelo as scv`
3. Load data with spliced/unspliced counts
4. Preprocess: `scv.pp.filter_and_normalize(adata)`
5. Analyze: `scv.tl.velocity()`; `scv.pl.velocity_embedding()`

#### Documentation
- **Documentation**: https://scvelo.readthedocs.io/
- **Repository**: https://github.com/theislab/scvelo
- **Keywords**: RNA velocity, single-cell dynamics, trajectory inference, cellular dynamics, gene expression

#### Relevance to Paper
The paper discusses how pseudotime ordering and trajectory analysis can inform GRN inference, especially for continuous processes like development and differentiation. Methods like LEAP and SINCERITIES leverage pseudotime to infer directionality in GRNs, making RNA velocity analysis highly relevant.

---

### 5. scvi-tools - Deep Probabilistic Analysis of Single-Cell Omics Data

**Relevance**: ⭐⭐⭐⭐ (Multi-omics integration)  
**Category**: Single-Cell Multi-Omics / Deep Learning  
**Tool Type**: Python Package

#### Description
scvi-tools provides deep probabilistic models for analyzing single-cell omics data, including multi-omics integration. The paper emphasizes the importance of integrating transcriptomics and chromatin accessibility data for improved GRN inference, making this tool highly relevant.

#### Key Features
- Multi-omics data integration
- Deep probabilistic modeling
- Batch correction
- Dimensionality reduction
- Imputation and denoising
- Supports scRNA-seq, scATAC-seq, and multi-omics

#### Installation
```bash
pip install scvi-tools
# or
conda install -c conda-forge scvi-tools
```

#### Usage Example
```python
import scvi
import scanpy as sc
import anndata as ad

# Load single-cell data
adata = sc.read_h5ad('single_cell_data.h5ad')

# Setup and train model
scvi.model.SCVI.setup_anndata(adata)
model = scvi.model.SCVI(adata)
model.train()

# Get latent representation
latent = model.get_latent_representation()

# For multi-omics integration
# Use scvi.model.TOTALVI or scvi.model.MULTIVI
```

#### Documentation
- **Documentation**: https://docs.scvi-tools.org/
- **Repository**: https://github.com/scverse/scvi-tools
- **Keywords**: single-cell, multi-omics, deep learning, probabilistic models, integration

#### Relevance to Paper
The paper extensively discusses multi-omics integration (mentioned 26 times) and how combining scRNA-seq and scATAC-seq data improves GRN inference accuracy. scvi-tools provides state-of-the-art methods for integrating these modalities, which is crucial for the multimodal GRN inference methods described in the paper.

---

### 6. episcanpy - Epigenomics Single Cell Analysis in Python

**Relevance**: ⭐⭐⭐⭐⭐ (Essential for ATAC-seq analysis)  
**Category**: Epigenomics / Chromatin Accessibility  
**Tool Type**: Python Package

#### Description
episcanpy is a Python package for analyzing epigenomics single-cell data, particularly ATAC-seq (Assay for Transposase-Accessible Chromatin with sequencing). The paper emphasizes that chromatin accessibility data is crucial for refining GRN inference by identifying open chromatin regions where TFs can bind.

#### Key Features
- Single-cell ATAC-seq analysis
- Peak calling and accessibility analysis
- Integration with scanpy
- Chromatin accessibility visualization
- Multi-omics integration capabilities

#### Installation
```bash
pip install episcanpy
# or
conda install -c conda-forge episcanpy
```

#### Usage Example
```python
import episcanpy as epi
import scanpy as sc

# Load ATAC-seq data
atac_adata = sc.read_h5ad('atac_data.h5ad')

# Preprocess ATAC-seq data
epi.pp.filter_cells(atac_adata, min_features=1000)
epi.pp.filter_features(atac_adata, min_cells=10)

# Normalize and transform
epi.pp.normalize_per_cell(atac_adata)
epi.pp.log1p(atac_adata)

# Dimensionality reduction
epi.pp.lsi(atac_adata, n_components=50)
epi.pp.neighbors(atac_adata)
epi.tl.umap(atac_adata)
epi.tl.leiden(atac_adata)

# Visualize
epi.pl.umap(atac_adata, color='leiden')
```

#### Documentation
- **Repository**: https://github.com/colomemaria/epiScanpy
- **Keywords**: ATAC-seq, epigenomics, chromatin accessibility, single-cell, regulatory elements

#### Relevance to Paper
The paper mentions ATAC-seq 11 times and emphasizes its importance for identifying open chromatin regions (CREs) that can be linked to TFs and target genes. episcanpy is essential for preprocessing and analyzing scATAC-seq data, which is a key input for multimodal GRN inference methods.

---

### 7. JASPAR - Transcription Factor Binding Site Matrices

**Relevance**: ⭐⭐⭐⭐⭐ (Directly mentioned in the paper)  
**Category**: Transcription Factor Databases / Motif Analysis  
**Tool Type**: Database / API Tool

#### Description
JASPAR is a database of transcription factor binding site matrices (position weight matrices, PWMs) that is directly mentioned in the paper's Box 1. The paper notes that GRN inference methods use TF binding motif databases to predict TF binding events on accessible CREs, and JASPAR is one of the most commonly used databases.

#### Key Features
- Access to TF binding site matrices (PWMs)
- Multiple collections (CORE, CNE, etc.)
- Species-specific data
- REST API access
- Integration with motif matching algorithms

#### Installation
Access via ToolUniverse or direct API:
```python
from tooluniverse.tools import JASPAR_get_transcription_factors
```

#### Usage Example
```python
# Using ToolUniverse
from tooluniverse import ToolUniverse

tu = ToolUniverse()
tu.load_tools()

# Get transcription factors from JASPAR
result = tu.run({
    "name": "JASPAR_get_transcription_factors",
    "arguments": {
        "collection": "CORE",
        "limit": 20
    }
})

# Result contains TF matrices with:
# - matrix_id, name, collection
# - species, class, family
# - pfm (position frequency matrix)
# - pwm (position weight matrix)
```

#### API Endpoint
- **API**: https://jaspar.elixir.no/api/v1/matrix/
- **Website**: https://jaspar.genereg.net/
- **Keywords**: transcription factors, binding motifs, PWM, TF binding sites

#### Relevance to Paper
The paper mentions JASPAR 3 times and lists it in Box 1 as one of the key TF binding motif databases used by GRN inference methods. The paper explains that methods use these databases with motif matcher algorithms (like FIMO, HOMER, MOODS) to predict TF binding on open chromatin regions, which is a critical step in GRN inference.

---

### 8. ENCODE - Functional Genomics Experiments Database

**Relevance**: ⭐⭐⭐⭐⭐ (Directly mentioned in the paper)  
**Category**: Functional Genomics / Data Resources  
**Tool Type**: Database / API Tool

#### Description
The ENCODE (Encyclopedia of DNA Elements) Consortium provides a comprehensive database of functional genomics experiments, including ChIP-seq and ATAC-seq data. The paper mentions ENCODE 6 times and notes that it has catalogued over one million candidate CREs with enhancer-like signatures.

#### Key Features
- Search ChIP-seq and ATAC-seq experiments
- Access to experiment metadata
- Downloadable data files (FASTQ, BAM, bigWig, peaks)
- Filter by assay, target, organism, cell type
- Programmatic access via API

#### Installation
Access via ToolUniverse:
```python
from tooluniverse.tools import ENCODE_search_experiments, ENCODE_list_files
```

#### Usage Example
```python
from tooluniverse import ToolUniverse

tu = ToolUniverse()
tu.load_tools()

# Search for ChIP-seq experiments
result = tu.run({
    "name": "ENCODE_search_experiments",
    "arguments": {
        "assay_title": "ChIP-seq",
        "target": "CTCF",
        "organism": "Homo sapiens",
        "status": "released",
        "limit": 10
    }
})

# List available files
files = tu.run({
    "name": "ENCODE_list_files",
    "arguments": {
        "file_type": "fastq",
        "assay_title": "ATAC-seq",
        "limit": 10
    }
})
```

#### API Endpoint
- **API**: https://www.encodeproject.org/search/
- **Website**: https://www.encodeproject.org/
- **Keywords**: ChIP-seq, ATAC-seq, functional genomics, regulatory elements, ENCODE

#### Relevance to Paper
The paper extensively discusses ENCODE data for validating GRN predictions and accessing reference datasets. ENCODE provides experimental ChIP-seq data that can be used to validate TF binding predictions made by GRN inference methods, which is a key validation strategy discussed in the paper.

---

### 9. ReMap - Transcription Factor Binding Sites Database

**Relevance**: ⭐⭐⭐⭐ (TF binding validation)  
**Category**: Transcription Factor Binding / Validation  
**Tool Type**: Database / API Tool

#### Description
ReMap provides a database of transcription factor binding sites from ChIP-seq experiments, organized by cell type and tissue. This is useful for validating TF binding predictions made during GRN inference, which the paper emphasizes as an important validation step.

#### Key Features
- TF binding sites from ChIP-seq experiments
- Cell type-specific binding data
- Gene and cell type filtering
- Integration with ENCODE data
- Validation of GRN predictions

#### Installation
Access via ToolUniverse:
```python
from tooluniverse.tools import ReMap_get_transcription_factor_binding
```

#### Usage Example
```python
from tooluniverse import ToolUniverse

tu = ToolUniverse()
tu.load_tools()

# Get TF binding sites for a specific gene
result = tu.run({
    "name": "ReMap_get_transcription_factor_binding",
    "arguments": {
        "gene_name": "BRCA1",
        "cell_type": "HepG2",
        "limit": 10
    }
})

# Returns experiments with:
# - accession, assay_title
# - target (TF information)
# - biosample_ontology (cell type)
# - description
```

#### API Endpoint
- **Website**: https://remap.univ-amu.fr/
- **Keywords**: ChIP-seq, transcription factors, binding sites, cell type-specific, validation

#### Relevance to Paper
The paper discusses experimental validation of GRN predictions, including using ChIP-seq data to validate TF binding events. ReMap provides curated ChIP-seq data that can be used to assess how many TF binding events were correctly predicted by GRN inference methods, which is a key validation approach mentioned in the paper.

---

### 10. NetworkX - Network Analysis Library

**Relevance**: ⭐⭐⭐⭐ (GRN topology analysis)  
**Category**: Network Analysis / Graph Theory  
**Tool Type**: Python Package

#### Description
NetworkX is a comprehensive Python library for network analysis. The paper discusses downstream GRN analyses including topological analysis, network centrality measures, and module identification, all of which can be performed using NetworkX.

#### Key Features
- Graph construction and manipulation
- Network centrality measures (degree, betweenness, closeness, eigenvector)
- Community detection and clustering
- Path analysis
- Network visualization
- Integration with other analysis tools

#### Installation
```bash
pip install networkx
# or
conda install -c conda-forge networkx
```

#### Usage Example
```python
import networkx as nx
import pandas as pd

# Create GRN from edge list
# Assuming you have a DataFrame with TF, target, weight columns
edges = pd.DataFrame({
    'TF': ['TF1', 'TF1', 'TF2', 'TF2'],
    'target': ['Gene1', 'Gene2', 'Gene1', 'Gene3'],
    'weight': [0.8, 0.6, 0.7, 0.9]
})

# Create directed graph
G = nx.from_pandas_edgelist(edges, 'TF', 'target', 
                            edge_attr='weight', 
                            create_using=nx.DiGraph())

# Calculate centrality measures
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G)

# Find communities/modules
communities = nx.community.greedy_modularity_communities(G.to_undirected())

# Identify hubs (highly connected nodes)
hubs = [node for node, degree in G.degree() if degree > 5]
```

#### Documentation
- **Documentation**: https://networkx.org/
- **Repository**: https://github.com/networkx/networkx
- **Keywords**: network analysis, graph theory, centrality, communities, topology

#### Relevance to Paper
The paper's "Downstream GRN analyses" section discusses topological analysis using network centrality measures to identify important TFs and genes. The paper mentions that centrality measures have been useful for identifying TFs that drive cell fate changes, making NetworkX highly relevant for analyzing inferred GRNs.

---

## Additional Relevant Tools

### GSEApy - Gene Set Enrichment Analysis
- **Relevance**: ⭐⭐⭐⭐
- **Description**: Python implementation of Gene Set Enrichment Analysis (GSEA), mentioned in the paper for inferring TF activities from GRNs
- **Usage**: Enrichment analysis of regulons and gene modules
- **Installation**: `pip install gseapy`

### SCREEN - Candidate Cis-Regulatory Elements
- **Relevance**: ⭐⭐⭐⭐
- **Description**: Database of candidate cis-regulatory elements (cCREs) from ENCODE
- **Usage**: Identify regulatory elements (enhancers, promoters) for genes
- **Access**: Via ToolUniverse `SCREEN_get_regulatory_elements`

### RegulomeDB - Regulatory Variant Annotations
- **Relevance**: ⭐⭐⭐
- **Description**: Database for regulatory variant annotations
- **Usage**: Query regulatory effects of genetic variants (SNPs)
- **Access**: Via ToolUniverse `RegulomeDB_query_variant`

### MuData - Multimodal Annotated Data
- **Relevance**: ⭐⭐⭐⭐
- **Description**: Data structure for storing multiple omics modalities (RNA-seq, ATAC-seq) in unified container
- **Usage**: Store and manage paired multi-omics data
- **Installation**: `pip install mudata`

---

## Tool Integration Workflow

Based on the paper's methodology, here's a recommended workflow integrating these tools:

### Step 1: Data Preprocessing
1. **Scanpy**: Preprocess scRNA-seq data (filtering, normalization, clustering)
2. **episcanpy**: Preprocess scATAC-seq data (peak calling, accessibility analysis)
3. **MuData**: Combine modalities into unified data structure

### Step 2: Multi-Omics Integration
1. **scvi-tools**: Integrate paired or unpaired scRNA-seq and scATAC-seq data
2. **scVelo**: Optional trajectory inference for dynamic processes

### Step 3: GRN Inference
1. **Arboreto/GRNBoost2**: Infer initial co-expression network from expression data
2. **JASPAR**: Access TF binding motifs for motif enrichment
3. **ENCODE/ReMap**: Validate TF binding predictions
4. **pySCENIC**: Complete GRN inference workflow (co-expression → pruning → scoring)

### Step 4: Network Analysis
1. **NetworkX**: Topological analysis, centrality measures, module identification
2. **GSEApy**: Enrichment analysis of regulons and modules

### Step 5: Validation
1. **ENCODE/ReMap**: Compare predicted TF binding with experimental ChIP-seq data
2. **SCREEN**: Validate predicted regulatory elements
3. **RegulomeDB**: Check if variants in predicted CREs have regulatory effects

---

## Installation Summary

### Core Tools (Required)
```bash
# Single-cell analysis
pip install scanpy anndata

# GRN inference
pip install pyscenic arboreto

# Multi-omics
pip install scvi-tools mudata episcanpy

# Network analysis
pip install networkx

# Trajectory analysis (optional)
pip install scvelo
```

### Database Access (via ToolUniverse)
```bash
pip install tooluniverse
```

Then access JASPAR, ENCODE, ReMap, SCREEN, and RegulomeDB through ToolUniverse's API tools.

---

## Key Takeaways

1. **pySCENIC** is the most directly relevant tool, being specifically designed for single-cell GRN inference as described in the paper.

2. **Scanpy** and **episcanpy** are essential for preprocessing single-cell RNA-seq and ATAC-seq data, respectively.

3. **Multi-omics integration** tools like **scvi-tools** and **MuData** are crucial for leveraging both transcriptomics and chromatin accessibility data.

4. **Database tools** (JASPAR, ENCODE, ReMap) provide essential reference data for TF binding motifs and experimental validation.

5. **Network analysis** with **NetworkX** enables downstream topological analysis of inferred GRNs.

6. The paper emphasizes that **combining multiple data modalities** improves GRN inference accuracy, making tools that support multi-omics integration highly valuable.

7. **Validation** is a key challenge discussed in the paper, making database tools for accessing experimental validation data (ENCODE, ReMap) essential.

---

## References

1. Badia-i-Mompel, P., et al. (2023). Gene regulatory network inference in the era of single-cell multi-omics. *Nature Reviews Genetics*, 24, 739-754.

2. ToolUniverse Repository: https://github.com/mims-harvard/ToolUniverse

3. Individual tool documentation and repositories as listed in each tool's section above.

---

## Appendix: Tool Comparison Matrix

| Tool | Primary Function | Data Type | Paper Mention | Installation Difficulty |
|------|-----------------|-----------|---------------|------------------------|
| pySCENIC | GRN Inference | scRNA-seq | ⭐⭐⭐⭐⭐ (8x) | Medium |
| Scanpy | Single-cell Analysis | scRNA-seq | Implicit | Easy |
| Arboreto | GRN Inference | Expression | ⭐⭐⭐⭐ (3x) | Easy |
| scVelo | Trajectory Analysis | scRNA-seq | Related | Medium |
| scvi-tools | Multi-omics Integration | Multi-omics | Related | Medium |
| episcanpy | ATAC-seq Analysis | scATAC-seq | Related | Easy |
| JASPAR | TF Motifs | Database | ⭐⭐⭐⭐⭐ (3x) | Easy (API) |
| ENCODE | Functional Genomics | Database | ⭐⭐⭐⭐⭐ (6x) | Easy (API) |
| ReMap | TF Binding Sites | Database | Related | Easy (API) |
| NetworkX | Network Analysis | Networks | Related | Easy |

---

*Report generated by exploring ToolUniverse repository and analyzing tool relevance to Badia-i-Mompel et al. (2023) paper on GRN inference from single-cell multi-omics data.*

```


Marking the report task as completed:



## Summary

Completed the tool exploration task. Here's what was done:

### Completed tasks

1. Cloned the ToolUniverse repository
2. Analyzed the Badia-i-Mompel et al. (2023) paper to understand its focus on GRN inference from single-cell multi-omics data
3. Identified relevant tools from ToolUniverse
4. Selected the top 10 most relevant tools
5. Generated a markdown report with detailed information

### Top 10 tools identified

1. pySCENIC — GRN inference (directly mentioned in paper)
2. Scanpy — Single-cell analysis (essential preprocessing)
3. Arboreto/GRNBoost2 — GRN inference (mentioned in paper)
4. scVelo — RNA velocity and trajectory inference
5. scvi-tools — Multi-omics integration
6. episcanpy — ATAC-seq analysis
7. JASPAR — TF binding motifs database (mentioned in paper)
8. ENCODE — Functional genomics database (mentioned in paper)
9. ReMap — TF binding sites validation
10. NetworkX — Network topology analysis

### Report contents

The report (`tool_exploration_report.md`) includes:
- Executive summary
- Detailed descriptions of each tool
- Installation instructions
- Usage examples with code
- Relevance to the paper
- Tool integration workflow
- Comparison matrix
- Additional relevant tools

The report is saved at:
`/Users/simonwang/Documents/Usage/AIagent4bio/lab4/demo/tool_exploration_report.md`

All tasks are complete. The report provides information about tools relevant to GRN inference from single-cell multi-omics data, as described in the Badia-i-Mompel paper.

