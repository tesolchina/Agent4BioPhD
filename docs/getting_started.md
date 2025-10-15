# Getting Started with Agent4BioPhD

This guide will help you get started with using AI agents for biology research automation.

## Overview

Agent4BioPhD demonstrates how AI agents can assist with various tasks in biology research:
- **Text-based tasks**: Brainstorming, literature review, writing
- **Programming tasks**: Data analysis, visualization, tool development

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/tesolchina/Agent4BioPhD.git
cd Agent4BioPhD
```

### 2. Set Up Python Environment (Optional but Recommended)

Using a virtual environment helps keep dependencies isolated:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Quick Start Examples

### Example 1: Research Question Generation

Open and explore the brainstorming example:

```bash
# View the file
cat examples/brainstorming/research_questions.md

# Or open in your text editor
code examples/brainstorming/research_questions.md
```

**What you'll learn:**
- How to systematically generate research questions
- Organizing questions by category
- Formulating testable hypotheses
- Designing experiments

### Example 2: Method Comparison

Explore how to organize and compare different computational methods:

```bash
cat examples/literature/method_comparison.md
```

**What you'll learn:**
- Comparing different GRN inference methods
- Understanding strengths and limitations
- Selecting appropriate methods for your research
- Creating comparison tables

### Example 3: Data Analysis

Run the GRN analysis script:

```bash
python examples/analysis/grn_analysis.py
```

**Expected output:**
```
============================================================
Gene Regulatory Network Analysis Demo
============================================================

Step 1: Generating synthetic expression data...
Generated data with shape: (100, 500)

Step 2: Initializing GRN analyzer...

Step 3: Preprocessing data...
Filtered from 100 to 100 genes

...
```

**What you'll learn:**
- Loading and preprocessing gene expression data
- Computing correlations
- Building networks
- Analyzing network topology

### Example 4: Visualization

Run the visualization demo:

```bash
python examples/code/data_visualization.py
```

**What you'll learn:**
- Creating correlation heatmaps
- Plotting degree distributions
- Visualizing TF-target relationships
- Generating publication-quality figures

## Understanding the Project Structure

```
Agent4BioPhD/
├── examples/              # Demonstration examples
│   ├── brainstorming/    # Research ideation
│   ├── literature/       # Method comparison
│   ├── analysis/         # Data analysis scripts
│   ├── writing/          # Writing assistance
│   └── code/            # Programming automation
├── reference/           # Reference materials
├── docs/               # Documentation
├── requirements.txt    # Python dependencies
└── README.md          # Main documentation
```

## Common Workflows

### Workflow 1: Starting a New Research Project

1. **Literature Review** → Read `reference/article_summary.md`
2. **Brainstorming** → Use `examples/brainstorming/research_questions.md`
3. **Method Selection** → Consult `examples/literature/method_comparison.md`
4. **Analysis** → Adapt scripts from `examples/analysis/`
5. **Writing** → Use templates from `examples/writing/`

### Workflow 2: Analyzing Your Own Data

1. **Prepare your data** in the format expected by the scripts (genes × cells)
2. **Modify the analysis script** to load your data
3. **Run preprocessing** and quality control
4. **Perform network inference** using appropriate methods
5. **Visualize results** using the visualization tools
6. **Document your methods** using writing templates

### Workflow 3: Creating Figures for Publication

1. **Analyze your data** to generate results
2. **Use visualization tools** from `examples/code/data_visualization.py`
3. **Customize plots** (colors, labels, sizes) to match journal requirements
4. **Export high-resolution figures** (300+ DPI)
5. **Generate figure legends** using AI assistance

## Customizing for Your Research

### Modifying Python Scripts

All Python scripts are designed to be modular and easy to customize:

```python
# Example: Using the GRNAnalyzer with your own data
import pandas as pd
from examples.analysis.grn_analysis import GRNAnalyzer

# Load your data (genes as rows, cells as columns)
my_data = pd.read_csv("my_expression_data.csv", index_col=0)

# Initialize analyzer
analyzer = GRNAnalyzer(my_data)

# Run analysis
analyzer.preprocess_data()
analyzer.compute_correlations()
network = analyzer.build_network(threshold=0.7)

# Get results
stats = analyzer.network_statistics()
hubs = analyzer.identify_hub_genes()
```

### Adapting Text Templates

The markdown files can be used as templates:

1. **Copy the template** to your own document
2. **Replace placeholder text** with your specific content
3. **Adapt the structure** to your needs
4. **Keep the AI-friendly format** for easy updates

## Best Practices

### For Text-Based Tasks

- ✓ Start with the provided templates
- ✓ Maintain consistent terminology
- ✓ Include all necessary details for reproducibility
- ✓ Cite sources appropriately
- ✓ Review and refine AI-generated content

### For Programming Tasks

- ✓ Comment your code clearly
- ✓ Use meaningful variable names
- ✓ Test with small datasets first
- ✓ Validate results against known benchmarks
- ✓ Document parameters and their effects

### For Data Analysis

- ✓ Always perform quality control
- ✓ Document preprocessing steps
- ✓ Use appropriate statistical tests
- ✓ Validate findings with multiple methods
- ✓ Save intermediate results

## Troubleshooting

### Python Script Errors

**Problem**: `ModuleNotFoundError: No module named 'numpy'`

**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

---

**Problem**: Script runs but produces unexpected results

**Solution**: Check your input data format
- Ensure genes are in rows and cells in columns
- Verify data is numeric
- Check for missing values (NaN)

---

### Performance Issues

**Problem**: Script is too slow for large datasets

**Solution**: 
- Use data filtering to reduce size
- Increase computational resources
- Consider using specialized tools (scanpy, etc.)

---

### Visualization Issues

**Problem**: Plots don't display

**Solution**:
- Check if running in appropriate environment (not headless server)
- Save to file instead of displaying: use `output_file` parameter
- Ensure matplotlib backend is properly configured

## Next Steps

After getting started with the examples:

1. **Explore the reference material** to understand the scientific context
2. **Try modifying the examples** with your own parameters
3. **Apply to your own data** and research questions
4. **Contribute improvements** back to the repository
5. **Share your experiences** and use cases

## Getting Help

If you need assistance:

1. Check the documentation in the `docs/` directory
2. Review example code comments
3. Open an issue on GitHub
4. Consult the reference article for biological context

## Additional Resources

- [Examples README](../examples/README.md) - Detailed guide to all examples
- [Article Summary](../reference/article_summary.md) - Background on GRN inference
- [Main README](../README.md) - Project overview

## Contributing

We welcome contributions! To add new examples or improve existing ones:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

Focus on:
- Clear documentation
- Reproducible examples
- Practical use cases
- Educational value

---

**Happy researching with AI agents! 🧬🤖**
