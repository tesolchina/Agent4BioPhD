#!/usr/bin/env Rscript
# -*- coding: utf-8 -*-

"""
motifmatchr Demo: Transcription Factor Binding Site Analysis

This script demonstrates how to use the motifmatchr R package to:
1. Load DNA sequence data
2. Fetch transcription factor motif databases
3. Identify transcription factor binding sites
4. Visualize and analyze motif matches

Note: This demo requires the motifmatchr package and its dependencies to be installed.
For installation instructions, see the README.md file.
"""

# Check if required packages are installed and load them
required_packages <- c("motifmatchr", "GenomicRanges", "BiocParallel", "JASPAR2020", 
                      "TFBSTools", "BSgenome.Hsapiens.UCSC.hg38")

# Function to install missing packages
install_if_missing <- function(packages) {
  new_packages <- packages[!(packages %in% installed.packages()[, "Package"])]
  if (length(new_packages) > 0) {
    message("Installing missing packages: ", paste(new_packages, collapse = ", "))
    BiocManager::install(new_packages)
  }
  return(TRUE)
}

# Try to load packages with fallback to mock data
library_loaded <- FALSE
tryCatch({
  # Check if BiocManager is installed
  if (!requireNamespace("BiocManager", quietly = TRUE)) {
    install.packages("BiocManager")
  }
  
  # Install missing packages
  install_if_missing(required_packages)
  
  # Load packages
  suppressPackageStartupMessages({
    library(motifmatchr)
    library(GenomicRanges)
    library(BiocParallel)
    library(JASPAR2020)
    library(TFBSTools)
    library(BSgenome.Hsapiens.UCSC.hg38)
  })
  
  message("All required packages loaded successfully.")
  library_loaded <- TRUE
}, error = function(e) {
  message("Warning: Could not load all required packages.")
  message("Error: ", e$message)
  message("This demo will use mock data for demonstration purposes.")
})

# Mock data generation function when packages aren't available
create_mock_motif_results <- function() {
  message("Generating mock motif match results for demonstration...")
  
  # Create mock GRanges object for target regions
  mock_regions <- data.frame(
    seqnames = c("chr1", "chr2", "chr3", "chr4", "chr5"),
    start = c(1000000, 2000000, 3000000, 4000000, 5000000),
    end = c(1001000, 2001000, 3001000, 4001000, 5001000),
    gene_id = c("GENE1", "GENE2", "GENE3", "GENE4", "GENE5")
  )
  
  # Create mock motif matches
  mock_matches <- list(
    "MYC" = data.frame(
      seqnames = c("chr1", "chr3"),
      start = c(1000100, 3000300),
      end = c(1000110, 3000310),
      strand = c("+", "+"),
      gene_id = c("GENE1", "GENE3")
    ),
    "TP53" = data.frame(
      seqnames = c("chr2", "chr4", "chr5"),
      start = c(2000200, 4000400, 5000500),
      end = c(2000210, 4000410, 5000510),
      strand = c("+", "-", "+"),
      gene_id = c("GENE2", "GENE4", "GENE5")
    ),
    "NFKB1" = data.frame(
      seqnames = c("chr1", "chr3", "chr5"),
      start = c(1000500, 3000700, 5000900),
      end = c(1000510, 3000710, 5000910),
      strand = c("-", "+", "-")
    )
  )
  
  # Create summary statistics
  mock_summary <- data.frame(
    motif_name = c("MYC", "TP53", "NFKB1"),
    num_matches = c(2, 3, 3),
    num_regions = c(2, 3, 3),
    avg_per_region = c(1.0, 1.0, 1.0)
  )
  
  return(list(
    regions = mock_regions,
    matches = mock_matches,
    summary = mock_summary
  ))
}

# Function to load example genomic regions
load_example_regions <- function() {
  if (library_loaded) {
    message("Loading example genomic regions...")
    
    # Create a simple set of genomic ranges
    gr <- GRanges(
      seqnames = c("chr1", "chr2", "chr3", "chr4", "chr5"),
      ranges = IRanges(
        start = c(1000000, 2000000, 3000000, 4000000, 5000000),
        end = c(1001000, 2001000, 3001000, 4001000, 5001000)
      )
    )
    
    # Add gene IDs as metadata
    mcols(gr)$gene_id <- c("GENE1", "GENE2", "GENE3", "GENE4", "GENE5")
    
    return(gr)
  } else {
    message("Using mock genomic regions...")
    return(create_mock_motif_results()$regions)
  }
}

# Function to load example motifs
load_example_motifs <- function() {
  if (library_loaded) {
    message("Loading example transcription factor motifs from JASPAR...")
    
    # Get matrices for some common TFs
    opts <- list()
    opts[['species']] <- 9606  # Human
    opts[['matrixtype']] <- "PFM"
    
    # Get motifs for a few transcription factors
    tfs <- c("MYC", "TP53", "NFKB1")
    pfms <- getMatrixSet(JASPAR2020, opts)
    pfms_subset <- pfms[names(pfms) %in% tfs]
    
    return(pfms_subset)
  } else {
    message("Using mock motifs...")
    return(c("MYC", "TP53", "NFKB1"))  # Just return TF names as mock
  }
}

# Function to find motif matches
find_motif_matches <- function(regions, motifs) {
  if (library_loaded) {
    message("Finding motif matches in genomic regions...")
    
    # Find motif matches using motifmatchr
    matches <- matchMotifs(
      pwms = motifs,
      subject = regions,
      genome = BSgenome.Hsapiens.UCSC.hg38,
      out = "positions"
    )
    
    # Return the matches
    return(matches)
  } else {
    message("Using mock motif match results...")
    return(create_mock_motif_results()$matches)
  }
}

# Function to summarize motif matches
summarize_motif_matches <- function(regions, matches) {
  message("Summarizing motif matches...")
  
  if (library_loaded) {
    # Count matches per motif
    summary_stats <- data.frame()
    
    for (i in seq_along(matches)) {
      motif_name <- names(matches)[i]
      motif_matches <- matches[[i]]
      
      num_matches <- length(motif_matches)
      num_regions <- length(unique(seqnames(motif_matches)))
      avg_per_region <- num_matches / num_regions
      
      summary_stats <- rbind(summary_stats, data.frame(
        motif_name = motif_name,
        num_matches = num_matches,
        num_regions = num_regions,
        avg_per_region = avg_per_region
      ))
    }
    
    return(summary_stats)
  } else {
    return(create_mock_motif_results()$summary)
  }
}

# Function to save results
save_motif_results <- function(matches, summary) {
  message("Saving motif analysis results...")
  
  # Create output directory
  output_dir <- "outputs"
  if (!dir.exists(output_dir)) {
    dir.create(output_dir)
  }
  
  # Save summary to CSV
  summary_file <- file.path(output_dir, "motif_analysis_summary.csv")
  write.csv(summary, file = summary_file, row.names = FALSE)
  message(paste("Summary saved to:", summary_file))
  
  # Save detailed matches (in real scenario, this would save the GRanges objects)
  matches_file <- file.path(output_dir, "motif_analysis_matches.txt")
  
  # Write mock detailed matches for demonstration
  if (!library_loaded) {
    con <- file(matches_file, "w")
    writeLines("=== Detailed Motif Matches ===", con)
    
    for (tf_name in names(matches)) {
      writeLines(paste("\nTranscription Factor:", tf_name), con)
      writeLines("Matches:", con)
      
      for (i in 1:nrow(matches[[tf_name]])) {
        match <- matches[[tf_name]][i, ]
        match_str <- paste(match$seqnames, match$start, match$end, match$strand, 
                          sep = ":")
        if (!is.null(match$gene_id)) {
          match_str <- paste(match_str, "(Gene:", match$gene_id, ")", sep = " ")
        }
        writeLines(paste("  ", match_str), con)
      }
    }
    close(con)
    message(paste("Detailed matches saved to:", matches_file))
  }
  
  return(list(summary_file = summary_file, matches_file = matches_file))
}

# Main function
main <- function() {
  cat("\n=== motifmatchr Demo: Transcription Factor Binding Site Analysis ===\n")
  cat("This demo shows how to use the motifmatchr R package\n")
  cat("for identifying transcription factor binding sites.\n\n")
  
  # Step 1: Load example genomic regions
  regions <- load_example_regions()
  cat("Number of genomic regions loaded:", 
      ifelse(library_loaded, length(regions), nrow(regions)), "\n")
  
  # Step 2: Load example motifs
  motifs <- load_example_motifs()
  cat("Number of motifs loaded:", 
      ifelse(library_loaded, length(motifs), length(motifs)), "\n")
  if (!library_loaded) {
    cat("Motifs:", paste(motifs, collapse = ", "), "\n")
  } else {
    cat("Motifs:", paste(names(motifs), collapse = ", "), "\n")
  }
  
  # Step 3: Find motif matches
  matches <- find_motif_matches(regions, motifs)
  cat("Motif matching completed.\n")
  
  # Step 4: Summarize results
  summary <- summarize_motif_matches(regions, matches)
  cat("\nSummary of motif matches:\n")
  print(summary)
  
  # Step 5: Save results
  saved_files <- save_motif_results(matches, summary)
  
  cat("\n=== motifmatchr Demo Complete ===\n")
  cat("\nFiles saved:")
  cat("\n-", saved_files$summary_file)
  cat("\n-", saved_files$matches_file)
  
  cat("\n\nNext Steps:")
  cat("\n1. Install all required packages:")
  cat("\n   BiocManager::install(c('motifmatchr', 'GenomicRanges', 'BiocParallel', ")
  cat("\n                          'JASPAR2020', 'TFBSTools', 'BSgenome.Hsapiens.UCSC.hg38'))")
  cat("\n2. Use your own genomic regions of interest")
  cat("\n3. Explore additional TFs from JASPAR database")
  cat("\n4. Integrate with gene expression data for functional analysis")
  cat("\n5. Combine with the litstudy Python package for comprehensive analysis")
}

# Run main function
main()