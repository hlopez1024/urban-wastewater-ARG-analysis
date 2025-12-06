#!/usr/bin/env python

import os
import pandas as pd

ACCESSION_FILE = "data/sample_accessions.txt"
BLAST_DIR = "results/blast"
COUNTS_DIR = "results/counts"

os.makedirs(COUNTS_DIR, exist_ok=True)

# read sample names
samples = []
with open(ACCESSION_FILE) as f:
    for line in f:
        if not line.strip():
            continue
        sample, acc = line.strip().split()
        samples.append(sample)

all_counts = []

for sample in samples:
    blast_file = os.path.join(BLAST_DIR, f"{sample}_vs_ARGdb.blast.tsv")
    if not os.path.exists(blast_file):
        print(f"Warning: missing BLAST file for {sample}, skipping")
        continue

    df = pd.read_csv(
        blast_file,
        sep="\t",
        header=None,
        names=["qseqid", "sseqid", "pident", "length", "evalue", "bitscore"],
    )

    counts = df["sseqid"].value_counts().rename(sample)
    all_counts.append(counts)

if not all_counts:
    raise SystemExit("No BLAST files found, cannot build counts table.")

counts_df = pd.concat(all_counts, axis=1).fillna(0).astype(int)
counts_df.to_csv(os.path.join(COUNTS_DIR, "arg_counts_raw.csv"))
print("Saved raw counts to results/counts/arg_counts_raw.csv")
