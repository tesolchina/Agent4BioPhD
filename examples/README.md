# Examples Directory

This directory contains demonstrations of how AI agents can assist with various academic research tasks in biology. Each subdirectory focuses on a specific category of tasks.

## Directory Structure

### 📝 brainstorming/
Examples of AI-assisted research question generation and hypothesis formulation.

**Contents:**
- `research_questions.md` - Demonstrates systematic generation of research questions across different categories (methodological, biological applications, computational challenges)

**Use Cases:**
- Initial project planning
- Grant proposal brainstorming
- Identifying research gaps
- Generating testable hypotheses

---

### 📚 literature/
Examples of automated literature analysis and method comparison.

**Contents:**
- `method_comparison.md` - Comprehensive comparison of GRN inference methods from the review article

**Use Cases:**
- Understanding pros/cons of different approaches
- Selecting appropriate methods for specific research questions
- Organizing knowledge from literature reviews
- Creating comparison tables and summaries

---

### 🔬 analysis/
Python scripts for data analysis and bioinformatics tasks.

**Contents:**
- `grn_analysis.py` - Complete Python implementation of GRN analysis pipeline including:
  - Data preprocessing and quality control
  - Correlation-based network inference
  - Network topology analysis
  - Hub gene identification
  - Export functions

**Use Cases:**
- Analyzing single-cell RNA-seq data
- Inferring gene regulatory networks
- Computing network statistics
- Identifying key regulatory genes

**Running the Example:**
```bash
python examples/analysis/grn_analysis.py
```

---

### ✍️ writing/
Examples of AI-assisted scientific writing for different paper sections.

**Contents:**
- `methods_section.md` - Complete methods section template for a GRN study with:
  - Data collection and preprocessing
  - Network inference procedures
  - Validation approaches
  - Statistical analysis
  - Multiple versions (condensed, standard, expanded)

**Use Cases:**
- Drafting methods sections
- Ensuring reproducibility
- Meeting journal requirements
- Maintaining consistent terminology

---

### 💻 code/
Programming task automation and tool development examples.

**Contents:**
- `data_visualization.py` - Visualization tools for GRN analysis including:
  - Correlation heatmaps
  - Degree distribution plots
  - TF-target network diagrams
  - Regulon activity visualizations
  - Network comparison plots

**Use Cases:**
- Creating publication-quality figures
- Exploratory data visualization
- Comparing different networks
- Presenting results

**Running the Example:**
```bash
python examples/code/data_visualization.py
```

---

## Getting Started

### Prerequisites

To run the Python examples, you'll need:

```bash
pip install numpy pandas matplotlib seaborn
```

### Running Examples

1. **Text-based examples** (brainstorming, literature, writing):
   - Simply open and read the markdown files
   - Use them as templates for your own work
   - Adapt the content to your specific research context

2. **Python scripts** (analysis, code):
   ```bash
   # Navigate to the repository root
   cd Agent4BioPhD
   
   # Run analysis example
   python examples/analysis/grn_analysis.py
   
   # Run visualization example
   python examples/code/data_visualization.py
   ```

## How AI Agents Help

These examples demonstrate how AI agents can:

1. **Speed up research**: Automate repetitive tasks and analysis pipelines
2. **Improve quality**: Generate comprehensive, well-structured content
3. **Enhance reproducibility**: Create detailed documentation and code
4. **Facilitate learning**: Provide examples and explanations of complex methods
5. **Support creativity**: Generate diverse ideas and approaches

## Customizing for Your Research

Each example can be adapted to your specific research project:

- **Brainstorming**: Replace the reference article with your own research topic
- **Literature**: Add methods or tools relevant to your field
- **Analysis**: Modify scripts to work with your data format
- **Writing**: Adjust templates to match your journal's requirements
- **Code**: Extend visualizations for your specific needs

## Integration with Research Workflow

These examples fit into a typical research workflow:

```
Literature Review → Brainstorming → Experimental Design → Data Collection
     ↓                  ↓                                        ↓
  [literature/]    [brainstorming/]                              ↓
                                                                  ↓
Data Analysis → Results Visualization → Manuscript Writing → Submission
     ↓                    ↓                      ↓
[analysis/]           [code/]              [writing/]
```

## Contributing

To add new examples:

1. Choose the appropriate subdirectory
2. Follow the existing format and style
3. Include clear documentation
4. Add example outputs or screenshots where applicable
5. Update this README

## Additional Resources

- [Reference article summary](../reference/article_summary.md)
- [Project documentation](../docs/)
- [Main README](../README.md)

## Questions or Issues?

If you have questions about using these examples or encounter any issues, please open an issue on the GitHub repository.
