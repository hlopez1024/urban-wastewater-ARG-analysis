#!/usr/bin/env python

import os
import pandas as pd
import numpy as np

COUNTS_DIR = "results/counts"

raw_path = os.path.join(COUNTS_DIR, "arg_counts_raw.csv")
if not os.path.exists(raw_path):
    raise SystemExit("Missing results/counts/arg_counts_raw.csv. Run parse_blast_to_counts.py first.")

counts = pd.read_csv(raw_path, index_col=0)

# total reads per sample (approximate: sum of counts per sample)
totals = counts.sum(axis=0)

rpm = counts.astype(float)
for col in rpm.columns:
    if totals[col] > 0:
        rpm[col] = rpm[col] / totals[col] * 1_000_000
    else:
        rpm[col] = 0.0

rpm_path = os.path.join(COUNTS_DIR, "arg_counts_rpm.csv")
rpm.to_csv(rpm_path)
print("Saved RPM normalized counts to", rpm_path)

# richness: number of genes with RPM > 0
richness = (rpm > 0).sum(axis=0)

# Shannon diversity
def shannon(col):
    values = col.values
    total = values.sum()
    if total == 0:
        return 0.0
    p = values / total
    p = p[p > 0]
    return float(-(p * np.log(p)).sum())

shannon_index = rpm.apply(shannon, axis=0)

summary = pd.DataFrame({
    "total_RPM": rpm.sum(axis=0),
    "richness": richness,
    "shannon": shannon_index
})
summary_path = os.path.join(COUNTS_DIR, "arg_summary_metrics.csv")
summary.to_csv(summary_path)
print("Saved summary metrics to", summary_path)
