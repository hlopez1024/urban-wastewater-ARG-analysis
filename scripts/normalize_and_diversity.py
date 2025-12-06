import os
import pandas as pd
import numpy as np

IN_PATH = "results/counts/arg_counts_raw.csv"
OUT_DIR = "results/counts"

os.makedirs(OUT_DIR, exist_ok=True)

df = pd.read_csv(IN_PATH, index_col=0)

totals = df.sum(axis=0)

rpm = df.astype(float)
for col in df.columns:
    rpm[col] = df[col] / totals[col] * 1_000_000

rpm.to_csv(f"{OUT_DIR}/arg_counts_rpm.csv")

def shannon(col):
    values = col.values
    total = values.sum()
    if total == 0:
        return 0
    p = values / total
    p = p[p > 0]
    return -(p * np.log(p)).sum()

summary = pd.DataFrame({
    "total_RPM": rpm.sum(axis=0),
    "richness": (rpm > 0).sum(axis=0),
    "shannon": rpm.apply(shannon, axis=0)
})

summary.to_csv(f"{OUT_DIR}/arg_summary_metrics.csv")
print("DONE: summary metrics created")
