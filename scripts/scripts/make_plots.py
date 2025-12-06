#!/usr/bin/env python

import os
import pandas as pd
import matplotlib.pyplot as plt

COUNTS_DIR = "results/counts"
FIG_DIR = "results/figures"

os.makedirs(FIG_DIR, exist_ok=True)

summary_path = os.path.join(COUNTS_DIR, "arg_summary_metrics.csv")
if not os.path.exists(summary_path):
    raise SystemExit("Missing arg_summary_metrics.csv. Run normalize_and_diversity.py first.")

summary = pd.read_csv(summary_path, index_col=0)

# Bar plot: total ARG RPM per sample
plt.figure()
summary["total_RPM"].plot(kind="bar")
plt.ylabel("Total ARG abundance (RPM)")
plt.xlabel("Sample")
plt.title("Total antibiotic resistance gene abundance per sample")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "fig_total_ARG_RPM_per_sample.png"))
plt.close()

# Bar plot: richness
plt.figure()
summary["richness"].plot(kind="bar")
plt.ylabel("Number of ARGs (richness)")
plt.xlabel("Sample")
plt.title("Antibiotic resistance gene richness per sample")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "fig_ARG_richness_per_sample.png"))
plt.close()

# Bar plot: Shannon diversity
plt.figure()
summary["shannon"].plot(kind="bar")
plt.ylabel("Shannon diversity index")
plt.xlabel("Sample")
plt.title("Antibiotic resistance gene diversity per sample")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "fig_ARG_shannon_per_sample.png"))
plt.close()

print("Saved plots in", FIG_DIR)
