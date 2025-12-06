import os
import pandas as pd

ACCESSION_FILE = "data/sample_accessions.txt"
BLAST_DIR = "results/blast"
OUT_DIR = "results/counts"

os.makedirs(OUT_DIR, exist_ok=True)

samples = []
with open(ACCESSION_FILE) as f:
    for line in f:
        if not line.strip():
            continue
        sample, acc = line.split()
        samples.append(sample)

all_counts = []

for sample in samples:
    path = f"{BLAST_DIR}/{sample}_vs_ARGdb.blast.tsv"
    if not os.path.exists(path):
        continue

    df = pd.read_csv(path, sep="\t", header=None, names=[
        "qseqid","sseqid","pident","length","evalue","bitscore"
    ])
    counts = df["sseqid"].value_counts().rename(sample)
    all_counts.append(counts)

counts_df = pd.concat(all_counts, axis=1).fillna(0).astype(int)
counts_df.to_csv(f"{OUT_DIR}/arg_counts_raw.csv")
print("DONE: arg_counts_raw.csv created")
