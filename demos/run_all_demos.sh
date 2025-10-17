#!/bin/bash
# -*- coding: utf-8 -*-

"""
Run All Demos

This script runs all demo scripts in the demos directory:
1. Warm-up paper analysis demo
2. LitStudy literature analysis demo
3. Motifmatchr motif matching demo

Usage:
  bash run_all_demos.sh
"""

# Set error handling
set -e

# Print script header
echo "====================================="
echo "Running All AI Agent4Bio Demos"
echo "====================================="
echo

# Get the absolute path to the script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "Working from demos directory: $SCRIPT_DIR"
echo

# Function to check if Python is installed
check_python() {
    if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
        echo "Error: Python is not installed or not in PATH"
        return 1
    fi
    return 0
}

# Function to check if Rscript is installed
check_r() {
    if ! command -v Rscript &> /dev/null; then
        echo "Error: Rscript is not installed or not in PATH"
        return 1
    fi
    return 0
}

# Run warm-up demo
echo "====================================="
echo "Running Warm-up Paper Analysis Demo"
echo "====================================="
echo

if check_python; then
    if [ -f "$SCRIPT_DIR/warmup_paper_analysis.py" ]; then
        python3 "$SCRIPT_DIR/warmup_paper_analysis.py" || python "$SCRIPT_DIR/warmup_paper_analysis.py"
        echo
        echo "Warm-up demo completed successfully."
        echo
    else
        echo "Warning: warmup_paper_analysis.py not found. Skipping..."
        echo
    fi
else
    echo "Skipping Python demos because Python is not available."
    echo
fi

# Run litstudy demo
echo "====================================="
echo "Running LitStudy Literature Analysis Demo"
echo "====================================="
echo

if check_python; then
    if [ -f "$SCRIPT_DIR/litstudy_demo.py" ]; then
        python3 "$SCRIPT_DIR/litstudy_demo.py" || python "$SCRIPT_DIR/litstudy_demo.py"
        echo
        echo "LitStudy demo completed successfully."
        echo
    else
        echo "Warning: litstudy_demo.py not found. Skipping..."
        echo
    fi
    
    # Run litstudy_badia_demo.py (new Badia-i-Mompel paper analysis)
    if [ -f "$SCRIPT_DIR/litstudy_badia_demo.py" ]; then
        echo "Running litstudy_badia_demo.py (Badia-i-Mompel paper analysis)"
        python3 "$SCRIPT_DIR/litstudy_badia_demo.py" || python "$SCRIPT_DIR/litstudy_badia_demo.py"
        echo
        echo "LitStudy Badia-i-Mompel demo completed successfully."
        echo
    else
        echo "Warning: litstudy_badia_demo.py not found. Skipping..."
        echo
    fi
fi

# Run motifmatchr demo
echo "====================================="
echo "Running Motifmatchr Motif Matching Demo"
echo "====================================="
echo

if check_r; then
    if [ -f "$SCRIPT_DIR/motifmatchr_demo.R" ]; then
        Rscript "$SCRIPT_DIR/motifmatchr_demo.R"
        echo
        echo "Motifmatchr demo completed successfully."
        echo
    else
        echo "Warning: motifmatchr_demo.R not found. Skipping..."
        echo
    fi
else
    echo "Skipping R demo because Rscript is not available."
    echo
fi

# Run original scripts
echo "====================================="
echo "Running Original Demo Scripts"
echo "====================================="
echo

# Navigate to scripts directory
SCRIPTS_DIR="$SCRIPT_DIR/../scripts"

if check_python; then
    if [ -f "$SCRIPTS_DIR/demo1_extract_methods.py" ]; then
        echo "Running demo1_extract_methods.py from scripts directory..."
        python3 "$SCRIPTS_DIR/demo1_extract_methods.py" || python "$SCRIPTS_DIR/demo1_extract_methods.py"
        echo
    else
        echo "Warning: demo1_extract_methods.py not found in scripts directory. Skipping..."
        echo
    fi
    
    if [ -f "$SCRIPTS_DIR/demo2_prepare_analysis.py" ]; then
        echo "Running demo2_prepare_analysis.py from scripts directory..."
        python3 "$SCRIPTS_DIR/demo2_prepare_analysis.py" || python "$SCRIPTS_DIR/demo2_prepare_analysis.py"
        echo
    else
        echo "Warning: demo2_prepare_analysis.py not found in scripts directory. Skipping..."
        echo
    fi
fi

if check_r; then
    if [ -f "$SCRIPTS_DIR/demo2_motif_analysis.R" ]; then
        echo "Running demo2_motif_analysis.R from scripts directory..."
        Rscript "$SCRIPTS_DIR/demo2_motif_analysis.R"
        echo
    else
        echo "Warning: demo2_motif_analysis.R not found in scripts directory. Skipping..."
        echo
    fi
fi

# Check outputs directory
echo "====================================="
echo "Checking Outputs"
echo "====================================="
echo

OUTPUTS_DIR="$SCRIPT_DIR/../outputs"
if [ -d "$OUTPUTS_DIR" ]; then
    echo "Output files have been generated in: $OUTPUTS_DIR"
    echo "Files available:"
    ls -la "$OUTPUTS_DIR"
    echo
else
    echo "Warning: Outputs directory not found. No output files were generated."
    echo
fi

echo "====================================="
echo "All demos completed."
echo "====================================="
echo "To learn more about each demo, see the README.md file in the demos directory."
echo "Thank you for using AI Agent4Bio!"
echo