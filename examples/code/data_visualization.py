#!/usr/bin/env python3
"""
Data Visualization for Gene Regulatory Networks

This script demonstrates automated visualization generation for GRN analysis,
showing how AI agents can help create publication-quality figures.

Based on concepts from Badia-i-Mompel et al. (2023) Nature Reviews Genetics
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict, Tuple, Optional
import warnings

warnings.filterwarnings('ignore')


class GRNVisualizer:
    """
    A class for creating visualizations of gene regulatory networks.
    """
    
    def __init__(self, style: str = 'seaborn-v0_8-paper'):
        """
        Initialize the visualizer with plotting style.
        
        Args:
            style: Matplotlib style to use
        """
        try:
            plt.style.use(style)
        except:
            plt.style.use('default')
        
        sns.set_palette("husl")
        self.fig_count = 0
    
    def plot_correlation_heatmap(self,
                                 correlation_matrix: pd.DataFrame,
                                 top_n: int = 50,
                                 figsize: Tuple[int, int] = (10, 8),
                                 title: str = "Gene-Gene Correlation Heatmap",
                                 output_file: Optional[str] = None):
        """
        Create a heatmap of gene-gene correlations.
        
        Args:
            correlation_matrix: Correlation matrix DataFrame
            top_n: Number of top variable genes to display
            figsize: Figure size
            title: Plot title
            output_file: If provided, save figure to this file
        """
        # Select top variable genes
        if correlation_matrix.shape[0] > top_n:
            gene_vars = correlation_matrix.var(axis=1).sort_values(ascending=False)
            top_genes = gene_vars.head(top_n).index
            plot_data = correlation_matrix.loc[top_genes, top_genes]
        else:
            plot_data = correlation_matrix
        
        # Create heatmap
        fig, ax = plt.subplots(figsize=figsize)
        
        sns.heatmap(plot_data, 
                   cmap='RdBu_r',
                   center=0,
                   vmin=-1, vmax=1,
                   square=True,
                   linewidths=0,
                   cbar_kws={"shrink": 0.8, "label": "Correlation"},
                   ax=ax)
        
        ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
        ax.set_xlabel("Genes", fontsize=12)
        ax.set_ylabel("Genes", fontsize=12)
        
        plt.tight_layout()
        
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            print(f"Saved heatmap to {output_file}")
        
        plt.close()
        self.fig_count += 1
    
    def plot_degree_distribution(self,
                                degree_data: pd.Series,
                                figsize: Tuple[int, int] = (10, 6),
                                log_scale: bool = False,
                                title: str = "Network Degree Distribution",
                                output_file: Optional[str] = None):
        """
        Plot the degree distribution of the network.
        
        Args:
            degree_data: Series with node degrees
            figsize: Figure size
            log_scale: Whether to use log scale
            title: Plot title
            output_file: If provided, save figure to this file
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)
        
        # Histogram
        ax1.hist(degree_data, bins=30, edgecolor='black', alpha=0.7)
        ax1.set_xlabel("Degree", fontsize=12)
        ax1.set_ylabel("Frequency", fontsize=12)
        ax1.set_title("Degree Histogram", fontsize=12, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        
        if log_scale:
            ax1.set_yscale('log')
        
        # Cumulative distribution
        sorted_degrees = np.sort(degree_data)
        cumulative = np.arange(1, len(sorted_degrees) + 1) / len(sorted_degrees)
        
        ax2.plot(sorted_degrees, 1 - cumulative, 'o-', alpha=0.6)
        ax2.set_xlabel("Degree", fontsize=12)
        ax2.set_ylabel("P(Degree ≥ k)", fontsize=12)
        ax2.set_title("Cumulative Distribution", fontsize=12, fontweight='bold')
        ax2.grid(True, alpha=0.3)
        
        if log_scale:
            ax2.set_xscale('log')
            ax2.set_yscale('log')
        
        plt.suptitle(title, fontsize=14, fontweight='bold', y=1.02)
        plt.tight_layout()
        
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            print(f"Saved degree distribution to {output_file}")
        
        plt.close()
        self.fig_count += 1
    
    def plot_tf_target_network(self,
                               tf_targets: Dict[str, List[Tuple[str, float]]],
                               top_tfs: int = 5,
                               figsize: Tuple[int, int] = (12, 8),
                               title: str = "TF-Target Relationships",
                               output_file: Optional[str] = None):
        """
        Create a simplified network visualization of TF-target relationships.
        
        Args:
            tf_targets: Dictionary mapping TFs to list of (target, weight) tuples
            top_tfs: Number of TFs to display
            figsize: Figure size
            title: Plot title
            output_file: If provided, save figure to this file
        """
        # Select top TFs by number of targets
        tf_sizes = {tf: len(targets) for tf, targets in tf_targets.items()}
        top_tf_names = sorted(tf_sizes.keys(), key=lambda x: tf_sizes[x], reverse=True)[:top_tfs]
        
        fig, ax = plt.subplots(figsize=figsize)
        
        # Position TFs on the left
        tf_y_positions = np.linspace(0.2, 0.8, len(top_tf_names))
        tf_positions = {tf: (0.1, y) for tf, y in zip(top_tf_names, tf_y_positions)}
        
        # Position targets on the right (spread them out)
        all_targets = set()
        for tf in top_tf_names:
            for target, _ in tf_targets[tf][:10]:  # Top 10 targets per TF
                all_targets.add(target)
        
        target_y_positions = np.linspace(0.1, 0.9, len(all_targets))
        target_positions = {target: (0.9, y) for target, y in zip(sorted(all_targets), target_y_positions)}
        
        # Draw edges
        for tf in top_tf_names:
            tf_pos = tf_positions[tf]
            for target, weight in tf_targets[tf][:10]:
                if target in target_positions:
                    target_pos = target_positions[target]
                    
                    # Edge color based on correlation sign
                    color = 'red' if weight > 0 else 'blue'
                    alpha = min(abs(weight), 0.7)
                    
                    ax.plot([tf_pos[0], target_pos[0]], 
                           [tf_pos[1], target_pos[1]], 
                           color=color, alpha=alpha, linewidth=1, zorder=1)
        
        # Draw TF nodes
        for tf, pos in tf_positions.items():
            ax.scatter(pos[0], pos[1], s=500, c='orange', edgecolor='black', 
                      linewidth=2, zorder=2, alpha=0.8)
            ax.text(pos[0] - 0.05, pos[1], tf, ha='right', va='center', 
                   fontsize=10, fontweight='bold')
        
        # Draw target nodes (smaller)
        for target, pos in target_positions.items():
            ax.scatter(pos[0], pos[1], s=100, c='lightblue', edgecolor='gray', 
                      linewidth=1, zorder=2, alpha=0.6)
            ax.text(pos[0] + 0.05, pos[1], target, ha='left', va='center', 
                   fontsize=8)
        
        ax.set_xlim(-0.1, 1.1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
        
        # Add legend
        ax.scatter([], [], s=500, c='orange', edgecolor='black', label='Transcription Factors')
        ax.scatter([], [], s=100, c='lightblue', edgecolor='gray', label='Target Genes')
        ax.plot([], [], color='red', label='Positive Correlation')
        ax.plot([], [], color='blue', label='Negative Correlation')
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2, frameon=True)
        
        plt.tight_layout()
        
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            print(f"Saved TF-target network to {output_file}")
        
        plt.close()
        self.fig_count += 1
    
    def plot_regulon_activity(self,
                             activity_matrix: pd.DataFrame,
                             cell_types: Optional[List[str]] = None,
                             figsize: Tuple[int, int] = (12, 6),
                             title: str = "Regulon Activity Across Cell Types",
                             output_file: Optional[str] = None):
        """
        Plot regulon activity across different cell types or conditions.
        
        Args:
            activity_matrix: DataFrame with regulons as rows and cells as columns
            cell_types: List of cell type labels for cells
            figsize: Figure size
            title: Plot title
            output_file: If provided, save figure to this file
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize, 
                                       gridspec_kw={'width_ratios': [3, 1]})
        
        # Heatmap of activity
        sns.heatmap(activity_matrix, 
                   cmap='YlOrRd',
                   cbar_kws={"label": "Activity Score"},
                   ax=ax1,
                   xticklabels=False,
                   yticklabels=True)
        
        ax1.set_xlabel("Cells", fontsize=12)
        ax1.set_ylabel("Regulons", fontsize=12)
        ax1.set_title("Activity Heatmap", fontsize=12, fontweight='bold')
        
        # Box plot of activity distribution
        activity_data = activity_matrix.T.melt(var_name='Regulon', value_name='Activity')
        
        if cell_types is not None:
            activity_data['Cell Type'] = np.tile(cell_types, activity_matrix.shape[0])
            sns.boxplot(data=activity_data, y='Regulon', x='Activity', 
                       hue='Cell Type', ax=ax2, orient='h')
        else:
            sns.boxplot(data=activity_data, y='Regulon', x='Activity', 
                       ax=ax2, orient='h')
        
        ax2.set_xlabel("Activity Score", fontsize=12)
        ax2.set_ylabel("")
        ax2.set_title("Distribution", fontsize=12, fontweight='bold')
        
        plt.suptitle(title, fontsize=14, fontweight='bold', y=1.02)
        plt.tight_layout()
        
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            print(f"Saved regulon activity plot to {output_file}")
        
        plt.close()
        self.fig_count += 1
    
    def plot_network_comparison(self,
                               network1_edges: pd.DataFrame,
                               network2_edges: pd.DataFrame,
                               labels: Tuple[str, str] = ("Network 1", "Network 2"),
                               figsize: Tuple[int, int] = (12, 5),
                               title: str = "Network Comparison",
                               output_file: Optional[str] = None):
        """
        Compare two networks side by side.
        
        Args:
            network1_edges: EdgeList DataFrame for network 1
            network2_edges: EdgeList DataFrame for network 2
            labels: Labels for the two networks
            figsize: Figure size
            title: Plot title
            output_file: If provided, save figure to this file
        """
        fig, axes = plt.subplots(1, 3, figsize=figsize)
        
        # Get nodes and edges for each network
        nodes1 = set(network1_edges['source']) | set(network1_edges['target'])
        nodes2 = set(network2_edges['source']) | set(network2_edges['target'])
        
        edges1 = set(zip(network1_edges['source'], network1_edges['target']))
        edges2 = set(zip(network2_edges['source'], network2_edges['target']))
        
        # Compute overlaps
        nodes_common = nodes1 & nodes2
        nodes_only1 = nodes1 - nodes2
        nodes_only2 = nodes2 - nodes1
        
        edges_common = edges1 & edges2
        edges_only1 = edges1 - edges2
        edges_only2 = edges2 - edges1
        
        # Plot 1: Node comparison
        categories = ['Common', f'Only\n{labels[0]}', f'Only\n{labels[1]}']
        node_counts = [len(nodes_common), len(nodes_only1), len(nodes_only2)]
        
        axes[0].bar(categories, node_counts, color=['green', 'blue', 'red'], alpha=0.7)
        axes[0].set_ylabel("Number of Nodes", fontsize=11)
        axes[0].set_title("Node Comparison", fontsize=11, fontweight='bold')
        axes[0].grid(True, alpha=0.3, axis='y')
        
        # Add value labels
        for i, v in enumerate(node_counts):
            axes[0].text(i, v + max(node_counts) * 0.02, str(v), 
                        ha='center', va='bottom', fontweight='bold')
        
        # Plot 2: Edge comparison
        edge_counts = [len(edges_common), len(edges_only1), len(edges_only2)]
        
        axes[1].bar(categories, edge_counts, color=['green', 'blue', 'red'], alpha=0.7)
        axes[1].set_ylabel("Number of Edges", fontsize=11)
        axes[1].set_title("Edge Comparison", fontsize=11, fontweight='bold')
        axes[1].grid(True, alpha=0.3, axis='y')
        
        for i, v in enumerate(edge_counts):
            axes[1].text(i, v + max(edge_counts) * 0.02, str(v), 
                        ha='center', va='bottom', fontweight='bold')
        
        # Plot 3: Venn diagram style for edges
        from matplotlib.patches import Circle
        
        circle1 = Circle((0.35, 0.5), 0.25, color='blue', alpha=0.3, label=labels[0])
        circle2 = Circle((0.65, 0.5), 0.25, color='red', alpha=0.3, label=labels[1])
        
        axes[2].add_patch(circle1)
        axes[2].add_patch(circle2)
        
        # Add counts
        axes[2].text(0.25, 0.5, str(len(edges_only1)), ha='center', va='center', 
                    fontsize=12, fontweight='bold')
        axes[2].text(0.5, 0.5, str(len(edges_common)), ha='center', va='center', 
                    fontsize=12, fontweight='bold')
        axes[2].text(0.75, 0.5, str(len(edges_only2)), ha='center', va='center', 
                    fontsize=12, fontweight='bold')
        
        axes[2].set_xlim(0, 1)
        axes[2].set_ylim(0, 1)
        axes[2].axis('off')
        axes[2].set_title("Edge Overlap", fontsize=11, fontweight='bold')
        axes[2].legend(loc='upper center', bbox_to_anchor=(0.5, 0.05))
        
        plt.suptitle(title, fontsize=14, fontweight='bold', y=1.02)
        plt.tight_layout()
        
        if output_file:
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            print(f"Saved network comparison to {output_file}")
        
        plt.close()
        self.fig_count += 1


def demo_visualizations():
    """
    Demonstrate the visualization capabilities.
    """
    print("=" * 60)
    print("GRN Visualization Demo")
    print("=" * 60)
    print()
    
    # Generate synthetic data
    np.random.seed(42)
    n_genes = 30
    
    # Create correlation matrix
    print("Creating correlation heatmap...")
    gene_names = [f"Gene_{i}" for i in range(n_genes)]
    corr_matrix = pd.DataFrame(
        np.random.randn(n_genes, n_genes),
        index=gene_names,
        columns=gene_names
    )
    corr_matrix = (corr_matrix + corr_matrix.T) / 2  # Make symmetric
    np.fill_diagonal(corr_matrix.values, 1)
    corr_matrix = corr_matrix.clip(-1, 1)
    
    visualizer = GRNVisualizer()
    visualizer.plot_correlation_heatmap(corr_matrix, top_n=20)
    
    # Create degree distribution
    print("Creating degree distribution plot...")
    degrees = np.random.power(2, 100) * 50  # Power-law-like distribution
    degree_series = pd.Series(degrees)
    visualizer.plot_degree_distribution(degree_series)
    
    # Create TF-target network
    print("Creating TF-target network...")
    tf_targets = {
        'TF1': [(f'Target_{i}', np.random.uniform(-1, 1)) for i in range(15)],
        'TF2': [(f'Target_{i}', np.random.uniform(-1, 1)) for i in range(10, 25)],
        'TF3': [(f'Target_{i}', np.random.uniform(-1, 1)) for i in range(20, 35)],
    }
    visualizer.plot_tf_target_network(tf_targets, top_tfs=3)
    
    print()
    print(f"Created {visualizer.fig_count} visualizations")
    print("=" * 60)


if __name__ == "__main__":
    demo_visualizations()
