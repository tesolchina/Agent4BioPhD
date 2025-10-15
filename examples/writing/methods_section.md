# Methods Section Writing Example

This document demonstrates how AI agents can assist in writing different sections of a research paper, using concepts from the Badia-i-Mompel et al. (2023) review as context.

## Example: Methods Section for a GRN Study

### Data Collection and Preprocessing

**Single-cell RNA sequencing data acquisition**

We obtained single-cell RNA sequencing (scRNA-seq) data from [specific tissue/organism] using the 10x Genomics Chromium platform. Libraries were prepared according to the manufacturer's protocol (Chromium Single Cell 3' Reagent Kits v3.1) and sequenced on an Illumina NovaSeq 6000 system with a target depth of 50,000 reads per cell.

**Quality control and filtering**

Raw sequencing reads were processed using Cell Ranger v7.0 (10x Genomics) to generate gene-by-cell expression matrices. Quality control was performed to remove low-quality cells and potential doublets. Specifically, we filtered out cells with:
- Fewer than 200 detected genes
- More than 6,000 detected genes (potential doublets)
- Mitochondrial gene content exceeding 15% of total counts

Following quality control, [X] cells passed filtering criteria and were retained for downstream analysis.

**Normalization and feature selection**

Gene expression counts were normalized using the SCTransform method as implemented in Seurat v4.3, which performs variance stabilization and removes technical variation while preserving biological heterogeneity. We selected the top 2,000 highly variable genes based on variance-stabilized expression values for dimensional reduction and clustering.

### Gene Regulatory Network Inference

**Method selection**

We employed [SCENIC/GRNBoost2/other method] for gene regulatory network (GRN) inference, chosen for its demonstrated performance with single-cell data and ability to identify transcription factor (TF)-target gene relationships. As reviewed by Badia-i-Mompel et al. (2023), regression-based methods like SCENIC show robust performance in inferring cell-type-specific regulatory networks from scRNA-seq data.

**GRN inference procedure**

Network inference was performed separately for each identified cell type to capture cell-type-specific regulatory programs. The analysis pipeline consisted of the following steps:

1. **Co-expression module identification**: We computed pairwise gene correlations using Spearman's rank correlation coefficient and constructed co-expression modules using the GRNBoost2 algorithm with gradient boosting decision trees.

2. **Motif enrichment analysis**: For each putative TF-target relationship, we performed motif enrichment analysis using the RcisTarget database, which contains motif information from JASPAR and other sources. Only TF-target pairs with supporting motif evidence (normalized enrichment score > 3.0) were retained.

3. **Regulon construction**: We defined regulons as sets of genes directly regulated by specific transcription factors, based on combined evidence from co-expression and motif enrichment. Regulons were required to contain at least 10 target genes to ensure statistical robustness.

4. **Activity scoring**: Regulon activity scores were calculated for each cell using the AUCell algorithm, which computes the enrichment of regulon target genes at the top of the cell's gene expression ranking.

**Parameter settings**

All GRN inference analyses were performed with the following parameters:
- Correlation threshold: 0.03
- Number of decision trees: 1,000
- Tree depth: 3
- Motif enrichment NES threshold: 3.0
- Minimum regulon size: 10 genes

### Validation of Inferred Networks

**Comparison with known regulatory relationships**

We validated inferred TF-target relationships against experimentally verified interactions from the following databases:
- ChIP-seq data from the ENCODE project
- Gene Ontology (GO) annotations
- TRRUST v2 (transcriptional regulatory relationships)

Precision and recall were calculated as:
- Precision = (True Positives) / (True Positives + False Positives)
- Recall = (True Positives) / (True Positives + False Negatives)

where True Positives represent inferred interactions confirmed by at least one database.

**Functional enrichment analysis**

To assess the biological relevance of inferred regulons, we performed Gene Ontology (GO) enrichment analysis using the enrichGO function from the clusterProfiler R package (v4.4). Significantly enriched terms (adjusted p-value < 0.05, Benjamini-Hochberg correction) were identified and visualized.

**Cell-type specificity assessment**

We quantified the cell-type specificity of each regulon by computing the Jensen-Shannon divergence (JSD) of regulon activity distributions across cell types. Regulons with JSD > 0.5 were classified as cell-type-specific.

### Network Analysis and Visualization

**Network topology analysis**

We characterized the topology of inferred GRNs using standard network metrics:
- Node degree distribution
- Clustering coefficient
- Network density
- Hub identification (genes with degree > 90th percentile)

Network metrics were computed using the igraph R package (v1.3).

**Visualization**

Gene regulatory networks were visualized using Cytoscape v3.9. Networks were laid out using the force-directed spring-embedded algorithm, with node size proportional to degree centrality and edge width proportional to interaction confidence. TFs were colored by their expression pattern across cell types.

For large networks (>500 nodes), we visualized only high-confidence interactions (confidence score > 0.8) and hub genes to improve interpretability.

### Differential Network Analysis

To identify changes in regulatory networks between conditions (e.g., control vs. treatment, healthy vs. disease), we performed differential network analysis:

1. **Edge-level comparison**: For each TF-target pair, we tested whether the interaction strength differed significantly between conditions using a permutation test (10,000 permutations, p < 0.05).

2. **Regulon activity comparison**: We compared regulon activity scores between conditions using the Wilcoxon rank-sum test with Benjamini-Hochberg correction for multiple testing (adjusted p < 0.05).

3. **Network rewiring identification**: We identified regulatory relationships that were present in one condition but absent in the other (gain/loss of regulation).

### Statistical Analysis

All statistical analyses were performed in R version 4.2.1. P-values were adjusted for multiple testing using the Benjamini-Hochberg false discovery rate (FDR) method unless otherwise noted. Results with adjusted p-value < 0.05 were considered statistically significant.

### Reproducibility

All analysis scripts and code are available at [GitHub repository URL]. The computing environment was managed using renv (v0.17) to ensure reproducibility of package versions. Raw and processed data have been deposited in the Gene Expression Omnibus (GEO) under accession number GSE[XXXXX].

---

## Alternative Versions for Different Contexts

### Condensed Version (for journals with space limitations)

**Gene Regulatory Network Inference**

We inferred gene regulatory networks from scRNA-seq data using SCENIC, which combines co-expression analysis with motif enrichment to identify TF-target relationships. Networks were constructed separately for each cell type (n = [X] cells per type). Regulons (TF-target gene sets) were validated against ChIP-seq data from ENCODE and showed [X]% precision. Network analysis and visualization were performed using igraph and Cytoscape. Statistical significance was assessed at FDR < 0.05.

### Expanded Version (for methods-focused papers)

[Include additional details about:]
- Rationale for method selection with comparison to alternatives
- Detailed parameter optimization procedures
- Sensitivity analyses
- Computational requirements and runtime
- Troubleshooting notes
- Comparison with alternative methods on the same dataset

---

## AI-Assisted Writing Tips

When using AI agents to draft methods sections:

1. **Provide specific details**: Include exact software versions, parameter values, and statistical thresholds

2. **Follow journal guidelines**: Check word limits and formatting requirements

3. **Maintain consistency**: Use the same terminology throughout

4. **Include citations**: Reference methods papers and software tools appropriately

5. **Focus on reproducibility**: Provide enough detail for others to replicate your analysis

6. **Explain choices**: Justify why specific methods were chosen over alternatives

7. **Report validation**: Describe how results were validated or benchmarked

## Common Sections to Include

- [ ] Sample collection and preparation
- [ ] Data generation (sequencing, imaging, etc.)
- [ ] Quality control procedures
- [ ] Data preprocessing and normalization
- [ ] Main analysis methods
- [ ] Validation approaches
- [ ] Statistical analysis
- [ ] Software and tools used
- [ ] Data availability statement
- [ ] Code availability statement

## Checklist for Methods Section Review

- [ ] All methods are described in sufficient detail for reproduction
- [ ] Software versions and parameter settings are specified
- [ ] Statistical tests and significance thresholds are stated
- [ ] Sample sizes are clearly indicated
- [ ] Citations are included for all methods and tools
- [ ] The rationale for method choices is explained
- [ ] Quality control steps are described
- [ ] Data availability is addressed
- [ ] The section flows logically
- [ ] Technical jargon is either defined or commonly understood in the field
