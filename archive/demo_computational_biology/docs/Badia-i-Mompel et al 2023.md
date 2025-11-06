Nature Reviews Genetics
View all journals
Search
Log in
Explore content
About the journal
Publish with us
Sign up for alerts
RSS feed
nature  
nature reviews genetics  
review articles  
article
Gene regulatory network inference in the era of single-cell multi-omics
Download PDF
Review Article
Published: 26 June 2023
Gene regulatory network inference in the era of single-cell multi-omics
Pau Badia-i-Mompel, Lorna Wessels, Sophia Müller-Dott, Rémi Trimbour, Ricardo O. Ramirez Flores, Ricard Argelaguet & Julio Saez-Rodriguez 
Nature Reviews Genetics volume 24, pages739–754 (2023)Cite this article
71k Accesses
293 Citations
225 Altmetric
Metricsdetails
Abstract
The interplay between chromatin, transcription factors and genes generates complex regulatory circuits that can be represented as gene regulatory networks (GRNs). The study of GRNs is useful to understand how cellular identity is established, maintained and disrupted in disease. GRNs can be inferred from experimental data — historically, bulk omics data — and/or from the literature. The advent of single-cell multi-omics technologies has led to the development of novel computational methods that leverage genomic, transcriptomic and chromatin accessibility information to infer GRNs at an unprecedented resolution. Here, we review the key principles of inferring GRNs that encompass transcription factor–gene interactions from transcriptomics and chromatin accessibility data. We focus on the comparison and classification of methods that use single-cell multimodal data. We highlight challenges in GRN inference, in particular with respect to benchmarking, and potential further developments using additional data modalities.
Similar content being viewed by others

Gene regulatory network reconstruction: harnessing the power of single-cell multi-omic data
Article Open access
19 October 2023

Inferring gene regulatory networks from single-cell multiome data using atlas-scale external data
Article Open access
12 April 2024

Modeling gene regulatory networks using neural network architectures
Article 22 July 2021
Introduction
Cells regulate gene transcription to coordinate cellular activities in response to intracellular and extracellular signals. Transcription is largely regulated by transcription factors (TFs), proteins that bind to specific sequences of DNA (DNA binding sites) and can have positive or negative effects on the transcriptional rate of target genes1. Genomic DNA is tightly packed with structural proteins into complexes known as nucleosomes, which are the basic unit of chromatin, making most genes inaccessible to the transcription machinery. To enable transcription, the region near a gene transcription start site, known as the promoter, needs to be exposed by displacing tightly packed nucleosomes. Changes in DNA accessibility can be triggered by the binding of so-called pioneer TFs2. Other TFs can bind to distal cis-regulatory elements (CREs) of the DNA and, together with cofactors and other proteins, cooperatively enable the recruitment and stabilization of the RNA polymerase protein complex that synthesizes mRNA from the gene body DNA (Fig. 1a).
Fig. 1: Principles of gene regulatory networks.
figure 1
a, Gene regulation and its key elements. Transcription factors (TFs) bind to promoter regions and cis-regulatory elements (CREs), displacing nucleosomes and making the transcription start site accessible. Cooperation between TFs, cofactors and other proteins allows for the recruitment and stabilization of the RNA polymerase protein complex, which synthesizes mRNA from the gene body DNA. b, Gene regulatory networks (GRNs) can be inferred from measured omics data and, through the modelling of additional information such as TF binding predictions or chromatin accessibility, can be refined to better resemble the true underlying GRN. The nodes of the GRN are TFs and their regulated genes, and the edges between nodes indicate the mode of regulation (activation or inhibition). c, GRNs generated from single-cell omics data allow to understand cell type and state specificity, explain the progression of dynamic trajectories and identify differences between conditions.
Full size image
Gene regulatory networks (GRNs) are interpretable computational models of the regulation of gene expression in the form of networks, mathematically also defined as graphs. Multiple components of gene regulation, such as TFs, splicing factors, long non-coding RNAs, microRNAs and metabolites, can be incorporated in GRNs. Here, we focus on their simplest representation, which captures only the interplay between TFs and target genes, whereby the nodes of the GRN consist of genes, some of them being TFs, and the edges of the GRN represent regulatory interactions between the genes (Fig. 1b). Other possible GRN representations are discussed elsewhere3,4,5,6. Uncovering the topology and the dynamics of GRNs is fundamental to understanding how cellular identity is established and maintained7, which has important implications for engineering cell fate8 and for disease prevention9.
Understanding GRNs is a long-standing quest in biology, as illustrated by the seminal work from the 1960s characterizing the bacterial lactose (lac) operon10. Reconstructing large-scale GRNs became a major focus of systems biology, leveraging various high-throughput experimental methods and computational algorithms11,12,13. Historically, GRNs have been commonly assembled from experimentally validated regulation events compiled in databases14,15,16,17 or inferred de novo from gene co-expression in bulk transcriptomics data18,19,20. If sufficient transcriptomics data are available, GRNs can be inferred that are better contextualized for the biological question at hand than GRNs extracted from databases, which tend to be generalistic. However, transcriptomics data do not directly capture many underlying regulatory mechanisms, such as the TF protein abundance and DNA binding events, cooperation of TFs and cofactors, alternative transcript splicing, post-translational protein modification events and the accessibility and structure of the genome. The inclusion and measurement of these other aspects of gene regulation has the potential to generate GRNs that better represent gene regulation in vivo (Fig. 1b). For example, the inclusion of chromatin accessibility21 data allows to fine-tune TF–gene links by considering whether genes are open and by including CREs in the inference of GRNs.
Furthermore, bulk profiling provides mixed measures across cell types in a tissue sample, and thus cannot disentangle regulatory programmes specific to particular cell types or cell states22,23. This limitation has been overcome by the use of single-cell technologies24,25, allowing the inference of GRNs across different cell types, differentiation trajectories and conditions (Fig. 1c). For this reason, and with the introduction of multimodal profiling technologies26,27,28, there has been a recent explosion of novel GRN inference methods.
In this Review, we outline general principles of GRN inference and their potential limitations. Furthermore, we describe how multimodal read-outs can be leveraged to infer more accurate GRNs, and we classify and briefly describe several novel tools that have been developed for this task. In addition, we highlight possible downstream GRN analyses and how to assess experimentally the obtained results. Finally, we discuss current challenges and future directions in the field.
Inference of GRNs
GRN inference refers to the process of summarizing gene regulation — a highly complex and dynamic process — into an interpretable network structure from data using computational methods. It is based on the assumption that the effects of a true underlying GRN can be observed and measured in molecular data29 (Fig. 1b). Interactions in GRNs can be directed or undirected (denoting a causality relationship between genes or lack of it, respectively), signed (denoting the mode of regulation, positive or negative) and/or weighted (denoting the strength of the interaction).
From transcriptomics data
Methods in this category fit models that try to explain the observed variability of gene expression based on the expression of other genes. Weighted gene co-expression network analysis (WGCNA)19 is one of the simplest and most popular approaches. It carries out pairwise correlations across the whole transcriptome to identify modules of co-expressed genes. The resulting network is commonly known as a gene co-expression network and its interactions are undirected owing to the symmetrical nature of correlations. Although this strategy is useful to identify gene modules in an unsupervised manner, the lack of causal regulatory links hinders its interpretability and typically yields a large number of false positive associations. To address these limitations, methods such as GENIE3 (ref. 20) and its faster implementation GRNBoost2 (ref. 30) first distinguish TFs from target genes based on previously reported regulatory activity31 and then train models that predict the expression of target genes based solely on the expression of TFs, which markedly reduces the number of interactions to be considered. By doing so, undirected interactions are turned into directed connections and thus introduce putative causal relationships. Nevertheless, inference from transcriptomics data alone introduces false positives as many other mechanisms that are involved in gene regulation, such as chromatin accessibility, are ignored. Moreover, because many processes are required for a mRNA transcript encoding a TF to become a functional protein, transcript levels alone might not be informative enough1,32. These limitations may hinder the inference process, as it has been shown that, overall, these methods tend to have moderate success in accurately inferring GRNs33,34,35.
From TF binding data or chromatin accessibility
Assays such as chromatin immunoprecipitation followed by sequencing (ChIP-seq)36 and cleavage under targets and tagmentation (CUT&Tag)37 enable TF binding to be measured across the genome. This information can be used to build GRNs directly by assigning TF binding sites to putative target genes38. However, despite some high-throughput alternatives39,40,41, profiling of TF binding is still costly and limited to TFs for which antibodies are available. In addition, the use of TF binding data alone typically requires the assignment of bound TFs to their target genes by closest genomic proximity, ignoring possible distal interaction events that are known to be relevant in gene regulation1. By contrast, a pioneering study explored the integration of ChIP-seq data and transcriptomics data to enable a more refined assignment of TFs to genes that did not depend on the closest gene42.
An alternative approach is to use chromatin accessibility data to infer gene regulatory elements that are potentially targeted by TFs. The most commonly used technology owing to its simple and relatively cheap protocol is the assay for transposase accessible chromatin with sequencing (ATAC-seq)21, but other technologies exist such as DNase-seq43 and NOME-seq44 (reviewed elsewhere45). Methods that leverage chromatin accessibility data split GRN inference into two steps: first, the assignment of TFs to gene regulatory elements (open chromatin regions, commonly referred to as peaks); and second, the assignment of these regulatory elements to genes (Fig. 2). For the first step, methods leverage TF binding motif databases and motif matcher algorithms to make binding predictions for TFs on accessible CREs (Box 1). For the second step, methods link accessible CREs to genes that are within a certain genomic distance. The distance cutoff is based on the observation that distal CREs such as enhancers or silencers generally interact with the promoter regions of genes at a typical distance1. Some examples of such inference methods include ATAC2GRN (ref. 46), LISA47 and SPIDER48. These methods assume that if the promoter region of a gene is accessible, the gene is being transcribed, but that might not always be the case.
Fig. 2: Flow chart of methods for gene regulatory network inference.
figure 2
Methods for gene regulatory network (GRN) inference involve different steps depending on the data modalities generated for the samples or cells being studied. Transcriptomics data are first preprocessed and normalized to build a gene expression matrix, containing the transcript levels of each gene across samples or cells. A list of known transcription factor (TF) genes is obtained from other sources to distinguish genes with regulatory capabilities. Interactions between TFs and target genes are then inferred by building models that try to predict the observed gene expression from TF transcript abundance, generating TF–gene associations. Finally, the obtained interactions are aggregated and represented as a GRN. Chromatin accessibility data are first preprocessed and peaks are called to build a peak accessibility matrix, containing binary information about the openness of cis-regulatory elements (CREs) across samples or cells. CREs are associated with genes based on genomic distance limits, and TFs are predicted to bind to CREs using TF binding motif databases and motif matcher algorithms. Together, this information is used to obtain TF–CRE–gene triplets. Finally, these interactions are simplified into TF–gene pairs and aggregated into a GRN. When samples are profiled by both transcriptomics and chromatin accessibility (multi-omics data), preprocessing of each modality is carried out and, if needed, the unpaired modalities are integrated. Having both modalities available, methods can simultaneously leverage the three aforementioned modelling steps to build TF–CRE–gene triplets, which then are simplified and aggregated into a GRN.
Full size image
Box 1 Binding motif databases and motif matcher algorithms
Generating genome-wide binding data for multiple transcription factors (TFs) requires laborious experiments, so methods for gene regulatory network (GRN) inference instead predict TF binding events on open genomic regions based on prior information. This information comes from a large collection of TF–DNA binding assays, such as chromatin immunoprecipitation followed by sequencing (ChIP-seq) experiments36, that can be used to extract the most likely genomic sequence to which a given TF specifically binds, commonly known as a TF binding motif208. Several databases have collected such assays and generated TF binding motif collections for model organisms. Because coverage between databases may vary, they can be merged to increase the number of TFs considered in the GRN inference process. Moreover, several computational algorithms have been developed that leverage TF binding motifs to predict binding events, known as motif matcher algorithms. All of these algorithms are based on computing the probability of a TF binding event from the motif sequence and filtering the significant ones. Because the different methods model TF binding differently, results may vary between them and should be considered during GRN inference. The table lists the TF binding motif databases and motif matcher algorithms used across the reviewed methods.
Name
URL
Refs.
Binding motif databases
CIS-BP
http://cisbp.ccbr.utoronto.ca/
209
cisTarget databases
https://resources.aertslab.org/cistarget/databases/
67
ENCODE
https://www.encodeproject.org/software/encode-motifs/
210
HOCOMOCO
https://hocomoco11.autosome.org/
211
JASPAR
https://jaspar.genereg.net/
212
TRANSFAC
https://genexplain.com/transfac/
213
UniPROBE
http://thebrain.bwh.harvard.edu/uniprobe/
214
Motif matcher algorithms
FIMO
https://snystrom.github.io/memes-manual/
215
GimmeMotifs
https://gimmemotifs.readthedocs.io/
216
HOMER
http://homer.ucsd.edu/homer/motif/
68
MOODs (as implemented in motifmatchr)
https://github.com/jhkorhonen/MOODS
https://github.com/GreenleafLab/motifmatchr
217, 218
motifanalysis (as implemented in reg-hint)
https://reg-gen.readthedocs.io/
219
PIQ toolkit
https://bitbucket.org/thashim/piq-single/src/master/
220
PWMScan
https://ccg.epfl.ch/pwmtools/pwmscan.php
221
pycisTarget
https://pycistarget.readthedocs.io/
67
Show less
From single-cell transcriptomics data
GRN inference methods using bulk omics data have enabled the characterization of genome-wide regulatory events but, in the case of mixed samples such as tissues, they cannot capture the cell type or state specificity of GRNs22,23. In addition, GRN inference methods require large sample sizes to generate sufficient data, which can become prohibitively costly in bulk profiling.
With the emergence of single-cell technologies, particularly single-cell RNA sequencing (scRNA-seq), GRN reconstruction methods have been used to infer cell type-specific TF–gene interactions, together with the dynamic changes that occur in these GRNs across development and conditions49 (Fig. 1c). One of the first GRN inference methods tailored to scRNA-seq data was SCENIC50, an extension to the GRNBoost2 (ref. 30) method, which generates cell type-specific GRNs by exploiting TF–gene co-expression patterns and, in addition, prunes the edges of the GRN based on TF binding motif enrichment on gene promoter regions. The improved resolution of single-cell measurements also enables the identification of dynamic cell states and their transitions that may not be easily differentiated into distinct groups, such as during development, cell differentiation or disease progression51,52. Pseudotime ordering characterizes these continuous changes and can be used to inform GRN inference. The resulting GRNs provide valuable insights into the complex processes involved in key fate decisions. LEAP53 and SINCERITIES54 are examples of GRN inference methods that leverage pseudotime ordering to infer the directionality between genes in the GRNs. The use of contrast-level statistics obtained after differential testing55,56 is an effective means of identifying differences between conditions, such as between healthy individuals and a cohort of patients with disease. This strategy differs from computing differences between GRNs, as explained in the later section describing ‘Downstream GRN analyses’.
Recent advances in single-cell chromatin accessibility profiling (such as single-cell ATAC-seq (scATAC-seq))57, which can be carried out together with single-cell transcriptomics26,27,28, have allowed for the refinement of GRN reconstruction at an unparalleled definition. Some early works inferred GRNs from unpaired multi-omics data to study human myeloid cell differentiation58, mouse embryonic development59 and HIV infection of dendritic cells60. However, they did not provide their method implemented as a tool for others to use. These were followed by an explosion of novel methods for GRN inference that leverage both scRNA-seq and scATAC-seq (Table 1 and Fig. 2; see Supplementary Box 1). The multimodal data used for GRN inference can be paired if both measurements come from the same cell or unpaired if they come from different cells. Some methods do not require matching chromatin accessibility and gene expression profiles for each cell, as they either summarize read-outs across groups of cells or build GRNs independently for each modality followed by a merging step. By contrast, other methods model both modalities in the same cell simultaneously. In these ‘simultaneous’ methods, unpaired data can still be modelled if both modalities are matched using integration approaches61. To facilitate usage, some of these methods (for example, DeepMAPS62, FigR63, GLUE64, scAI65 and SOMatic66) implement their own integration approach.
Table 1 Existing tools for inference of gene regulatory networks from multi-omics data
Full size table
Multimodal GRN inference methods use an extended framework to that used by single-modality methods to reconstruct GRNs. Specifically, they predict gene expression from TF gene expression, they assign TFs to accessible CREs using binding motif information and they associate CREs with target genes constrained by genomic distance (Fig. 2). For the prediction of TF binding events, different methods use different, highly heterogeneous TF binding motif databases and prediction algorithms (Table 1 and Box 1). As TF binding motif databases have different coverage of TFs, and prediction algorithms model binding differently, results between GRN inference methods might differ even if they use similar modelling strategies. The majority of methods allow for using different TF binding motif databases than their default, but most methods fix the motif matcher algorithm used — except for SCENIC+67, which implements three algorithms, cisTarget67, DEM67 and HOMER68. In addition, GRN inference methods use different genomic distance cutoffs to assign open chromatin regions to target genes. Some consider close distances up to 10 kb, others medium distances up to 100 kb, others large distal effects up to 1,000 kb and others do not specify the distance cutoff either in the original publication or in the source code (Table 1). Given that functionally validated interactions are greatly enriched at the closest distances, and that they substantially fall off by 100 kb1,69, differences in distance cutoffs will likely affect the resulting inferred GRN.
After carrying out the above steps (Fig. 2), multimodal GRN inference methods generate a candidate scaffold network made up of triplets of a TF associated with a CRE that is linked to a target gene. To generate a final GRN structure, different mathematical strategies are used. Some of these strategies assume a linear relationship between TFs, CREs and genes, and others assume a non-linear relationship (Table 1). Linear modelling assumes that one variable, for example gene transcripts, changes in direct proportion to another variable, for example TF transcripts or CRE openness. By contrast, non-linear modelling can accommodate more complex interactions between variables such as synergistic effects70. Although it is widely acknowledged that gene expression is a non-linear process70, linear modelling of GRNs is often preferred owing to its simplicity in formulation and interpretation. Independently of the modelling strategy used, the significance of the obtained regulatory interactions can be assessed using either frequentist or Bayesian probability statistical frameworks (Table 1). A frequentist approach defines the probability of an event as the proportion of times that the event occurs in a large number of identical experiments, whereas Bayesian probability defines it as a measure of confidence in the occurrence of the said event based on both observed data and previous information. Bayesian methods can take into account available prior knowledge but they usually require larger computational resources than frequentist approaches, which can be a limitation when inferring genome-wide GRNs with large-scale single-cell data. In addition, the success of Bayesian inference depends on the quality of the prior knowledge used. Therefore, when no prior information is available or it is suspected to be inaccurate, frequentist inference might be more accurate.
Multimodal GRN inference methods can be grouped based on the combination of their modelling strategy and the types of input they accept (Table 1). The majority of methods are designed to model GRNs across distinct groups, usually cell types, by frequentist regression. FigR63 and GRaNIE71, among others, use frequentist linear regression; DIRECT-NET72 and SCENIC+67 use frequentist non-linear regression (random forest); and PECA73 and Symphony74,75 use Bayesian modelling. By contrast, CellOracle76, Inferelator 3.0 (ref. 77) and Pando78 offer multiple modelling strategies to the user. In case no distinct groups can be defined from the data owing to its continuous nature, for example in cell development, scMEGA79 and IReNA80 leverage trajectories to infer GRNs linearly and non-linearly, respectively. Also, Dictys81, scMTNI82 and TimeReg83 use a combination of both cell type grouping and trajectory data to inform the GRN modelling, whereas CellOracle76 and SCENIC+67 use the latter to carry out downstream analyses. ANANSE84, sc-compReg85 and SCENIC+67 build group-specific (for example, cell type-specific) GRNs but can also leverage gene contrast statistics during the inference process.
Downstream GRN analyses
Once GRNs have been inferred from any resolution and combination of omics data, they can be queried using various downstream analyses to provide novel biological insights (Fig. 3 and Box 2).
Fig. 3: Applications of gene regulatory networks.
figure 3
a, Topological analysis. Network centrality measures can be used to identify hubs of transcription factors (TFs) or genes within a gene regulatory network (GRN) that are highly connected. Clustering of nodes based on their connectivity gives rise to sub-network modules that can be associated with biological functions. b, Comparative analysis. Comparison of the connectivities in different GRNs by the pairwise subtraction of TF–gene interactions between GRNs can provide insight into the rewiring of gene regulation between different cell types, individuals, conditions or organisms. c, Inference of TF activity. GRNs can be coupled to enrichment methods to infer which TFs might be functionally active from transcriptomics data. GRNs inferred from multi-omics data can then be used to infer TF activities in other contexts, such as independent single-cell, spatial or bulk transcriptomics data. d, In silico perturbation experiments. GRNs can be used to simulate perturbation experiments by propagating changes in gene expression through the network over short iterations. The obtained simulated gene expression profiles can then be used to infer cell fate decisions.
Full size image
Box 2 Successful applications of gene regulatory networks derived from single-cell multi-omics data
Gene regulatory networks (GRNs) have been used in various contexts to answer a range of research questions; here, we summarize some recent examples.
A multimodal time course of human brain organoids was generated using single-cell RNA sequencing (scRNA-seq) and single-cell assay for transposase accessible chromatin with sequencing (scATAC-seq)78. Using the GRN inference tool Pando, the authors predicted transcription factor (TF) binding sites and inferred a global GRN underlying organoid development. By making in silico predictions from the GRN followed by a CRISPR-based screen, they identified GLI3 as an essential TF for cortical fate establishment.
A multimodal atlas of the fly brain was generated using scRNA-seq and scATAC-seq, and characterized developmental, reprogramming and maturation trajectories222. Using a deep learning model trained on the omics data, the authors inferred cell type-specific TF binding predictions and used this to decode the regulatory grammar of enhancer architectures that underlie neuronal diversity.
CellOracle was introduced as a mathematical model to carry out in silico TF perturbations from GRNs trained using single-cell multi-omics data76. In the context of zebrafish development, the authors made systematic predictions of TF knockouts, which allowed the identification of new roles for key regulators of early zebrafish development, including noto and lhx1a.
A multimodal atlas of mouse early organogenesis was built by profiling gene expression and chromatin accessibility from individual cells87. The authors developed in silico chromatin immunoprecipitation followed by sequencing (ChIP-seq), a method to predict TF binding sites, and used it to characterize the GRNs underlying the transition of neuromesodermal progenitors to somitic mesoderm. Using the CellOracle76 framework for in silico predictions, followed by experimental validation, they characterized a role of Brachyury in priming cis-regulatory elements (CREs) for differentiation.
scRNA-seq and scATAC-seq were carried out on cortical tissue from patients with Alzheimer disease90. By modelling relationships between TFs, CREs and target genes, the authors identified ZEB1 and MAFB as candidates involved in gene regulation and, potentially, disease progression in neurons and microglia.
Inferelator 3.0 (ref. 77) was used to infer GRNs for several CD4+ memory T cell populations from mice and the results were benchmarked by curating TF knockout and ChIP-seq data for 42 of the identified TFs223. The authors integrated the obtained GRNs with cell–cell communication networks, and functionally validated a regulatory circuit involving IL-6, MAF and CD153 in T follicular helper cells that is important for antibody-mediated vaccine responses in aged mice.
Show less
Topological analysis
Although GRNs are simple and interpretable models of gene regulation, they can still contain large numbers of genes and an even larger number of interactions between them. Network centrality measures can help identify which TFs or genes are more important for the connectivity or the information flow of the network (Fig. 3a). Some examples of network centrality measures include degree centrality, closeness centrality, betweenness centrality and eigenvector centrality. These measures have been useful to identify TFs that drive cell fate changes in diverse biological contexts, such as direct lineage reprograming76, human myocardial infarction86 and mouse development87.
Another approach to characterize the topology of GRNs is using methods based on spectral graph theory, which explore the properties of a network when represented as a matrix. For example, non-negative matrix factorization applied to the adjacency matrices of GRNs has identified groups of TFs that cooperatively drive lineage transitions in mouse embryonic stem cells83,88. Similarly, clustering of GRN topology identified known regulators in human haematopoietic cell differentiation70 and in the response of macrophages to interferon-γ71. The gene regulatory modules that are obtained can then be enriched for gene sets to characterize their potential biological functions89.
Comparative analysis
Comparative analysis of GRNs can uncover the rewiring events that drive differences between cell types, cell states, disease states, treatment approaches and organisms (Fig. 3b). The easiest method for comparative analysis involves the pairwise subtraction of TF–gene interactions between GRNs. This methodology has identified key regulators in subpopulations of B cells in patients with lymphocytic leukaemia85, groups of TFs for transdifferentiation of fibroblasts to different human cell types84, candidate Alzheimer disease-specific trans-regulators90 and cell state-specific regulators in human T cells74,75. It has also been used to assess evolutionary conservation of TF–gene interactions and adaptation of transcriptional regulation across species91. However, owing to the sparse and noisy nature of GRNs, direct comparison of TF–gene interactions is often not sufficiently robust. Topic modelling strategies such as latent Dirichlet allocation92, an unsupervised Bayesian model that was originally developed for natural language processing, allow for generating dense, low-dimensional representations that filter noise in the structure of the GRN, and thus capture more robustly the differences in regulatory relationships. This strategy has been useful for predicting the survival of patients with cancer93 and for identifying rewiring events in human haematopoiesis82.
Inference of TF activities
GRNs can be coupled with enrichment methods to infer TF activities from transcriptomics data15,50,94,95. This approach allows for the observed gene expression to be integrated with the GRN topology to extract which TFs might have relevant roles in certain contexts (Fig. 3c). Common enrichment methods include GSEA96, AUCell50 and VIPER94, among others95. In bulk studies, inference of TF activities through enrichment methods has enabled, for example, the identification of druggable oncoproteins94, stratification of cell lines in response to drug treatment97 and identification of a master regulator as a metastasis promoter in breast carcinoma98. In single-cell studies, enrichment methods have identified a novel mechanism of immunotherapy resistance in human T cells99, regulators and inducers of oligodendroglioma50, and potential druggable targets for pathological fibroblasts in patients with COVID-19 (ref. 100). These methods have also been recently applied to spatially resolved transcriptomics data, for example to suggest regulators involved in the functional transition of cardiomyocytes across the border zone that surrounds ischaemic lesions in human myocardial infarction86.
Perturbation and prediction of cell fate
GRNs can be used to simulate gene expression values over time by propagating TF expression to target genes in an iterative manner. With this framework, in silico perturbations can be carried out by changing the expression of a candidate TF and then observing how it affects the resulting transcriptome after a given number of iterations (Fig. 3d). Afterwards, the simulated values can be compared with the gene expression of local neighbouring cells to estimate cell identity transition probabilities analogous to RNA velocity analysis101. First introduced by CellOracle76, this strategy suggested the role of Zfp57 in generating and maintaining mouse induced endoderm progenitors, which was later experimentally validated with in vitro perturbation experiments. SCENIC+67 used a similar strategy to identify RUNX3 as a potential driver of melanocytes to mesenchymal melanoma cells, showcasing the ability of GRNs to capture and model complex regulatory events.
Experimental assessment of GRNs
The connections predicted by GRN inference methods should be seen as hypothetical regulatory interactions that must be assessed by complementary information and/or experiments. In this section, we discuss common practices for this purpose (Fig. 4).
Fig. 4: Experimental assessment of gene regulatory networks.
figure 4
Although there is no clear ‘ground truth’ for gene regulation, several experiments and analyses can be carried out to validate specific aspects of gene regulatory networks (GRNs). Interactions between transcription factors (TFs) can be queried in protein–protein databases for TFs that share large numbers of target genes and are assumed to interact. The presence of TF protein can be confirmed by proteomic assays, and the activation state of TFs can be assessed in targeted phosphorylation experiments. Links between TFs and cis-regulatory elements (CREs) can be confirmed by binding assays, such as chromatin immunoprecipitation followed by sequencing (ChIP-seq), cleavage under targets and tagmentation (CUT&Tag) and CAP-SELEX. Candidate CREs can be tested for regulatory capability with reporter assays or perturbation experiments. Alternatively, functional CREs can be assumed to be evolutionarily conserved or to be enriched in disease-associated loci as identified by genome-wide association studies. Links between CREs and genes can be evaluated experimentally by genome conformation assays such as Hi-C or super-resolution microscopy, or by CRISPR-based perturbation experiments. Alternatively, databases of expression quantitative trait loci may be used.
Full size image
TF abundance and post-translational modification
The number of transcripts encoding a given TF is a limited proxy of its protein abundance, let alone its activity102. To this end, proteomics technologies can be used to measure the abundance of TFs. Targeted proteomics at single-cell resolution is still challenging but some technologies such as mass spectrometry-based approaches or assays that use antibody–oligonucleotide conjugates are already available103 (reviewed elsewhere104). Alternatively, databases such as The Human Protein Atlas105,106 can be queried to confirm whether a candidate TF has been previously reported to be present at the protein level in a given tissue or cell type. In addition, post-translational modifications such as phosphorylation, ubiquitylation and methylation can affect TF localization, stability, activity and interaction with other proteins107. The most highly studied post-translational modification of TFs is phosphorylation, which can be informative as to whether a TF is in an inactive or active form108.
TF binding and cooperativity
GRN inference methods rely on TF binding predictions based on binding motif analysis to assign TFs to open chromatin regions in the genome. It is known that this type of prediction produces many false positives as a large number of TF binding motifs have low specificity109. To this end, ChIP-seq36, which as mentioned above measures the binding of TFs to DNA, can be used to test how many TF binding events were correctly predicted by the GRN inference method76. Databases such as ChIP-Atlas110, EpiMap111 and UniBind112 compile large collections of ChIP-seq experimental data and organize them by organism, tissue and cell type, making them valuable resources for analysing GRN predictions. Because not all ChIP-seq peaks represent direct binding events of a TF, EpiMap111 and UniBind112 implement different strategies to curate the data, thus providing more reliable information regarding TF binding sites. Another alternative is single-molecule footprinting, a technique that jointly measures TF binding and nucleosome occupancy at single DNA molecule resolution113,114. It allows for checking the state frequency of each genomic region: bound by a TF, unbound but with open chromatin, or unbound and occupied by nucleosomes. The advantage of single-molecule footprinting over ChIP-seq is that it provides a dynamic and quantifiable state of TF binding instead of a binary description. GRN inference methods predict that several TFs bind to the same open genomic region, which is in keeping with the knowledge that TFs bind cooperatively to DNA to induce transcription1,115,116. Another approach to assess the obtained GRN is to check whether the network has recovered the cooperative binding of TFs. Technologies such as CAP-SELEX117 enable cooperative interactions between selected TF pairs to be jointly profiled in the presence of DNA. Single-molecule footprinting can also be used for this purpose by checking the overlap of footprints. Other approaches include using protein–protein interaction assays118 or checking databases of previously annotated interactions119.
Regulatory activity of CREs
CREs can be in three different chromatin states: transcriptionally active, poised or repressive. Many of the reported open chromatin regions might not have a role in gene regulation, thereby increasing the number of false positives in GRN predictions. Therefore, experiments must assess whether candidate enhancers affect gene expression. The massively parallel reporter assay120 is a technique that allows to test whether candidate genomic regions can induce gene expression in episomal vectors. Another strategy is to carry out pooled CRISPR-based perturbations of candidate CREs followed by RNA sequencing to identify which regions of the genome affect gene expression69,121. In addition, the ENCODE Consortium has catalogued, using various biochemical assays, more than one million candidate CREs with enhancer-like signatures that span ~16% of the human genome36,122,123. As functional enhancers are evolutionarily conserved124,125, another approach is to check for genomic sequence similarity across different species. When studying diseases, CREs in open chromatin regions can be scanned for single-nucleotide polymorphisms (SNPs) that have been previously linked to diseases in genome-wide association studies. If candidate CREs are enriched for disease-associated SNPs, this suggests that those CREs are likely to be functional90,126.
Linkage to target genes
Even if an open chromatin region is validated to have regulatory properties, it is necessary to test which specific genes it affects. Chromosome conformation capture techniques such as Hi-C127,128,129 allow to measure the probability of contact between genomic regions and to identify topologically associating domains. Because gene regulation is based on sustained genomic interactions130,131, if a genomic region is consistently in close contact with the promoter region of a gene, it may regulate the gene. To this end, super-resolution microscopy has also been used to validate candidate CRE–gene interactions132, although with less throughput than Hi-C. Perturbation assays such as CRISPR-based screens coupled with whole-transcriptome analysis allow for deleting or activating specific CREs and observing how this changes gene expression69,133. In addition, databases of expression quantitative trait loci in human populations can be used to validate distal candidate CREs134,135,136.
TF perturbation
A more direct approach to test whether a TF regulates a particular gene is to perturb TF expression and see how this affects gene expression. Technologies for pooled CRISPR (in)activation screens coupled with whole-transcriptome read out are already available137,138,139,140,141. The changes in gene expression upon TF perturbation can be used as the ground truth to check how many of the affected genes are identified as target genes in the GRN35,95,142. Also, one can see whether the estimated TF activities (see previous section on ‘Inference of TF activities’) correspond to the perturbation that has been carried out (low or high TF activity for knockout or overexpression of the TF, respectively).
Challenges and future directions
The accumulation of omics data sets, particularly single-cell multi-omics data, in recent years has enabled a new wave of improved GRN inference strategies. An improved understanding of GRNs should pave the way to use these models not only as means to understand the principles of gene regulation but also as tools to drive cell fate decisions for cellular engineering, enabling the generation of new cell types with new functions and the reprogramming of diseased cells to a healthy phenotype. The prospects are hugely promising, but many challenges remain regarding the modelling of GRNs and their use as predictive tools.
Integrating transcription and accessibility
The use of multi-omics, in principle, allows for a better representation of gene regulation but also comes with its own challenges. As highly interrelated processes, chromatin accessibility and transcription are temporally coordinated. Yet they have profoundly different kinetics and may be temporally shifted. These relationships are often not fully understood and it is typically assumed that paired chromatin accessibility and transcriptomics data in the same cell at a single time point are representative of the interplay between both processes143,144. This limitation is compounded in the case of unpaired data if inadequate integration results in mismatched scATAC-seq and scRNA-seq data that will mislead the downstream modelling of GRNs145. Novel integration strategies, such as that introduced by FigR63, hold the promise to obtain better matching between cells. Among other factors, the temporal shift between chromatin accessibility and gene expression, as well as cooperative effects, gives rise to non-linear relationships. Some of the GRN inference methods that we have discussed use non-linear formulations to account for this, but they lose interpretability compared with linear models, and they often do not explicitly capture the sign of the interaction. For this reason, and for computational scalability, many methods still prefer to model gene regulation linearly. To improve the interpretability, SCENIC+67 and IReNA80 first infer regulatory interactions non-linearly using random forests, and then determine the sign of the interaction based on correlation analysis between TF and gene transcripts.
Scale and sparsity of single-cell data
GRN inference methods require a large number of observations that capture the variability of the biological process being studied. These observations can be individual cells, samples or conditions. Single-cell technologies generate thousands of profiles for a given sample, making it easier to infer GRNs in a larger variety of biological contexts than for bulk profiling technologies. Nonetheless, cells from the same sample are not necessarily independent and cannot be considered true biological replicates146. For this reason, the inclusion of different samples might be needed to obtain meaningful GRNs. In addition, current single-cell GRN inference methods build an aggregate network across a population of cells and do not take into account that cells may come from different samples. A candidate approach to address this issue is LIONESS147, which models the contribution of each sample when inferring GRNs and can generate sample-specific regulatory interactions. In addition, single-cell data are by nature sparse and noisy, particularly for data obtained by scATAC-seq, and proper filters need to be used to ensure a minimum quality148,149. For paired multi-omics technologies, a systematic benchmark comparing their varying coverage and sensitivity to their single-omic counterparts is missing150. Although sparsity is a known property of single-cell technologies151,152, none of the GRN inference methods discussed here explicitly accounts for sparsity in its modelling. Some methods apply data transformations to counteract this limitation. Imputation methods can be used to reduce the number of ‘dropouts’ (caused by under-sampling of mRNAs or accessible DNA reads)153,154,155, although it has been shown that they might have detrimental effects on GRN reconstruction156. Strategies that aggregate similar cells into pseudo-bulk profiles or metacells146,157,158 have been reported to be beneficial87. Owing to their sparsity, most computational pipelines treat scATAC-seq data as binary data, assigning regions of the genome that are either accessible or closed for each cell. However, the true state of DNA accessibility is known to be more refined and can involve regions of intermediate accessibility that fluctuate in a dynamic manner159. Thus, treating chromatin accessibility data as binary might be detrimental for downstream analyses160,161, and methods that handle accessibility in a quantitative manner might improve GRN reconstruction154,155,162,163.
The regulatory role of 3D genome structure
Current methods of GRN inference use arbitrary cutoffs based on genomic distance to assign CREs to genes. The aim of this filtering is to reduce the search space for each gene, requiring less computational resources, and to reduce the number of false positive interactions based on the fact that most genomic interactions are proximal69. However, there are some examples of interactions between CREs and genes separated by large distances, such as enhancers of the MYC gene located almost 2 Mb downstream of it164. Depending on the distance cutoff that is used, GRN inference methods might miss crucial CRE–gene interactions. In addition, some interactions occur across chromosomes, as reported during olfactory receptor selection165, which current GRN methods are not able to consider. One solution to this problem is to use technologies based on 3D proximity, such as Hi-C127,129, to assess whether a CRE might be regulating a gene. This strategy has been successfully applied by DC3 (ref. 88) and MAGICAL166. Despite some high-throughput alternatives167,168, chromosome conformation capture techniques pose new challenges owing to their sparse nature169 and the facts that they still require integration with other modalities and their protocol can be hard to reproduce170,171. Until they become more widely available, computational approaches have been used to predict the 3D structure of the genome based on accessibility data such as scATAC-seq data172,173. Their use in GRN modelling has the potential to overcome the limitations of using distance-based cutoffs.
Refinement of TF binding predictions
The current strategy used by GRN inference methods of assigning TFs to CREs relies on TF binding motif databases (Box 1). Each database has a different coverage of motif collections, which might bias the resulting predictions. Motif databases are based on data from previous binding experiments such as ChIP-seq. However, it is estimated that there are no available binding data for 10% of the approximately 1,600 sequence-specific TFs encoded in the human genome31,109. TFs without known binding motifs are excluded from GRN modelling, a factor that is exacerbated for non-model organisms as they tend to have fewer known TF binding motifs than other more well-studied organisms. One possible solution to incorporate missing TFs might be to leverage known protein–protein interactions during GRN inference. Moreover, current TF binding motifs are based on data from multiple tissues and cell types. It is known that TF binding is a highly context-specific process1, and although the available motifs are still relevant for many tissues, cell type-specific motif models might help to increase the accuracy of TF binding predictions. Recent computational strategies based on deep learning allow for cell type-specific TF binding predictions174,175. These models are trained to predict cell type-specific DNA accessibility solely based on DNA sequence. Once trained, they identify which nucleotides are predicted to affect accessibility the most through in silico mutagenesis or by using strategies of interpretable machine learning such as SHAP176. To derive cell type-specific TF binding predictions, these methods combine the predicted nucleotide quantifications with binding motifs. Although these strategies have the potential to better contextualize GRN inference, they require pretrained models using large amounts of data and are still limited to known TF binding motifs. With the accumulation of high-quality cell atlases from consortium initiatives49,177,178, we envision that these strategies could eventually replace classic TF binding motif predictions. Furthermore, current TF binding predictions are binary but a quantitative definition could be more informative. BANC-seq179, a technology that measures quantitative TF binding affinities, has the potential to generate more accurate GRNs.
Emerging multi-omics for GRN inference
The paired profiling of transcriptomics and chromatin accessibility data has enabled the potentially more accurate inference of GRNs but is still a costly assay, limiting its widespread use. Newer alternatives such as ISSAAC-seq180 enable multi-omics profiling at a much lower cost than the commercial 10× Multiome kit. Despite this, it might be the case that joint scRNA-seq and scATAC-seq data alone do not provide enough information to characterize gene regulation fully. In that case, advances in single-cell multi-omics profiling technologies that include more data modalities will be crucial181. Among such promising technologies is NEAT-seq182, which simultaneously profiles intra-nuclear proteins, chromatin accessibility and gene expression, allowing to discard possible false positives in GRN modelling by including TF protein abundance. Another example is scChaRM-seq183, which simultaneously profiles DNA methylation, chromatin accessibility and gene expression. Their joint profiling allows for TF assignment to CREs to be fine-tuned according to their methylation status. Moreover, ATAC-STARR-seq184 can carry out massively parallel reporter assay and chromatin accessibility profiling simultaneously to test the transcribing capacity of open CREs. Advances in untargeted single-cell proteomics and phosphoproteomics may enable the profiling of functionally active TFs185. One example is Phospho-seq186, a novel technology that profiles chromatin accessibility and phosphorylated proteins at the single-cell level. Genetic information is known to be heterogeneous among populations of individuals but most methods assume that they share the same genome187. scGET-seq188, a technology that jointly profiles the genome and chromatin accessibility, has the potential to aid the inference of causal GRNs by testing how SNPs may affect chromatin accessibility owing to changes in TF binding affinities.
Benchmarking of GRNs
The benchmarking of GRNs is crucial to understand the accuracy of novel GRN inference methods, in particular those that leverage multi-omics data, which have not yet been evaluated systematically. Unfortunately, the validation of predicted GRNs is a complicated task as there is no clear ‘ground truth’ for gene regulation. One approach to benchmarking is to build in silico GRNs that allow us to assess GRN reconstruction against a known ground truth34, yet one that might not well reflect true biological GRNs. As mentioned in the previous section, there are different methodologies that can be used to assess indirectly the quality of the predicted gene regulation events but these have certain limitations. Even if TF binding to a gene is observed, it does not necessarily mean that the TF regulates that gene as TFs bind stochastically into open regions of DNA and require cooperation with other molecules for effective regulation of transcription159. Chromosome conformation capture technologies provide contact information and define topologically associating domains. However, their resolution might not be sufficient to detect certain genomic interactions189. High-resolution Hi-C maps exist, such as Micro-C190, but their cost becomes prohibitive when comparing many experimental conditions. To address this, machine learning approaches are being used to impute higher-coverage Hi-C maps from lower-coverage data to increase their resolution191. Another possibility is to use super-resolution microscopy-based alternatives, but their throughput is rather limited189. TFs cooperatively drive gene expression but they do so mainly as a result of DNA-mediated interactions rather than protein–protein contacts117. Therefore, the evaluation of TF–TF interactions might be limited to particular cases only. The evaluation of GRNs through the use of perturbation experiments is a more promising approach owing to its inherent causality. However, perturbation screens are costly, sometimes do not work as expected and may be hindered by compensatory mechanisms and unaccounted for downstream effects. In addition to all of these limitations, as gene regulation is a time-dependent process, it might be the case that experiments contradict themselves because they captured a different time frame or because of experimental noise. Because the generation of a true ‘gold standard’ of gene regulation seems out of reach for the moment, we are more inclined to use these different assessment strategies as a collection of ‘silver standards’. We envision that a computational tool that collects and distributes such information will be useful for the community to carry out quality control on the inferred GRNs and to benchmark novel GRN inference methods. Platforms such as the Open Problems for Single-Cell Analysis project192 offer a suitable infrastructure to run and evaluate the large variety of GRN inference methods. These would also enable the evaluation of GRN inference methods in an unbiased manner through open competition, as was illustrated for GRN inference from bulk transcriptomics data by the DREAM challenges33.
GRNs in the bigger picture
It is important to keep in mind that GRNs are not isolated. The classic example of the lac operon, whereby a metabolite (lactose) triggers gene regulation, highlights that GRNs are part of an entangled cellular machinery, including signalling and metabolic processes. The addition of single-cell phosphoproteomics and metabolomics193 opens the possibility of linking gene regulation to cell signalling processes using context-specific network models194.
Furthermore, cells rarely work as autonomous systems, and gene regulation is highly coordinated within tissues. Thus, another promising direction will be the integration of multimodal data with spatial information. In particular, we envision the integration of GRNs with intracellular and intercellular communication processes195,196,197 into spatially aware models198,199. These strategies can help in understanding multicellular regulatory processes in time and space200.
Conclusions
Advances in high-throughput, single-cell multimodal technologies together with computational methods are paving the way to increasingly accurate GRN inference models. The large scale of the data sets makes it increasingly possible to train deep learning methods to predict gene expression from sequencing data175,201,202. GRNs complement these approaches by giving a more interpretable model. Together, these different approaches might help us to better understand differences in gene regulation across cell types, organs, populations and species, and serve as tools to control cell fate decisions. In the biomedical field, such knowledge could enable the identification of novel drug targets that control pathophysiological processes in different diseases.
References
Kim, S. & Wysocka, J. Deciphering the multi-scale, quantitative cis-regulatory code. Mol. Cell 83, 373–392 (2023). This extensive review covers the molecular basis of the cis-regulatory code.
Article
 CAS PubMed Google Scholar 
238
1
201
0
Zaret, K. S. & Carroll, J. S. Pioneer transcription factors: establishing competence for gene expression. Genes Dev. 25, 2227–2241 (2011).
Article
 CAS PubMed PubMed Central Google Scholar 
1,541
59
1,370
2
Lai, X., Wolkenhauer, O. & Vera, J. Understanding microRNA-mediated gene regulatory networks through mathematical modelling. Nucleic Acids Res. 44, 6019–6035 (2016).
Article
 CAS PubMed PubMed Central Google Scholar 
183
4
145
0
Du, J.-X. et al. Splicing factors: insights into their regulatory network in alternative splicing in cancer. Cancer Lett. 501, 83–104 (2021).
Article
 CAS PubMed Google Scholar 
45
1
28
0
Statello, L., Guo, C.-J., Chen, L.-L. & Huarte, M. Gene regulation by long non-coding RNAs and its biological functions. Nat. Rev. Mol. Cell Biol. 22, 96–118 (2021).
Article
 CAS PubMed Google Scholar 
4,102
30
3,347
1
2
Carthew, R. W. Gene regulation and cellular metabolism: an essential partnership. Trends Genet. 37, 389–400 (2021).
Article
 CAS PubMed Google Scholar 
96
0
55
0
Davidson, E. H. & Erwin, D. H. Gene regulatory networks and the evolution of animal body plans. Science 311, 796–800 (2006).
Article
 CAS PubMed Google Scholar 
1,159
33
951
2
Su, E. Y., Spangler, A., Bian, Q., Kasamoto, J. Y. & Cahan, P. Reconstruction of dynamic regulatory networks reveals signaling-induced topology changes associated with germ layer specification. Stem Cell Rep. 17, 427–442 (2022).
Article
 CAS Google Scholar 
18
0
24
0
Claringbould, A. & Zaugg, J. B. Enhancers in disease: molecular basis and emerging treatment strategies. Trends Mol. Med. 27, 1060–1073 (2021).
Article
 CAS PubMed Google Scholar 
169
2
147
0
Jacob, F. & Monod, J. Genetic regulatory mechanisms in the synthesis of proteins. J. Mol. Biol. 3, 318–356 (1961). This seminal study delineates a gene regulatory system.
Article
 CAS PubMed Google Scholar 
6,191
17
1,459
2
Ideker, T., Galitski, T. & Hood, L. A new approach to decoding life: systems biology. Annu. Rev. Genomics Hum. Genet. 2, 343–372 (2001).
Article
 CAS PubMed Google Scholar 
1,568
2
945
0
Davidson, E. H. et al. A genomic regulatory network for development. Science 295, 1669–1678 (2002).
Article
 CAS PubMed Google Scholar 
1,502
8
999
1
Snyder, M. & Gallagher, J. E. G. Systems biology from a yeast omics perspective. FEBS Lett. 583, 3895–3899 (2009).
Article
 CAS PubMed PubMed Central Google Scholar 
51
0
32
0
Han, H. et al. TRRUST v2: an expanded reference database of human and mouse transcriptional regulatory interactions. Nucleic Acids Res. 46, D380–D386 (2018).
Article
 CAS PubMed Google Scholar 
1,831
16
1,577
0
Garcia-Alonso, L., Holland, C. H., Ibrahim, M. M., Turei, D. & Saez-Rodriguez, J. Benchmark and integration of resources for the estimation of human transcription factor activities. Genome Res. 29, 1363–1375 (2019).
Article
 CAS PubMed PubMed Central Google Scholar 
920
20
931
0
1
Liu, Z.-P., Wu, C., Miao, H. & Wu, H. RegNetwork: an integrated database of transcriptional and post-transcriptional regulatory networks in human and mouse. Database 2015, bav095 (2015).
Article
 PubMed PubMed Central Google Scholar 
515
1
402
0
Keenan, A. B. et al. ChEA3: transcription factor enrichment analysis by orthogonal omics integration. Nucleic Acids Res. 47, W212–W224 (2019).
Article
 CAS PubMed PubMed Central Google Scholar 
932
13
886
0
Margolin, A. A. et al. ARACNE: an algorithm for the reconstruction of gene regulatory networks in a mammalian cellular context. BMC Bioinforma. 7, S7 (2006).
Article
 Google Scholar 
Langfelder, P. & Horvath, S. WGCNA: an R package for weighted correlation network analysis. BMC Bioinforma. 9, 559 (2008).
Article
 Google Scholar 
Huynh-Thu, V. A., Irrthum, A., Wehenkel, L. & Geurts, P. Inferring regulatory networks from expression data using tree-based methods. PLoS ONE 5, e12776 (2010).
Article
 PubMed PubMed Central Google Scholar 
1,998
7
1,994
0
Buenrostro, J. D., Giresi, P. G., Zaba, L. C., Chang, H. Y. & Greenleaf, W. J. Transposition of native chromatin for fast and sensitive epigenomic profiling of open chromatin, DNA-binding proteins and nucleosome position. Nat. Methods 10, 1213–1218 (2013).
Article
 CAS PubMed PubMed Central Google Scholar 
6,378
104
6,728
1
Fiers, M. W. E. J. et al. Mapping gene regulatory networks from single-cell omics data. Brief. Funct. Genomics 17, 246–254 (2018).
Article
 CAS PubMed PubMed Central Google Scholar 
229
0
190
0
Cha, J. & Lee, I. Single-cell network biology for resolving cellular heterogeneity in human diseases. Exp. Mol. Med. 52, 1798–1808 (2020).
Article
 CAS PubMed PubMed Central Google Scholar 
126
0
100
0
Klein, A. M. et al. Droplet barcoding for single-cell transcriptomics applied to embryonic stem cells. Cell 161, 1187–1201 (2015).
Article
 CAS PubMed PubMed Central Google Scholar 
3,389
44
3,191
1
Macosko, E. Z. et al. Highly parallel genome-wide expression profiling of individual cells using nanoliter droplets. Cell 161, 1202–1214 (2015).
Article
 CAS PubMed PubMed Central Google Scholar 
7,120
131
7,576
5
Chen, S., Lake, B. B. & Zhang, K. High-throughput sequencing of the transcriptome and chromatin accessibility in the same cell. Nat. Biotechnol. 37, 1452–1457 (2019).
Article
 CAS PubMed PubMed Central Google Scholar 
763
11
745
0
Liu, L. et al. Deconvolution of single-cell multi-omics layers reveals regulatory heterogeneity. Nat. Commun. 10, 470 (2019).
Article
 CAS PubMed PubMed Central Google Scholar 
235
2
169
0
Ma, S. et al. Chromatin potential identified by shared single-cell profiling of RNA and chromatin. Cell 183, 1103–1116.e20 (2020).
Article
 CAS PubMed PubMed Central Google Scholar 
992
51
933
0
Mercatelli, D., Scalambra, L., Triboli, L., Ray, F. & Giorgi, F. M. Gene regulatory network inference resources: a practical overview. Biochim. Biophys. Acta Gene Regul. Mech. 1863, 194430 (2020).
Article
 CAS PubMed Google Scholar 
160
1
124
0
Moerman, T. et al. GRNBoost2 and Arboreto: efficient and scalable inference of gene regulatory networks. Bioinformatics 35, 2159–2161 (2019).
Article
 CAS PubMed Google Scholar 
522
0
501
0
Lambert, S. A. et al. The human transcription factors. Cell 175, 598–599 (2018).
Article
 CAS PubMed Google Scholar 
700
9
601
1
Holland, C. H. et al. Robustness and applicability of transcription factor and pathway analysis tools on single-cell RNA-seq data. Genome Biol. 21, 36 (2020).
Article
 CAS PubMed PubMed Central Google Scholar 
Marbach, D. et al. Wisdom of crowds for robust gene network inference. Nat. Methods 9, 796–804 (2012). This work is a crowdsourced benchmark for GRN inference from bulk transcriptomics data.
Article
 CAS PubMed PubMed Central Google Scholar 
1,682
56
2,169
4
Pratapa, A., Jalihal, A. P., Law, J. N., Bharadwaj, A. & Murali, T. M. Benchmarking algorithms for gene regulatory network inference from single-cell transcriptomic data. Nat. Methods 17, 147–154 (2020).
Article
 CAS PubMed PubMed Central Google Scholar 
669
12
950
0
McCalla, S. G. et al. Identifying strengths and weaknesses of methods for computational network inference from single-cell RNA-seq data. G3 3, jkad004 (2023).
Article
 Google Scholar 
44
1
86
1
Johnson, D. S., Mortazavi, A., Myers, R. M. & Wold, B. Genome-wide mapping of in vivo protein–DNA interactions. Science 316, 1497–1502 (2007).
Article
 CAS PubMed Google Scholar 
2,766
42
2,192
3
Kaya-Okur, H. S. et al. CUT&Tag for efficient epigenomic profiling of small samples and single cells. Nat. Commun. 10, 1930 (2019).
Article
 PubMed PubMed Central Google Scholar 
1,869
20
1,610
1
Lee, T. I. et al. Transcriptional regulatory networks in Saccharomyces cerevisiae. Science 298, 799–804 (2002).
Article
 CAS PubMed Google Scholar 
2,809
82
2,742
5
Grosselin, K. et al. High-throughput single-cell ChIP-seq identifies heterogeneity of chromatin states in breast cancer. Nat. Genet. 51, 1060–1066 (2019).
Article
 CAS PubMed Google Scholar 
444
7
349
1
Bartosovic, M., Kabbe, M. & Castelo-Branco, G. Single-cell CUT&Tag profiles histone modifications and transcription factors in complex tissues. Nat. Biotechnol. 39, 825–835 (2021).
Article
 CAS PubMed PubMed Central Google Scholar 
398
4
313
2
Bartosovic, M. & Castelo-Branco, G. Multimodal chromatin profiling using nanobody-based single-cell CUT&Tag. Nat. Biotechnol. https://doi.org/10.1038/s41587-022-01535-4
(2022).
Article PubMed PubMed Central Google Scholar 
105
2
105
0
Qin, J., Hu, Y., Xu, F., Yalamanchili, H. K. & Wang, J. Inferring gene regulatory networks by integrating ChIP-seq/chip and transcriptome data via LASSO-type regularization methods. Methods 67, 294–303 (2014).
Article
 CAS PubMed Google Scholar 
58
0
59
0
Boyle, A. P. et al. High-resolution mapping and characterization of open chromatin across the genome. Cell 132, 311–322 (2008).
Article
 CAS PubMed PubMed Central Google Scholar 
1,397
61
1,192
2
Kelly, T. K. et al. Genome-wide mapping of nucleosome positioning and DNA methylation within individual DNA molecules. Genome Res. 22, 2497–2506 (2012).
Article
 CAS PubMed PubMed Central Google Scholar 
445
41
434
1
Minnoye, L. et al. Chromatin accessibility profiling methods. Nat. Rev. Methods Prim. 1, 1–24 (2021).
Google Scholar 
Pranzatelli, T. J. F., Michael, D. G. & Chiorini, J. A. ATAC2GRN: optimized ATAC-seq and DNase1-seq pipelines for rapid and accurate genome regulatory network inference. BMC Genom. 19, 563 (2018).
Article
 Google Scholar 
Qin, Q. et al. Lisa: inferring transcriptional regulators through integrative modeling of public chromatin accessibility and ChIP-seq data. Genome Biol. 21, 32 (2020).
Article
 PubMed PubMed Central Google Scholar 
Sonawane, A. R., DeMeo, D. L., Quackenbush, J. & Glass, K. Constructing gene regulatory networks using epigenetic data. NPJ Syst. Biol. Appl. 7, 45 (2021).
Article
 CAS PubMed PubMed Central Google Scholar 
34
2
28
0
Tabula Sapiens Consortium et al. The Tabula Sapiens: a multiple-organ, single-cell transcriptomic atlas of humans. Science 376, eabl4896 (2022).
Article
 Google Scholar 
837
6
281
1
Aibar, S. et al. SCENIC: single-cell regulatory network inference and clustering. Nat. Methods 14, 1083–1086 (2017). This work presents the first bespoke method to infer GRNs at the single-cell level, introducing the use of TF binding motif information for the estimation of GRNs.
Article
 CAS PubMed PubMed Central Google Scholar 
5,210
36
4,314
1
Herring, C. A., Chen, B., McKinley, E. T. & Lau, K. S. Single-cell computational strategies for lineage reconstruction in tissue systems. Cell Mol. Gastroenterol. Hepatol. 5, 539–548 (2018).
Article
 PubMed PubMed Central Google Scholar 
38
0
44
0
Wagner, A., Regev, A. & Yosef, N. Revealing the vectors of cellular identity with single-cell genomics. Nat. Biotechnol. 34, 1145–1160 (2016).
Article
 CAS PubMed PubMed Central Google Scholar 
653
3
537
0
Specht, A. T. & Li, J. LEAP: constructing gene co-expression networks for single-cell RNA-sequencing data using pseudotime ordering. Bioinformatics 33, 764–766 (2017).
Article
 CAS PubMed Google Scholar 
188
0
157
0
Papili Gao, N., Ud-Dean, S. M. M., Gandrillon, O. & Gunawan, R. SINCERITIES: inferring gene regulatory networks from time-stamped single cell transcriptional expression profiles. Bioinformatics 34, 258–266 (2018).
Article
 PubMed Google Scholar 
232
3
191
1
Love, M. I., Huber, W. & Anders, S. Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2. Genome Biol. 15, 550 (2014).
Article
 PubMed PubMed Central Google Scholar 
Ritchie, M. E. et al. limma powers differential expression analyses for RNA-sequencing and microarray studies. Nucleic Acids Res. 43, e47 (2015).
Article
 PubMed PubMed Central Google Scholar 
35,601
34
29,513
1
Buenrostro, J. D. et al. Single-cell chromatin accessibility reveals principles of regulatory variation. Nature 523, 486–490 (2015). This paper introduces single-cell assay for transpose-accessible chromatin (scATAC) technology.
Article
 CAS PubMed PubMed Central Google Scholar 
2,245
26
1,940
0
Ramirez, R. N. et al. Dynamic gene regulatory networks of human myeloid differentiation. Cell Syst. 4, 416–429.e3 (2017).
Article
 CAS PubMed PubMed Central Google Scholar 
114
6
112
0
Starks, R. R., Biswas, A., Jain, A. & Tuteja, G. Combined analysis of dissimilar promoter accessibility and gene expression profiles identifies tissue-specific genes and actively repressed networks. Epigenetics Chromatin 12, 16 (2019).
Article
 PubMed PubMed Central Google Scholar 
Johnson, J. S. et al. A comprehensive map of the monocyte-derived dendritic cell transcriptional network engaged upon innate sensing of HIV. Cell Rep. 30, 914–931.e9 (2020).
Article
 CAS PubMed PubMed Central Google Scholar 
28
5
25
0
Argelaguet, R., Cuomo, A. S. E., Stegle, O. & Marioni, J. C. Computational principles and challenges in single-cell data integration. Nat. Biotechnol. 39, 1202–1215 (2021).
Article
 CAS PubMed Google Scholar 
409
0
414
0
Ma, A. et al. Single-cell biological network inference using a heterogeneous graph transformer. Nat. Commun. 14, 964 (2023).
Article
 CAS PubMed PubMed Central Google Scholar 
142
0
89
0
Kartha, V. K. et al. Functional inference of gene regulation using single-cell multi-omics. Cell Genom. 2, 100166 (2022). This paper introduces FigR, which has a novel integration strategy for scRNA-seq and scATAC-seq data that can enhance GRN inference.
Article
 CAS PubMed PubMed Central Google Scholar 
192
7
210
0
Cao, Z.-J. & Gao, G. Multi-omics single-cell data integration and regulatory inference with graph-linked embedding. Nat. Biotechnol. 40, 1458–1466 (2022).
Article
 CAS PubMed PubMed Central Google Scholar 
429
4
505
0
Jin, S., Zhang, L. & Nie, Q. scAI: an unsupervised approach for the integrative analysis of parallel single-cell transcriptomic and epigenomic profiles. Genome Biol. 21, 25 (2020).
Article
 PubMed PubMed Central Google Scholar 
Jansen, C. et al. Building gene regulatory networks from scATAC-seq and scRNA-seq using linked self organizing maps. PLoS Comput. Biol. 15, e1006555 (2019).
Article
 PubMed PubMed Central Google Scholar 
80
0
76
0
González-Blas, C. B. et al. SCENIC+: single-cell multiomic inference of enhancers and gene regulatory networks. Preprint at bioRxiv https://doi.org/10.1101/2022.08.19.504505 (2022). This study presents a large, curated collection of TF binding motifs and introduces a novel GRN inference method.
167
2
321
0
Heinz, S. et al. Simple combinations of lineage-determining transcription factors prime cis-regulatory elements required for macrophage and B cell identities. Mol. Cell 38, 576–589 (2010).
Article
 CAS PubMed PubMed Central Google Scholar 
13,022
179
12,919
4
Gasperini, M. et al. A genome-wide framework for mapping gene regulation via cellular genetic screens. Cell 176, 1516 (2019).
Article
 CAS PubMed Google Scholar 
189
18
246
1
Zuin, J. et al. Nonlinear control of transcription through enhancer–promoter interactions. Nature 604, 571–577 (2022).
Article
 CAS PubMed PubMed Central Google Scholar 
384
49
318
2
Kamal, A. et al. GRaNIE and GRaNPA: inference and evaluation of enhancer-mediated gene regulatory networks. Mol. Syst. Biol. https://doi.org/10.15252/msb.202311627
(2023).
Article PubMed PubMed Central Google Scholar 
53
0
59
0
Zhang, L., Zhang, J. & Nie, Q. DIRECT-NET: an efficient method to discover cis-regulatory elements and construct regulatory networks from single-cell multiomics data. Sci. Adv. 8, eabl7393 (2022).
Article
 CAS PubMed PubMed Central Google Scholar 
64
0
53
0
Duren, Z., Chen, X., Jiang, R., Wang, Y. & Wong, W. H. Modeling gene regulation from paired expression and chromatin accessibility data. Proc. Natl Acad. Sci. USA 114, E4914–E4923 (2017).
Article
 CAS PubMed PubMed Central Google Scholar 
210
4
233
0
Burdziak, C., Azizi, E., Prabhakaran, S. & Pe’er, D. A nonparametric multi-view model for estimating cell type-specific gene regulatory networks. Preprint at arXiv https://doi.org/10.48550/arXiv.1902.08138 (2019).
7
0
4
0
Bachireddy, P. et al. Mapping the evolution of T cell states during response and resistance to adoptive cellular therapy. Cell Rep. 37, 109992 (2021).
Article
 CAS PubMed PubMed Central Google Scholar 
55
3
51
1
1
Kamimoto, K. et al. Dissecting cell identity via network inference and in silico gene perturbation. Nature 614, 742–751 (2023). This work presents a novel GRN inference method from scRNA-seq and scATAC-seq data that also introduces an in silico TF perturbation strategy.
Article
 CAS PubMed PubMed Central Google Scholar 
474
12
570
0
Skok Gibbs, C. et al. High-performance single-cell gene regulatory network inference at scale: the Inferelator 3.0. Bioinformatics 38, 2519–2528 (2022).
Article
 PubMed PubMed Central Google Scholar 
65
1
86
0
Fleck, J. S. et al. Inferring and perturbing cell fate regulomes in human brain organoids. Nature https://doi.org/10.1038/s41586-022-05279-8
(2022).
Article PubMed PubMed Central Google Scholar 
266
10
291
0
Li, Z., Nagai, J. S., Kuppe, C., Kramann, R. & Costa, I. G. scMEGA: single-cell multi-omic enhancer-based gene regulatory network inference. Bioinform. Adv. 3, vbad003 (2023).
Article
 PubMed PubMed Central Google Scholar 
26
0
34
0
Jiang, J. et al. IReNA: integrated regulatory network analysis of single-cell transcriptomes and chromatin accessibility profiles. iScience 25, 105359 (2022).
Article
 CAS PubMed PubMed Central Google Scholar 
31
0
33
0
Wang, L. et al. Dictys: dynamic gene regulatory network dissects developmental continuum with single-cell multi-omics. Preprint at bioRxiv https://doi.org/10.1101/2022.09.14.508036 (2022).
36
1
65
0
Zhang, S. et al. Inference of cell type-specific gene regulatory networks on cell lineages from single cell omic datasets. Nat. Commun. 14, 3064 (2023).
Article
 CAS PubMed PubMed Central Google Scholar 
93
0
84
0
Duren, Z., Chen, X., Xin, J., Wang, Y. & Wong, W. H. Time course regulatory analysis based on paired expression and chromatin accessibility data. Genome Res. 30, 622–634 (2020).
Article
 CAS PubMed PubMed Central Google Scholar 
51
0
65
0
Xu, Q. et al. ANANSE: an enhancer network-based computational approach for predicting key transcription factors in cell fate determination. Nucleic Acids Res. 49, 7966–7985 (2021).
Article
 CAS PubMed PubMed Central Google Scholar 
71
4
105
0
Duren, Z. et al. sc-compReg enables the comparison of gene regulatory networks between conditions using single-cell data. Nat. Commun. 12, 4763 (2021).
Article
 CAS PubMed PubMed Central Google Scholar 
32
0
27
0
Kuppe, C. et al. Spatial multi-omic map of human myocardial infarction. Nature 608, 766–777 (2022).
Article
 CAS PubMed PubMed Central Google Scholar 
501
17
559
0
Argelaguet, R. et al. Decoding gene regulation in the mouse embryo using single-cell multi-omics. Preprint at bioRxiv https://doi.org/10.1101/2022.06.15.496239 (2022).
62
4
94
0
Zeng, W. et al. DC3 is a method for deconvolution and coupled clustering from bulk and single-cell genomics data. Nat. Commun. 10, 4613 (2019).
Article
 PubMed PubMed Central Google Scholar 
71
0
51
0
Liberzon, A. et al. The molecular signatures database (MSigDB) hallmark gene set collection. Cell Syst. 1, 417–425 (2015).
Article
 CAS PubMed PubMed Central Google Scholar 
11,716
109
10,805
0
Anderson, A. G. et al. Single nucleus multiomics identifies ZEB1 and MAFB as candidate regulators of Alzheimer’s disease-specific cis-regulatory elements. Cell Genomics 3, 100263 (2023).
Article
 CAS PubMed PubMed Central Google Scholar 
73
5
107
0
Thompson, D., Regev, A. & Roy, S. Comparative analysis of gene regulatory networks: from network reconstruction to evolution. Annu. Rev. Cell Dev. Biol. 31, 399–428 (2015).
Article
 CAS PubMed Google Scholar 
185
1
145
0
Pritchard, J. K., Stephens, M. & Donnelly, P. Inference of population structure using multilocus genotype data. Genetics 155, 945–959 (2000).
Article
 CAS PubMed PubMed Central Google Scholar 
32,169
22
6,432
2
Lou, S. et al. TopicNet: a framework for measuring transcriptional regulatory network change. Bioinformatics 36, i474–i481 (2020).
Article
 CAS PubMed PubMed Central Google Scholar 
30
0
22
0
Alvarez, M. J. et al. Functional characterization of somatic mutations in cancer using network-based inference of protein activity. Nat. Genet. 48, 838–847 (2016).
Article
 CAS PubMed PubMed Central Google Scholar 
914
8
1,280
0
Badia-i-Mompel, P. et al. decoupleR: ensemble of computational methods to infer biological activities from omics data. Bioinforma. Adv. 2, vbac016 (2022).
Article
 Google Scholar 
656
4
733
0
Subramanian, A. et al. Gene set enrichment analysis: a knowledge-based approach for interpreting genome-wide expression profiles. Proc. Natl Acad. Sci. USA 102, 15545–15550 (2005).
Article
 CAS PubMed PubMed Central Google Scholar 
49,369
357
44,573
3
Garcia-Alonso, L. et al. Transcription factor activities enhance markers of drug sensitivity in cancer. Cancer Res. 78, 769–780 (2018).
Article
 CAS PubMed Google Scholar 
196
5
222
0
Walsh, L. A. et al. An integrated systems biology approach identifies TRIM25 as a key determinant of breast cancer metastasis. Cell Rep. 20, 1623–1640 (2017).
Article
 CAS PubMed PubMed Central Google Scholar 
107
8
108
0
Guan, X. et al. Androgen receptor activity in T cells limits checkpoint blockade efficacy. Nature 606, 791–796 (2022).
Article
 CAS PubMed PubMed Central Google Scholar 
301
10
223
0
Melms, J. C. et al. A molecular single-cell lung atlas of lethal COVID-19. Nature 595, 114–119 (2021).
Article
 CAS PubMed PubMed Central Google Scholar 
656
57
825
3
2
La Manno, G. et al. RNA velocity of single cells. Nature 560, 494–498 (2018).
Article
 PubMed PubMed Central Google Scholar 
3,869
73
4,108
1
de Sousa Abreu, R., Penalva, L. O., Marcotte, E. M. & Vogel, C. Global signatures of protein and mRNA expression levels. Mol. Biosyst. 5, 1512–1526 (2009).
PubMed Google Scholar 
Chung, H. et al. Joint single-cell measurements of nuclear proteins and RNA in vivo. Nat. Methods 18, 1204–1212 (2021).
Article
 CAS PubMed PubMed Central Google Scholar 
116
1
80
0
Bennett, H. M., Stephenson, W., Rose, C. M. & Darmanis, S. Single-cell proteomics enabled by next-generation sequencing or mass spectrometry. Nat. Methods 20, 363–374 (2023).
Article
 CAS PubMed Google Scholar 
260
0
142
0
Uhlén, M. et al. A human protein atlas for normal and cancer tissues based on antibody proteomics. Mol. Cell. Proteom. 4, 1920–1932 (2005).
Article
 Google Scholar 
1,407
55
1,109
2
Uhlén, M. et al. Proteomics. Tissue-based map of the human proteome. Science 347, 1260419 (2015).
Article
 PubMed Google Scholar 
14,080
501
12,351
10
Weidemüller, P., Kholmatov, M., Petsalaki, E. & Zaugg, J. B. Transcription factors: bridge between cell signaling and gene regulation. Proteomics 21, e2000034 (2021).
Article
 PubMed Google Scholar 
216
2
165
0
Sousa, A. et al. Pan-cancer landscape of protein activities identifies drivers of signalling dysregulation and patient survival. Mol. Syst. Biol. 19, e10631 (2023).
Article
 PubMed PubMed Central Google Scholar 
22
0
12
0
Inukai, S., Kock, K. H. & Bulyk, M. L. Transcription factor–DNA binding: beyond binding site motifs. Curr. Opin. Genet. Dev. 43, 110–119 (2017).
Article
 CAS PubMed PubMed Central Google Scholar 
356
4
259
0
Oki, S. et al. ChIP-Atlas: a data-mining suite powered by full integration of public ChIP-seq data. EMBO Rep. 19, e46255 (2018).
Article
 PubMed PubMed Central Google Scholar 
756
9
630
0
Boix, C. A., James, B. T., Park, Y. P., Meuleman, W. & Kellis, M. Regulatory genomic circuitry of human disease loci by integrative epigenomics. Nature 590, 300–307 (2021).
Article
 CAS PubMed PubMed Central Google Scholar 
397
11
509
1
1
Puig, R. R., Boddie, P., Khan, A., Castro-Mondragon, J. A. & Mathelier, A. UniBind: maps of high-confidence direct TF–DNA interactions across nine species. BMC Genom. 22, 482 (2021).
Article
 CAS Google Scholar 
Krebs, A. R. et al. Genome-wide single-molecule footprinting reveals high RNA polymerase II turnover at paused promoters. Mol. Cell 67, 411–422.e4 (2017).
Article
 CAS PubMed PubMed Central Google Scholar 
228
15
235
0
Sönmezer, C. et al. Molecular co-occupancy identifies transcription factor binding cooperativity in vivo. Mol. Cell 81, 255–267.e6 (2021).
Article
 PubMed Google Scholar 
153
7
183
1
Gasperini, M., Tome, J. M. & Shendure, J. Towards a comprehensive catalogue of validated and target-linked human enhancers. Nat. Rev. Genet. 21, 292–310 (2020).
Article
 CAS PubMed PubMed Central Google Scholar 
359
5
366
0
Ibarra, I. L. et al. Mechanistic insights into transcription factor cooperativity and its impact on protein–phenotype interactions. Nat. Commun. 11, 124 (2020).
Article
 CAS PubMed PubMed Central Google Scholar 
94
3
78
0
Jolma, A. et al. DNA-dependent formation of transcription factor pairs alters their binding specificity. Nature 527, 384–388 (2015).
Article
 CAS PubMed Google Scholar 
551
11
538
1
Lu, H. et al. Recent advances in the development of protein–protein interactions modulators: mechanisms and clinical trials. Signal. Transduct. Target. Ther. 5, 1–23 (2020).
Article
 Google Scholar 
763
3
697
0
Orchard, S. et al. The MIntAct project—IntAct as a common curation platform for 11 molecular interaction databases. Nucleic Acids Res. 42, D358–D363 (2014).
Article
 CAS PubMed Google Scholar 
1,856
12
1,594
0
Patwardhan, R. P. et al. High-resolution analysis of DNA regulatory elements by synthetic saturation mutagenesis. Nat. Biotechnol. 27, 1173–1175 (2009).
Article
 CAS PubMed PubMed Central Google Scholar 
377
7
352
1
Ren, X. et al. Parallel characterization of cis-regulatory elements for multiple genes using CRISPRpath. Sci. Adv. 7, eabi4360 (2021).
Article
 CAS PubMed PubMed Central Google Scholar 
26
3
16
0
ENCODE Project Consortium. The ENCODE (ENCyclopedia Of DNA Elements) Project. Science 306, 636–640 (2004).
Article
 Google Scholar 
2,317
17
991
1
Thurman, R. E. et al. The accessible chromatin landscape of the human genome. Nature 489, 75–82 (2012).
Article
 CAS PubMed PubMed Central Google Scholar 
2,695
139
2,703
7
Hardison, R. C., Oeltjen, J. & Miller, W. Long human–mouse sequence alignments reveal novel regulatory elements: a reason to sequence the mouse genome. Genome Res. 7, 959–966 (1997).
Article
 CAS PubMed Google Scholar 
308
2
196
0
Pennacchio, L. A. et al. In vivo enhancer analysis of human conserved non-coding sequences. Nature 444, 499–502 (2006).
Article
 CAS PubMed Google Scholar 
1,154
38
1,144
3
Wang, S. K. et al. Single-cell multiome of the human retina and deep learning nominate causal variants in complex eye diseases. Cell Genom. 2, 100164 (2022).
Article
 CAS PubMed PubMed Central Google Scholar 
73
2
103
0
Lieberman-Aiden, E. et al. Comprehensive mapping of long-range interactions reveals folding principles of the human genome. Science 326, 289–293 (2009).
Article
 CAS PubMed PubMed Central Google Scholar 
8,702
478
10,370
9
Mumbach, M. R. et al. HiChIP: efficient and sensitive analysis of protein-directed genome architecture. Nat. Methods 13, 919–922 (2016).
Article
 CAS PubMed PubMed Central Google Scholar 
1,094
20
1,098
0
Ramani, V. et al. Massively multiplex single-cell Hi-C. Nat. Methods 14, 263–266 (2017).
Article
 CAS PubMed PubMed Central Google Scholar 
560
5
438
0
Dixon, J. R. et al. Chromatin architecture reorganization during stem cell differentiation. Nature 518, 331–336 (2015).
Article
 CAS PubMed PubMed Central Google Scholar 
1,627
145
1,709
3
Chen, H. et al. Dynamic interplay between enhancer–promoter topology and gene activity. Nat. Genet. 50, 1296–1303 (2018).
Article
 CAS PubMed PubMed Central Google Scholar 
471
37
430
2
Fukaya, T., Lim, B. & Levine, M. Enhancer control of transcriptional bursting. Cell 166, 358–368 (2016).
Article
 CAS PubMed PubMed Central Google Scholar 
721
69
726
6
Xie, S., Duan, J., Li, B., Zhou, P. & Hon, G. C. Multiplexed engineering and analysis of combinatorial enhancer activity in single cells. Mol. Cell 66, 285–299.e5 (2017).
Article
 CAS PubMed Google Scholar 
324
7
283
0
GTEx Consortium et al. Genetic effects on gene expression across human tissues. Nature 550, 204–213 (2017).
Article
 PubMed Central Google Scholar 
4,175
100
2,870
3
1
van der Wijst, M. G. P. et al. Single-cell RNA sequencing identifies celltype-specific cis-eQTLs and co-expression QTLs. Nat. Genet. 50, 493–497 (2018).
Article
 PubMed PubMed Central Google Scholar 
398
11
425
0
Kerimov, N. et al. A compendium of uniformly processed human gene expression and splicing quantitative trait loci. Nat. Genet. 53, 1290–1299 (2021).
Article
 CAS PubMed PubMed Central Google Scholar 
385
7
403
0
Dixit, A. et al. Perturb-Seq: dissecting molecular circuits with scalable single-cell RNA profiling of pooled genetic screens. Cell 167, 1853–1866.e17 (2016).
Article
 CAS PubMed PubMed Central Google Scholar 
1,631
21
1,641
0
Datlinger, P. et al. Pooled CRISPR screening with single-cell transcriptome readout. Nat. Methods 14, 297–301 (2017).
Article
 CAS PubMed PubMed Central Google Scholar 
1,007
8
1,033
0
Schraivogel, D. et al. Targeted Perturb-seq enables genome-scale genetic screens in single cells. Nat. Methods 17, 629–635 (2020).
Article
 CAS PubMed PubMed Central Google Scholar 
221
5
276
0
Ng, A. H. M. et al. A comprehensive library of human transcription factors for cell fate engineering. Nat. Biotechnol. 39, 510–519 (2021).
Article
 CAS PubMed Google Scholar 
205
3
198
0
Joung, J. et al. A transcription factor atlas of directed differentiation. Cell 186, 209–229.e26 (2023).
Article
 CAS PubMed Google Scholar 
165
0
153
0
1
Littman, R., Wang, N., Peng, C. & Yang, X. SCING: single cell integrative gene regulatory network inference elucidates robust, interpretable gene regulatory networks. Preprint at bioRxiv https://doi.org/10.1101/2022.09.07.506959 (2022).
1
0
0
0
Yurkovsky, E. & Nachman, I. Event timing at the single-cell level. Brief. Funct. Genomics 12, 90–98 (2013).
Article
 CAS PubMed Google Scholar 
42
0
30
0
Co, A. D., Lagomarsino, M. C., Caselle, M. & Osella, M. Stochastic timing in gene expression for simple regulatory strategies. Nucleic Acids Res. 45, 1069–1078 (2017).
Article
 PubMed Google Scholar 
70
2
68
0
Lee, M. Y. Y., Kaestner, K. H. & Li, M. Benchmarking algorithms for joint integration of unpaired and paired single-cell RNA-seq and ATAC-seq data. Preprint at bioRxiv https://doi.org/10.1101/2023.02.01.526609 (2023).
19
0
21
0
Squair, J. W. et al. Confronting false discoveries in single-cell differential expression. Nat. Commun. 12, 5692 (2021).
Article
 CAS PubMed PubMed Central Google Scholar 
800
20
770
1
Kuijjer, M. L., Tung, M. G., Yuan, G., Quackenbush, J. & Glass, K. Estimating sample-specific regulatory networks. iScience 14, 226–240 (2019).
Article
 CAS PubMed PubMed Central Google Scholar 
180
1
284
0
Luecken, M. D. & Theis, F. J. Current best practices in single-cell RNA-seq analysis: a tutorial. Mol. Syst. Biol. 15, e8746 (2019).
Article
 PubMed PubMed Central Google Scholar 
1,924
13
1,787
0
Yan, F., Powell, D. R., Curtis, D. J. & Wong, N. C. From reads to insight: a hitchhiker’s guide to ATAC-seq data analysis. Genome Biol. 21, 22 (2020).
Article
 PubMed PubMed Central Google Scholar 
Vandereyken, K., Sifrim, A., Thienpont, B. & Voet, T. Methods and applications for single-cell and spatial multi-omics. Nat. Rev. Genet. https://doi.org/10.1038/s41576-023-00580-2
(2023).
Article PubMed PubMed Central Google Scholar 
854
1
609
0
Blencowe, M. et al. Network modeling of single-cell omics data: challenges, opportunities, and progresses. Emerg. Top. Life Sci. 3, 379–398 (2019).
Article
 CAS PubMed PubMed Central Google Scholar 
63
0
60
0
Lähnemann, D. et al. Eleven grand challenges in single-cell data science. Genome Biol. 21, 31 (2020).
Article
 PubMed PubMed Central Google Scholar 
van Dijk, D. et al. Recovering gene interactions from single-cell data using data diffusion. Cell 174, 716–729.e27 (2018).
Article
 PubMed PubMed Central Google Scholar 
1,630
15
1,292
0
Bravo González-Blas, C. et al. cisTopic: cis-regulatory topic modeling on single-cell ATAC-seq data. Nat. Methods 16, 397–400 (2019).
Article
 PubMed Google Scholar 
445
3
581
0
Li, Z. et al. Chromatin-accessibility estimation from single-cell ATAC-seq data with scOpen. Nat. Commun. 12, 6386 (2021).
Article
 CAS PubMed PubMed Central Google Scholar 
106
2
98
0
Ly, L.-H. & Vingron, M. Effect of imputation on gene network reconstruction from single-cell RNA-seq data. Patterns 3, 100414 (2022).
Article
 CAS PubMed Google Scholar 
26
1
16
0
Baran, Y. et al. MetaCell: analysis of single-cell RNA-seq data using K–nn graph partitions. Genome Biol. 20, 206 (2019).
Article
 PubMed PubMed Central Google Scholar 
Persad, S. et al. SEACells infers transcriptional and epigenomic cellular states from single-cell genomics data. Nat. Biotechnol. https://doi.org/10.1038/s41587-023-01716-9
(2023).
Article PubMed Google Scholar 
156
0
206
0
Klemm, S. L., Shipony, Z. & Greenleaf, W. J. Chromatin accessibility and the regulatory epigenome. Nat. Rev. Genet. 20, 207–220 (2019).
Article
 CAS PubMed Google Scholar 
1,646
44
1,267
2
Miao, Z. & Kim, J. Is single nucleus ATAC-seq accessibility a qualitative or quantitative measurement? Preprint at bioRxiv https://doi.org/10.1101/2022.04.20.488960 (2022).
7
2
13
0
Martens, L. D., Fischer, D. S., Theis, F. J. & Gagneur, J. Modeling fragment counts improves single-cell ATAC-seq analysis. Preprint at bioRxiv https://doi.org/10.1101/2022.05.04.490536 (2022).
35
1
51
0
Stuart, T., Srivastava, A., Madad, S., Lareau, C. A. & Satija, R. Single-cell chromatin state analysis with Signac. Nat. Methods 18, 1333–1341 (2021).
Article
 CAS PubMed PubMed Central Google Scholar 
1,429
4
1,545
0
2
Granja, J. M. et al. ArchR is a scalable software package for integrative single-cell chromatin accessibility analysis. Nat. Genet. 53, 403–411 (2021).
Article
 CAS PubMed PubMed Central Google Scholar 
1,205
14
1,652
0
2
Bahr, C. et al. Author Correction: a Myc enhancer cluster regulates normal and leukaemic haematopoietic stem cell hierarchies. Nature 558, E4 (2018).
Article
 CAS PubMed Google Scholar 
9
0
2
0
Monahan, K., Horta, A. & Lomvardas, S. LHX2- and LDB1-mediated trans interactions regulate olfactory receptor choice. Nature 565, 448–453 (2019).
Article
 CAS PubMed PubMed Central Google Scholar 
313
14
348
0
Chen, X. et al. Mapping disease regulatory circuits at cell-type resolution from single-cell multiomics data. Preprint at medRxiv https://doi.org/10.1101/2022.12.06.22282077 (2022).
2
0
1
0
Stevens, T. J. et al. 3D structures of individual mammalian genomes studied by single-cell Hi-C. Nature 544, 59–64 (2017).
Article
 CAS PubMed PubMed Central Google Scholar 
838
56
873
6
Flyamer, I. M. et al. Single-nucleus Hi-C reveals unique chromatin reorganization at oocyte-to-zygote transition. Nature 544, 110–114 (2017).
Article
 CAS PubMed PubMed Central Google Scholar 
752
47
816
4
Zhang, R., Zhou, T. & Ma, J. Multiscale and integrative single-cell Hi-C analysis with Higashi. Nat. Biotechnol. 40, 254–261 (2022).
Article
 CAS PubMed Google Scholar 
168
2
180
0
2
Yu, M. & Ren, B. The three-dimensional organization of mammalian genomes. Annu. Rev. Cell Dev. Biol. 33, 265–289 (2017).
Article
 CAS PubMed PubMed Central Google Scholar 
369
6
312
0
Marti-Renom, M. A. et al. Challenges and guidelines toward 4D nucleome data and model standards. Nat. Genet. 50, 1352–1358 (2018).
Article
 CAS PubMed Google Scholar 
56
0
49
0
Rossini, R., Kumar, V., Mathelier, A., Rognes, T. & Paulsen, J. MoDLE: high-performance stochastic modeling of DNA loop extrusion interactions. Genome Biol. 23, 247 (2022).
Article
 CAS PubMed PubMed Central Google Scholar 
Tan, J. et al. Cell-type-specific prediction of 3D chromatin organization enables high-throughput in silico genetic screening. Nat. Biotechnol. https://doi.org/10.1038/s41587-022-01612-8
(2023). This work demonstrates that the prediction of Hi-C data from chromatin accessibility is a promising strategy to replace the use of genomic distance thresholds.
Article PubMed PubMed Central Google Scholar 
93
4
106
0
Yuan, H. & Kelley, D. R. scBasset: sequence-based modeling of single-cell ATAC-seq using convolutional neural networks. Nat. Methods 19, 1088–1096 (2022). This work introduces the concept of in silico mutagenesis to contextualize TF binding motifs to cell types.
Article
 CAS PubMed Google Scholar 
111
1
133
0
1
Taskiran, I. I., Spanier, K. I., Christiaens, V., Mauduit, D. & Aerts, S. Cell type directed design of synthetic enhancers. Preprint at bioRxiv https://doi.org/10.1101/2022.07.26.501466 (2022).
60
3
106
0
Lundberg, S. M. & Lee, S.-I. A unified approach to interpreting model predictions. Adv. Neural Inf. Process. Syst. 30, 4765–4774 (2017).
Google Scholar 
Regev, A. et al. The human cell atlas. eLife 6, e27041 (2017).
Article
 PubMed PubMed Central Google Scholar 
2,265
6
1,369
0
HuBMAP Consortium. The human body at cellular resolution: the NIH Human Biomolecular Atlas Program. Nature 574, 187–192 (2019).
Article
 CAS Google Scholar 
576
0
246
0
Neikes, H. K. et al. Quantification of absolute transcription factor binding affinities in the native chromatin context using BANC-seq. Nat. Biotechnol. https://doi.org/10.1038/s41587-023-01715-w
(2023).
Article PubMed Google Scholar 
24
0
11
0
Xu, W. et al. ISSAAC-seq enables sensitive and flexible multimodal profiling of chromatin accessibility and gene expression in single cells. Nat. Methods 19, 1243–1249 (2022).
Article
 CAS PubMed Google Scholar 
90
1
65
0
Ogbeide, S., Giannese, F., Mincarelli, L. & Macaulay, I. C. Into the multiverse: advances in single-cell multiomic profiling. Trends Genet. 38, 831–843 (2022).
Article
 CAS PubMed Google Scholar 
79
0
53
0
Chen, A. F. et al. NEAT-seq: simultaneous profiling of intra-nuclear proteins, chromatin accessibility and gene expression in single cells. Nat. Methods 19, 547–553 (2022).
Article
 CAS PubMed Google Scholar 
117
1
78
0
Yan, R., Cheng, X. & Guo, F. Protocol for scChaRM-seq: simultaneous profiling of gene expression, DNA methylation, and chromatin accessibility in single cells. STAR Protoc. 2, 100972 (2021).
Article
 CAS PubMed PubMed Central Google Scholar 
10
0
3
0
Hansen, T. J. & Hodges, E. ATAC-STARR-seq reveals transcription factor-bound activators and silencers within chromatin-accessible regions of the human genome. Genome Res. 32, 1529–1541 (2022).
Article
 PubMed PubMed Central Google Scholar 
51
6
56
1
Budnik, B., Levy, E., Harmange, G. & Slavov, N. SCoPE-MS: mass spectrometry of single mammalian cells quantifies proteome heterogeneity during cell differentiation. Genome Biol. 19, 161 (2018).
Article
 PubMed PubMed Central Google Scholar 
Blair, J. D. et al. Phospho-seq: integrated, multi-modal profiling of intracellular protein dynamics in single cells. Preprint at bioRxiv https://doi.org/10.1101/2023.03.27.534442 (2023).
16
0
18
0
Uffelmann, E. et al. Genome-wide association studies. Nat. Rev. Methods Prim. 1, 1–21 (2021).
Google Scholar 
Tedesco, M. et al. Chromatin velocity reveals epigenetic dynamics by single-cell profiling of heterochromatin and euchromatin. Nat. Biotechnol. 40, 235–244 (2022).
Article
 CAS PubMed Google Scholar 
120
5
117
0
Jerkovic, I. & Cavalli, G. Understanding 3D genome organization by multidisciplinary methods. Nat. Rev. Mol. Cell Biol. 22, 511–528 (2021).
Article
 CAS PubMed Google Scholar 
349
1
232
0
Hsieh, T.-H. S. et al. Mapping nucleosome resolution chromosome folding in yeast by Micro-C. Cell 162, 108–119 (2015).
Article
 CAS PubMed PubMed Central Google Scholar 
750
59
778
5
Zhang, Y. et al. Enhancing Hi-C data resolution with deep convolutional neural network HiCPlus. Nat. Commun. 9, 750 (2018).
Article
 PubMed PubMed Central Google Scholar 
200
0
224
0
Lance, C. et al. Multimodal single cell data integration challenge: Results and lessons learned. In Proc. NeurIPS 2021 Competitions and Demonstrations Track (eds. Kiela, D., Ciccone, M. & Caputo, B.) Vol. 176, 162–176 (PMLR, 2022).
Rappez, L. et al. SpaceM reveals metabolic states of single cells. Nat. Methods 18, 799–805 (2021).
Article
 CAS PubMed PubMed Central Google Scholar 
302
3
302
0
Garrido-Rodriguez, M., Zirngibl, K., Ivanova, O., Lobentanzer, S. & Saez-Rodriguez, J. Integrating knowledge and omics to decipher mechanisms via large-scale models of signaling networks. Mol. Syst. Biol. 18, e11036 (2022).
Article
 PubMed PubMed Central Google Scholar 
59
0
44
0
Browaeys, R., Saelens, W. & Saeys, Y. NicheNet: modeling intercellular communication by linking ligands to target genes. Nat. Methods 17, 159–162 (2020).
Article
 CAS PubMed Google Scholar 
1,708
7
1,851
0
Armingol, E., Officer, A., Harismendy, O. & Lewis, N. E. Deciphering cell–cell interactions and communication from gene expression. Nat. Rev. Genet. 22, 71–88 (2021).
Article
 CAS PubMed Google Scholar 
1,126
6
1,040
1
Dimitrov, D. et al. Comparison of methods and resources for cell–cell communication inference from single-cell RNA-seq data. Nat. Commun. 13, 3224 (2022).
Article
 PubMed PubMed Central Google Scholar 
448
8
461
0
Tanevski, J., Flores, R. O. R., Gabor, A., Schapiro, D. & Saez-Rodriguez, J. Explainable multiview framework for dissecting spatial relationships from highly multiplexed data. Genome Biol. 23, 97 (2022).
Article
 PubMed PubMed Central Google Scholar 
Fischer, D. S., Schaar, A. C. & Theis, F. J. Modeling intercellular communication in tissues using spatial graphs of cells. Nat. Biotechnol. 41, 332–336 (2023).
Article
 CAS PubMed Google Scholar 
170
10
138
0
Zhang, D. et al. Spatial epigenome-transcriptome co-profiling of mammalian tissues. Nature 616, 113–122 (2023).
Article
 CAS PubMed PubMed Central Google Scholar 
299
11
276
0
Avsec, Ž. et al. Effective gene expression prediction from sequence by integrating long-range interactions. Nat. Methods 18, 1196–1203 (2021).
Article
 CAS PubMed PubMed Central Google Scholar 
987
16
1,412
0
Li, Z. et al. Applications of deep learning in understanding gene regulation. Cell Rep. Methods 3, 100384 (2023).
Article
 CAS PubMed PubMed Central Google Scholar 
43
0
29
0
Miraldi, E. R. et al. Leveraging chromatin accessibility for transcriptional regulatory network inference in T helper 17 cells. Genome Res. 29, 449–463 (2019).
Article
 CAS PubMed PubMed Central Google Scholar 
116
3
169
0
Alanis-Lobato, G. et al. MICA: a multi-omics method to predict gene regulatory networks in early human embryos. Preprint at bioRxiv https://doi.org/10.1101/2023.02.03.527081 (2023).
12
1
35
0
Zenere, A., Rundquist, O., Gustafsson, M. & Altafini, C. Using high-throughput multi-omics data to investigate structural balance in elementary gene regulatory network motifs. Bioinformatics 38, 173–178 (2021).
Article
 PubMed PubMed Central Google Scholar 
8
0
8
0
Ledru, N. et al. Predicting regulators of epithelial cell state through regularized regression analysis of single cell multiomic sequencing. Preprint at bioRxiv https://doi.org/10.1101/2022.12.29.522232 (2022).
10
0
10
0
Jiang, Y. et al. Nonparametric single-cell multiomic characterization of trio relationships between transcription factors, target genes, and cis-regulatory regions. Cell Syst. 13, 737–751.e4 (2022).
Article
 CAS PubMed PubMed Central Google Scholar 
35
0
53
0
Zambelli, F., Pesole, G. & Pavesi, G. Motif discovery and transcription factor binding sites before and after the next-generation sequencing era. Brief. Bioinform 14, 225–237 (2013).
Article
 CAS PubMed Google Scholar 
141
0
115
0
Weirauch, M. T. et al. Determination and inference of eukaryotic transcription factor sequence specificity. Cell 158, 1431–1443 (2014).
Article
 CAS PubMed PubMed Central Google Scholar 
1,895
36
2,200
1
Kheradpour, P. & Kellis, M. Systematic discovery and characterization of regulatory motifs in ENCODE TF binding experiments. Nucleic Acids Res. 42, 2976–2987 (2014).
Article
 CAS PubMed Google Scholar 
480
14
546
0
Kulakovskiy, I. V. et al. HOCOMOCO: towards a complete collection of transcription factor binding models for human and mouse via large-scale ChIP-seq analysis. Nucleic Acids Res. 46, D252–D259 (2018).
Article
 CAS PubMed Google Scholar 
918
13
889
0
Castro-Mondragon, J. A. et al. JASPAR 2022: the 9th release of the open-access database of transcription factor binding profiles. Nucleic Acids Res. 50, D165–D173 (2022).
Article
 CAS PubMed Google Scholar 
1,808
13
1,519
0
Matys, V. TRANSFAC® and its module TRANSCompel®: transcriptional gene regulation in eukaryotes. Nucleic Acids Res. 34, D108–D110 (2006).
Article
 CAS PubMed Google Scholar 
2,146
11
1,954
0
Newburger, D. E. & Bulyk, M. L. UniPROBE: an online database of protein binding microarray data on protein–DNA interactions. Nucleic Acids Res. 37, D77–D82 (2009).
Article
 CAS PubMed Google Scholar 
369
3
352
0
Grant, C. E., Bailey, T. L. & Noble, W. S. FIMO: scanning for occurrences of a given motif. Bioinformatics 27, 1017–1018 (2011).
Article
 CAS PubMed PubMed Central Google Scholar 
4,333
15
4,137
0
Bruse, N. & van Heeringen, S. J. GimmeMotifs: an analysis framework for transcription factor motif analysis. Preprint at bioRxiv https://doi.org/10.1101/474403 (2018).
80
0
117
0
Korhonen, J. H., Palin, K., Taipale, J. & Ukkonen, E. Fast motif matching revisited: high-order PWMs, SNPs and indels. Bioinformatics 33, 514–521 (2017).
Article
 CAS PubMed Google Scholar 
45
0
30
0
Schep, A. N., Wu, B., Buenrostro, J. D. & Greenleaf, W. J. chromVAR: inferring transcription-factor-associated accessibility from single-cell epigenomic data. Nat. Methods 14, 975–978 (2017).
Article
 CAS PubMed PubMed Central Google Scholar 
1,581
21
1,715
0
Li, Z. et al. RGT: a toolbox for the integrative analysis of high throughput regulatory genomics data. BMC Bioinforma. 24, 79 (2023).
Article
 CAS Google Scholar 
Sherwood, R. I. et al. Discovery of directional and nondirectional pioneer transcription factors by modeling DNase profile magnitude and shape. Nat. Biotechnol. 32, 171–178 (2014).
Article
 CAS PubMed PubMed Central Google Scholar 
453
22
531
1
Ambrosini, G., Groux, R. & Bucher, P. PWMScan: a fast tool for scanning entire genomes with a position-specific weight matrix. Bioinformatics 34, 2483–2484 (2018).
Article
 CAS PubMed PubMed Central Google Scholar 
167
2
154
0
Janssens, J. et al. Decoding gene regulation in the fly brain. Nature 601, 630–636 (2022).
Article
 CAS PubMed Google Scholar 
165
3
166
0
Wayman, J. A. et al. An atlas of gene regulatory networks for memory CD4+ T cells in youth and old age. Preprint at bioRxiv https://doi.org/10.1101/2023.03.07.531590 (2023).
7
1
25
0
Download references
Acknowledgements
The authors thank the developers of the methods discussed for the insightful feedback they provided. S.M.-D. was funded by the LiSyM-cancer network supported by the German Federal Ministry of Education and Research (BMBF; Funding number 031L0257B).
Author information
Authors and Affiliations
Heidelberg University, Faculty of Medicine, Heidelberg University Hospital, Institute for Computational Biomedicine, Bioquant, Heidelberg, Germany
Pau Badia-i-Mompel, Lorna Wessels, Sophia Müller-Dott, Rémi Trimbour, Ricardo O. Ramirez Flores & Julio Saez-Rodriguez
Department of Vascular Biology and Tumor Angiogenesis, European Center for Angioscience, Medical Faculty, MannHeim Heidelberg University, Mannheim, Germany
Lorna Wessels
Institut Pasteur, Université Paris Cité, CNRS UMR 3738, Machine Learning for Integrative Genomics Group, Paris, France
Rémi Trimbour
Altos Labs, Granta Park, Cambridge, UK
Ricard Argelaguet
Contributions
All authors researched data for the article. P.B.-i-M., L.W., S.M.-D., R.O.R.F., R.A. and J.S.-R. contributed substantially to discussion of the content. P.B.-i-M., L.W., R.A. and J.S.-R. wrote the article. All authors reviewed and/or edited the manuscript before submission.
Corresponding author
Correspondence to Julio Saez-Rodriguez.
Ethics declarations
Competing interests
J.S.-R. reports funding from GSK, Pfizer and Sanofi, and consultant fees from Travere Therapeutics, Stadapharm and Astex Pharmaceutical. R.A. is an employee of Altos Labs. The other authors declare no competing interests.
Peer review
Peer review information
Nature Reviews Genetics thanks X. Yang and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.
Additional information
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
Supplementary information
Supplementary Information
Glossary
Assay for transpose-accessible chromatin with sequencing
(ATAC-seq). A technique to identify accessible DNA regions using hyperactive Tn5 transposase.
Betweenness centrality
A network centrality measure representing the number of appearances of a node in the shortest path of any other two nodes in the network.
Chromatin
A higher-order filamentous structure of DNA–protein complex that can exist in a condensed or uncondensed state.
Chromatin immunoprecipitation followed by sequencing
(ChIP-seq). A technique to analyse protein interactions with accessible DNA regions using chromatin immunoprecipitation followed by DNA sequencing.
cis-Regulatory elements
(CREs). Non-coding DNA regions that regulate the transcription of nearby genes upon binding of transcription factors (TFs). These include promoters, enhancers and silencers.
Cleavage under targets and tagmentation
(CUT&Tag). An antibody-based technique to analyse protein interactions with accessible DNA regions using transposase Tn5-mediated tagmentation followed by DNA sequencing.
Closeness centrality
A network centrality measure describing the average distance (length of the shortest path) of a node to all other nodes.
Degree centrality
A network centrality measure describing the number of edges (degree) of a node.
DNA binding sites
DNA sequences where transcription factors can bind to drive gene regulation, usually represented as nucleotide patterns known as motifs.
Eigenvector centrality
A network centrality measure describing the importance of a node in the network based on the centrality of its neighbours.
Enhancers
Distal regulatory DNA regions where transcription regulatory proteins can bind and activate transcription.
Expression quantitative trait loci
Genomic locations whose sequence variation is associated with changes in gene expression.
Gene regulatory networks
(GRNs). Network representations of molecular interactions between transcriptional regulators and target genes.
Genome-wide association studies
Analysis approach to identify frequently appearing single-nucleotide polymorphisms in the genome across a large cohort of individuals.
Hi-C
A technique to study chromatin conformation in three dimensions to identify genomic sequences that might be distal to each other in linear distance but closer in the 3D space.
Metacells
Groups of cells with a similar molecular profile that can be aggregated into a single omics profile to reduce sparsity of the data.
Motif matcher algorithms
String matching algorithms to detect transcription factor binding sites in DNA sequences.
Network centrality
A group of graph theory metrics that defines the relative importance of a node in a network.
Peaks
Regions of accessible chromatin that form the read-out of epigenetic sequencing techniques.
Promoter
A regulatory region in the genome located before the transcriptional start site of a gene.
Silencers
Distal regulatory DNA regions where transcription regulatory proteins can bind and repress transcription.
Single-nucleotide polymorphisms
(SNPs). DNA sequence variations caused by substitution of a single nucleotide in a specific position.
Topologically associating domains
Self-interacting genomic regions with high interaction frequency of sequences within the domain and relative isolation from neighbouring regions, forming a 3D chromosome structure.
Transcription factors
(TFs). Proteins that modify the rate of transcription by binding to specific DNA sequences.
Rights and permissions
Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.
Reprints and permissions
About this article
Check for updates. Verify currency and authenticity via CrossMark
Cite this article
Badia-i-Mompel, P., Wessels, L., Müller-Dott, S. et al. Gene regulatory network inference in the era of single-cell multi-omics. Nat Rev Genet 24, 739–754 (2023). https://doi.org/10.1038/s41576-023-00618-5
Download citation
Accepted
12 May 2023
Published
26 June 2023
Issue date
November 2023
DOI
https://doi.org/10.1038/s41576-023-00618-5
Share this article
Anyone you share the following link with will be able to read this content:
Get shareable link
Provided by the Springer Nature SharedIt content-sharing initiative
Subjects
Gene regulatory networks
Regulatory networks
This article is cited by
ATP6V0A4 as a novel prognostic biomarker and potential therapeutic target in oral squamous cell carcinoma
BMC Oral Health (2025)
0
0
0
0
Xiaopu GaoJiamin ZhouSongkai Huang
LNP-enclosed NamiRNA inhibits pancreatic cancer proliferation and migration via dual pathways
Journal of Nanobiotechnology (2025)
0
0
0
0
Chao YuZhou FangRufu Chen
Gene2role: a role-based gene embedding method for comparative analysis of signed gene regulatory networks
BMC Bioinformatics (2025)
1
0
1
0
Xin ZengShu LiuKenta Nakai
Efficient structure learning of gene regulatory networks with Bayesian active learning
BMC Bioinformatics (2025)
0
0
0
0
Dániel SándorPéter Antal
Modeling combinatorial regulation from single-cell multi-omics provides regulatory units underpinning cell type landscape using cRegulon
Genome Biology (2025)
1
0
0
0
Zhanying FengXi ChenWing Hung Wong
You have full access to this article via Hong Kong Baptist University Library.
Download PDF
Associated content
Focus
Single-cell omics
Sections
Figures
References
Abstract
Introduction
Inference of GRNs
Downstream GRN analyses
Experimental assessment of GRNs
Challenges and future directions
Conclusions
References
Acknowledgements
Author information
Ethics declarations
Peer review
Additional information
Supplementary information
Glossary
Rights and permissions
About this article
This article is cited by
Advertisement
Nature Reviews Genetics (Nat Rev Genet)
 
ISSN
 1471-0064 (online)
 
ISSN
 1471-0056 (print)