# physicochemical_profiling-of-proteins

Physicochemical Profiling of Protein Sequences (Biopython)


📌 Overview
This repository contains a Python script that automates physicochemical analysis of protein sequences using Biopython.
The script is designed as part of a computational biology/bioinformatics technical assessment and supports batch analysis of multiple protein sequences provided in FASTA format.
The tool computes key physicochemical properties that are commonly used to assess protein stability, solubility, and biochemical behavior during recombinant expression.


✨ Features
Supports multiple protein sequences in a single FASTA file
Calculates:
Molecular Weight (MW)
Isoelectric Point (pI)
GRAVY (Grand Average of Hydropathicity)
Instability Index


Outputs:
Results to the terminal
Results to a CSV file for downstream analysis
Uses Biopython ProtParam, a widely accepted bioinformatics library


📂 Repository Structure


├── physicochemical_profiling.py   # Main analysis script

├── input_proteins.fasta           # Input FASTA file (example)

├── physicochemical_results.csv    # Output file (generated)

└── README.md


🧪 Input Format
The input file must be a plain-text FASTA file containing one or more protein sequences.

Example (input_proteins.fasta)


 File is given in the repository

⚠️ Important
File must be saved as plain text
Only valid amino-acid characters (A–Z)
No special characters such as $, *, or formatting metadata


🛠 Requirements
Python 3.9+
Biopython
Install dependencies
python3 -m pip install biopython


▶️ How to Run
Place your FASTA file in the same directory as the script
Update the FASTA filename in the script if required
Run:
python3 physicochemical_profiling.py


📊 Output
Terminal Output (example)
Results for NP_000577.2
Molecular Weight (Da): 17627.53
Isoelectric Point (pI): 7.67
GRAVY: -0.007
Instability Index: 47.71


🧠 Interpretation
GRAVY: More negative values indicate increased hydrophilicity
pI: Lower pI often correlates with improved solubility under physiological conditions
Instability Index: Values >40 suggest intrinsic instability; comparison across variants is informative
This script is particularly useful for comparing wild-type vs mutant proteins during rational protein design.


🚀 Applications
Protein engineering and mutation analysis

Recombinant protein expression planning

Solubility and stability screening

Bioinformatics training and assessments


📚 Libraries Used
Biopython – ProtParam module for protein property analysis


👤 Author
Developed as part of a computational biology / bioinformatics technical assessment.


📄 License
This project is provided for academic, educational, and evaluation purposes.

