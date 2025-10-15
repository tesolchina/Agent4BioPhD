#!/usr/bin/env python3
"""
Gene Regulatory Network Analysis Script

This script demonstrates basic GRN analysis tasks that could be automated
by AI agents for biology research. It includes functions for:
- Loading and preprocessing single-cell data
- Computing gene-gene correlations
- Identifying transcription factors
- Visualizing network structures
- Performing basic network analysis

Based on concepts from Badia-i-Mompel et al. (2023) Nature Reviews Genetics
"""

import numpy as np
import pandas as pd
from typing import List, Dict, Tuple, Optional
import warnings

warnings.filterwarnings('ignore')


class GRNAnalyzer:
    """
    A class to perform basic gene regulatory network analysis.
    """
    
    def __init__(self, expression_data: pd.DataFrame):
        """
        Initialize the GRN analyzer with expression data.
        
        Args:
            expression_data: DataFrame with genes as rows and cells as columns
        """
        self.expression_data = expression_data
        self.correlation_matrix = None
        self.network_edges = None
        
    def preprocess_data(self, 
                       min_cells: int = 10, 
                       min_counts: int = 1,
                       log_transform: bool = True) -> pd.DataFrame:
        """
        Preprocess expression data by filtering and normalizing.
        
        Args:
            min_cells: Minimum number of cells a gene must be expressed in
            min_counts: Minimum counts threshold
            log_transform: Whether to apply log transformation
            
        Returns:
            Preprocessed expression data
        """
        # Filter genes expressed in minimum number of cells
        genes_to_keep = (self.expression_data > min_counts).sum(axis=1) >= min_cells
        filtered_data = self.expression_data.loc[genes_to_keep]
        
        print(f"Filtered from {self.expression_data.shape[0]} to {filtered_data.shape[0]} genes")
        
        # Log transformation
        if log_transform:
            filtered_data = np.log1p(filtered_data)
            
        # Z-score normalization per gene
        normalized_data = (filtered_data - filtered_data.mean(axis=1).values.reshape(-1, 1)) / \
                         (filtered_data.std(axis=1).values.reshape(-1, 1) + 1e-8)
        
        self.expression_data = normalized_data
        return normalized_data
    
    def compute_correlations(self, method: str = 'pearson') -> pd.DataFrame:
        """
        Compute gene-gene correlation matrix.
        
        Args:
            method: Correlation method ('pearson' or 'spearman')
            
        Returns:
            Correlation matrix
        """
        if method == 'pearson':
            self.correlation_matrix = self.expression_data.T.corr()
        elif method == 'spearman':
            self.correlation_matrix = self.expression_data.T.corr(method='spearman')
        else:
            raise ValueError(f"Unknown method: {method}")
            
        print(f"Computed {method} correlation for {self.correlation_matrix.shape[0]} genes")
        return self.correlation_matrix
    
    def identify_tf_targets(self, 
                           tf_list: List[str], 
                           threshold: float = 0.5,
                           top_n: Optional[int] = None) -> Dict[str, List[Tuple[str, float]]]:
        """
        Identify potential target genes for given transcription factors.
        
        Args:
            tf_list: List of transcription factor gene names
            threshold: Correlation threshold for considering a target
            top_n: If specified, return only top N targets per TF
            
        Returns:
            Dictionary mapping TF names to list of (target, correlation) tuples
        """
        if self.correlation_matrix is None:
            self.compute_correlations()
        
        tf_targets = {}
        
        for tf in tf_list:
            if tf not in self.correlation_matrix.index:
                print(f"Warning: {tf} not found in expression data")
                continue
                
            # Get correlations for this TF
            correlations = self.correlation_matrix.loc[tf]
            
            # Filter by threshold and exclude self-correlation
            targets = correlations[
                (np.abs(correlations) >= threshold) & 
                (correlations.index != tf)
            ]
            
            # Sort by absolute correlation value
            targets = targets.reindex(
                targets.abs().sort_values(ascending=False).index
            )
            
            if top_n is not None:
                targets = targets.head(top_n)
            
            tf_targets[tf] = [(gene, corr) for gene, corr in targets.items()]
            
        return tf_targets
    
    def build_network(self, 
                     threshold: float = 0.6,
                     min_targets: int = 5) -> pd.DataFrame:
        """
        Build a network from correlation matrix.
        
        Args:
            threshold: Correlation threshold for edge inclusion
            min_targets: Minimum number of targets for a node to be included
            
        Returns:
            DataFrame with columns: source, target, weight
        """
        if self.correlation_matrix is None:
            self.compute_correlations()
        
        edges = []
        
        # Extract edges above threshold
        for i, gene1 in enumerate(self.correlation_matrix.index):
            for j, gene2 in enumerate(self.correlation_matrix.columns):
                if i < j:  # Avoid duplicates and self-loops
                    corr = self.correlation_matrix.iloc[i, j]
                    if abs(corr) >= threshold:
                        edges.append({
                            'source': gene1,
                            'target': gene2,
                            'weight': corr
                        })
        
        self.network_edges = pd.DataFrame(edges)
        
        # Filter nodes with minimum targets
        node_counts = pd.concat([
            self.network_edges['source'].value_counts(),
            self.network_edges['target'].value_counts()
        ], axis=1).fillna(0).sum(axis=1)
        
        valid_nodes = node_counts[node_counts >= min_targets].index
        self.network_edges = self.network_edges[
            self.network_edges['source'].isin(valid_nodes) |
            self.network_edges['target'].isin(valid_nodes)
        ]
        
        print(f"Built network with {len(self.network_edges)} edges")
        return self.network_edges
    
    def network_statistics(self) -> Dict[str, float]:
        """
        Compute basic network statistics.
        
        Returns:
            Dictionary of network statistics
        """
        if self.network_edges is None:
            raise ValueError("Network has not been built yet")
        
        # Get all nodes
        nodes = set(self.network_edges['source']) | set(self.network_edges['target'])
        n_nodes = len(nodes)
        n_edges = len(self.network_edges)
        
        # Compute degree distribution
        degrees = pd.concat([
            self.network_edges['source'].value_counts(),
            self.network_edges['target'].value_counts()
        ], axis=1).fillna(0).sum(axis=1)
        
        stats = {
            'n_nodes': n_nodes,
            'n_edges': n_edges,
            'density': n_edges / (n_nodes * (n_nodes - 1) / 2),
            'mean_degree': degrees.mean(),
            'median_degree': degrees.median(),
            'max_degree': degrees.max()
        }
        
        return stats
    
    def identify_hub_genes(self, top_n: int = 10) -> pd.DataFrame:
        """
        Identify hub genes (highly connected nodes).
        
        Args:
            top_n: Number of top hubs to return
            
        Returns:
            DataFrame with hub genes and their degrees
        """
        if self.network_edges is None:
            raise ValueError("Network has not been built yet")
        
        # Compute degree for each node
        degrees = pd.concat([
            self.network_edges['source'].value_counts(),
            self.network_edges['target'].value_counts()
        ], axis=1).fillna(0).sum(axis=1)
        
        hubs = degrees.sort_values(ascending=False).head(top_n)
        
        return pd.DataFrame({
            'gene': hubs.index,
            'degree': hubs.values
        })
    
    def export_network(self, filename: str, format: str = 'edgelist'):
        """
        Export network to file.
        
        Args:
            filename: Output filename
            format: Export format ('edgelist', 'gml', 'graphml')
        """
        if self.network_edges is None:
            raise ValueError("Network has not been built yet")
        
        if format == 'edgelist':
            self.network_edges.to_csv(filename, sep='\t', index=False)
            print(f"Network exported to {filename}")
        else:
            print(f"Format {format} not yet implemented")


def generate_synthetic_data(n_genes: int = 100, 
                            n_cells: int = 500,
                            n_modules: int = 5) -> pd.DataFrame:
    """
    Generate synthetic expression data for demonstration.
    
    Args:
        n_genes: Number of genes
        n_cells: Number of cells
        n_modules: Number of co-expressed gene modules
        
    Returns:
        Synthetic expression DataFrame
    """
    np.random.seed(42)
    
    # Create gene modules
    genes_per_module = n_genes // n_modules
    expression_data = np.zeros((n_genes, n_cells))
    
    for i in range(n_modules):
        # Base expression for this module
        module_expression = np.random.randn(n_cells) * 2 + 5
        
        start_idx = i * genes_per_module
        end_idx = start_idx + genes_per_module if i < n_modules - 1 else n_genes
        
        for j in range(start_idx, end_idx):
            # Add gene-specific variation
            expression_data[j, :] = module_expression + np.random.randn(n_cells) * 0.5
    
    # Add noise
    expression_data += np.random.randn(n_genes, n_cells) * 0.2
    
    # Convert to counts (Poisson-like)
    expression_data = np.exp(expression_data)
    expression_data = np.random.poisson(expression_data)
    
    # Create DataFrame
    gene_names = [f"Gene_{i:03d}" for i in range(n_genes)]
    cell_names = [f"Cell_{i:03d}" for i in range(n_cells)]
    
    return pd.DataFrame(expression_data, index=gene_names, columns=cell_names)


def main():
    """
    Main demonstration function.
    """
    print("=" * 60)
    print("Gene Regulatory Network Analysis Demo")
    print("=" * 60)
    print()
    
    # Generate synthetic data
    print("Step 1: Generating synthetic expression data...")
    expr_data = generate_synthetic_data(n_genes=100, n_cells=500)
    print(f"Generated data with shape: {expr_data.shape}")
    print()
    
    # Initialize analyzer
    print("Step 2: Initializing GRN analyzer...")
    analyzer = GRNAnalyzer(expr_data)
    print()
    
    # Preprocess data
    print("Step 3: Preprocessing data...")
    analyzer.preprocess_data(min_cells=10, log_transform=True)
    print()
    
    # Compute correlations
    print("Step 4: Computing gene-gene correlations...")
    analyzer.compute_correlations(method='pearson')
    print()
    
    # Build network
    print("Step 5: Building gene regulatory network...")
    network = analyzer.build_network(threshold=0.6, min_targets=3)
    print()
    
    # Network statistics
    print("Step 6: Computing network statistics...")
    stats = analyzer.network_statistics()
    print("Network Statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value:.4f}")
    print()
    
    # Identify hub genes
    print("Step 7: Identifying hub genes...")
    hubs = analyzer.identify_hub_genes(top_n=10)
    print("Top 10 Hub Genes:")
    print(hubs.to_string(index=False))
    print()
    
    # Identify TF targets (using first few genes as example TFs)
    print("Step 8: Identifying transcription factor targets...")
    example_tfs = list(expr_data.index[:5])
    tf_targets = analyzer.identify_tf_targets(example_tfs, threshold=0.5, top_n=5)
    
    print("Example TF-Target Relationships:")
    for tf, targets in tf_targets.items():
        print(f"\n  {tf}:")
        for target, corr in targets[:3]:
            print(f"    -> {target} (r={corr:.3f})")
    print()
    
    print("=" * 60)
    print("Analysis complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
