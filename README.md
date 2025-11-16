# urban-wastewater-ARG-analysis
Metagenomic ARG analysis — BIOL 5340 final project
# Antibiotic Resistance Gene Flow in Urban Wastewater

This project analyzes ARG (antibiotic resistance gene) abundance and diversity across hospital wastewater, municipal sewage, and river samples using metagenomic FASTQ files from NCBI SRA.

## Repo structure
data/               # accession list + small reference or links
scripts/            # shell and Python scripts
notebooks/          # Colab notebook (added later)
results/            # outputs (not uploaded to GitHub)
README.md
ai_usage.md
requirements.txt
.gitignore

## How to run (summary)
1. Fill `data/sample_accessions.txt` with SRA IDs (one per line).  
2. Use SRA Toolkit locally or in Colab to download FASTQ files (do NOT upload FASTQ to GitHub).  
3. Run scripts in `scripts/` to perform BLAST and generate counts and plots.

## Notes
- All code and notebooks should be reproducible and documented.  
- Do not upload raw FASTQ files to GitHub — only accession IDs and processed outputs.  

GitHub repo for class submission: https://github.com/hlopez1024/urban-wastewater-ARG-analysis
