# Experimental Design Examples

This document demonstrates how AI agents can assist in designing experiments for gene regulatory network studies, inspired by concepts from Badia-i-Mompel et al. (2023).

## Overview

Proper experimental design is crucial for obtaining high-quality data for GRN inference. This guide covers key considerations and provides templates for different experimental scenarios.

---

## Scenario 1: Cell-Type-Specific GRN Analysis

### Research Question
How do gene regulatory networks differ between cell types in a developing tissue?

### Experimental Design

#### Sample Collection
- **Tissue source**: Embryonic tissue at developmental stage X
- **Sample size**: 3 biological replicates per time point
- **Cell types of interest**: 5 major cell types identified by marker expression
- **Quality criteria**: Cell viability > 90%, minimal dissociation stress

#### Single-Cell RNA-seq Design
- **Platform**: 10x Genomics Chromium (3' v3.1 chemistry)
- **Target cells**: 5,000 cells per sample
- **Sequencing depth**: 50,000 reads per cell
- **Total cells**: ~75,000 cells (15 samples × 5,000 cells)

#### Multi-Omics Integration (Optional Enhancement)
- **ATAC-seq**: Parallel chromatin accessibility profiling
- **Method**: 10x Multiome (joint RNA + ATAC)
- **Benefit**: Direct evidence of regulatory potential

#### Controls
1. **Technical controls**:
   - Empty droplets for background estimation
   - Cell type markers to validate cell identity
   - Sequencing depth across samples

2. **Biological controls**:
   - Include well-characterized cell types as reference
   - Validate with known marker genes

#### Power Analysis
- **Minimum cells per cell type**: 200 cells
- **Minimum genes per cell**: 500 detected genes
- **Expected genes**: 20,000 genes, ~3,000 variable genes

---

## Scenario 2: Temporal Network Dynamics

### Research Question
How does the gene regulatory network evolve during cell differentiation?

### Experimental Design

#### Time Course Design
- **Time points**: 0h, 6h, 12h, 24h, 48h, 72h post-induction
- **Sampling strategy**: Dense early sampling (more dynamic changes)
- **Replicates**: 3 biological replicates per time point
- **Total samples**: 18 samples

#### Considerations
1. **Temporal resolution**: Balance between:
   - Capturing dynamic changes (frequent sampling)
   - Experimental feasibility (limited by resources)
   - Statistical power (sufficient replicates)

2. **Synchronization**: 
   - Ensure cells start at similar developmental stage
   - Use inducible system if possible
   - Monitor synchrony with marker genes

#### Data Collection
- **scRNA-seq at each time point**
- **Cell count**: 3,000 cells per time point
- **Trajectory analysis**: Pseudotime ordering within time points

#### Analysis Strategy
1. Infer GRN at each time point separately
2. Identify time-varying regulatory relationships
3. Cluster genes by temporal expression pattern
4. Map regulons to differentiation trajectories

---

## Scenario 3: Perturbation-Based Network Validation

### Research Question
Which predicted regulatory relationships are causal?

### Experimental Design

#### Perturbation Strategy
- **Method**: CRISPR interference (CRISPRi) or knockout
- **Targets**: Top 20 predicted transcription factors (TFs)
- **Controls**: Non-targeting guides, scrambled sequences

#### Screening Design
1. **Primary screen**:
   - Perturb each TF individually
   - Measure transcriptome response (scRNA-seq or bulk RNA-seq)
   - 3 biological replicates per perturbation

2. **Validation screen**:
   - Focus on top hits from primary screen
   - Higher sequencing depth
   - Include time course (0h, 24h, 48h post-perturbation)

#### Sample Size Calculation
```
Primary screen:
- 20 TFs × 3 replicates = 60 perturbation samples
- 3 control replicates
- Total: 63 samples

Validation screen:
- 5 TFs × 3 time points × 3 replicates = 45 samples
- 3 time points × 3 control replicates = 9 samples
- Total: 54 samples
```

#### Validation Metrics
1. **Direct targets**: Should show significant expression change
2. **Indirect targets**: May show delayed or smaller changes
3. **Non-targets**: Should show minimal change
4. **Network topology**: Compare perturbed vs. unperturbed networks

---

## Scenario 4: Disease vs. Healthy Network Comparison

### Research Question
How does the gene regulatory network change in disease?

### Experimental Design

#### Sample Collection
- **Healthy controls**: n=10 individuals
- **Disease cases**: n=10 matched patients
- **Matching criteria**: Age, sex, disease stage
- **Tissue**: Same tissue type from both groups

#### Experimental Considerations
1. **Batch effects**:
   - Process samples from both groups simultaneously
   - Randomize sample processing order
   - Include batch information in analysis

2. **Confounding factors**:
   - Age, sex, medication use
   - Collection time, storage conditions
   - Disease heterogeneity

#### Data Collection
- **Single-cell resolution**: Capture cell-type-specific changes
- **Depth**: 5,000 cells per sample minimum
- **Quality**: Stringent QC to remove low-quality cells

#### Analysis Strategy
1. Identify shared cell types between conditions
2. Infer GRN separately for each condition
3. Compare network topology and hub genes
4. Identify disease-specific regulatory relationships
5. Validate key differences with functional assays

---

## General Experimental Design Principles

### 1. Define Clear Objectives
- [ ] Specific biological question
- [ ] Expected outcomes
- [ ] Success criteria
- [ ] Alternative interpretations

### 2. Optimize Sample Size
Use power analysis to determine minimum sample size:
```
Factors to consider:
- Expected effect size
- Desired statistical power (typically 0.8)
- Significance level (typically 0.05)
- Technical and biological variability
```

### 3. Include Appropriate Controls

**Positive controls**:
- Known regulatory relationships
- Well-characterized cell types or conditions

**Negative controls**:
- Non-targeting perturbations
- Unrelated cell types or tissues

**Technical controls**:
- Batch effects monitoring
- Sequencing depth controls
- Quality metrics

### 4. Plan for Validation
- Independent experimental methods
- Different biological systems
- Literature comparison
- Functional assays

### 5. Consider Cost-Benefit Trade-offs

| Aspect | Low Cost | Medium Cost | High Cost |
|--------|----------|-------------|-----------|
| Sequencing depth | 10K reads/cell | 50K reads/cell | 100K+ reads/cell |
| Cell number | 1K cells | 5K cells | 10K+ cells |
| Replicates | 2 replicates | 3 replicates | 5+ replicates |
| Multi-omics | RNA only | RNA + ATAC | RNA + ATAC + Protein |

**Recommendation**: Start with medium cost to balance data quality and resources.

---

## Experimental Design Checklist

### Before Starting
- [ ] Clear research question defined
- [ ] Literature review completed
- [ ] Method selection justified
- [ ] Power analysis performed
- [ ] Budget and timeline approved
- [ ] Ethical approvals obtained (if applicable)

### Sample Collection
- [ ] Sample size determined
- [ ] Collection protocol standardized
- [ ] Quality control criteria defined
- [ ] Storage conditions optimized
- [ ] Metadata template prepared

### Data Generation
- [ ] Sequencing platform selected
- [ ] Sequencing depth determined
- [ ] Library preparation protocol tested
- [ ] Quality metrics defined
- [ ] Backup plan for failed samples

### Analysis Plan
- [ ] Analysis pipeline identified
- [ ] Software tools selected
- [ ] Computational resources available
- [ ] Validation strategy defined
- [ ] Timeline for analysis established

### After Experiment
- [ ] Data quality assessment
- [ ] Metadata properly recorded
- [ ] Raw data backed up
- [ ] Analysis reproducible
- [ ] Results validated

---

## Common Pitfalls to Avoid

### 1. Insufficient Replicates
**Problem**: Low statistical power, unreliable results

**Solution**: Use power analysis, aim for at least 3 biological replicates

### 2. Batch Effects
**Problem**: Technical variation overwhelms biological signal

**Solution**: Randomize samples, process together, include batch in analysis

### 3. Low Sequencing Depth
**Problem**: Miss lowly expressed genes, poor network inference

**Solution**: Pilot experiment to determine optimal depth, budget accordingly

### 4. Poor Quality Control
**Problem**: Low-quality cells bias results

**Solution**: Establish stringent QC criteria, document decisions

### 5. Lack of Validation
**Problem**: Computational predictions may not be biologically accurate

**Solution**: Plan validation experiments from the start

---

## Example Timeline

### 3-Month Project Timeline

**Month 1: Preparation**
- Weeks 1-2: Literature review, experimental design
- Weeks 3-4: Sample collection, library preparation

**Month 2: Data Generation**
- Weeks 5-6: Sequencing
- Weeks 7-8: Initial QC and analysis

**Month 3: Analysis and Validation**
- Weeks 9-10: Network inference and analysis
- Weeks 11-12: Validation experiments and manuscript preparation

---

## Resources for Experimental Design

### Software Tools
- **Power analysis**: R package `pwr`, G*Power
- **Sample size**: scPower for single-cell studies
- **Experimental design**: R package `DeclareDesign`

### Literature
- Badia-i-Mompel et al. (2023) - GRN inference methods review
- ENCODE Consortium - Best practices for functional genomics
- Single Cell Best Practices - Community guidelines

### Databases
- GEO - Find similar studies and typical parameters
- ENCODE - ChIP-seq data for validation
- GTEx - Tissue-specific expression for reference

---

## Conclusion

Effective experimental design requires:
1. Clear research question
2. Appropriate methods
3. Sufficient sample size
4. Proper controls
5. Validation strategy
6. Realistic timeline and budget

AI agents can help by:
- Suggesting experimental parameters
- Identifying potential pitfalls
- Providing template protocols
- Organizing design considerations
- Estimating required resources

This accelerates the design process while ensuring rigor and reproducibility.
