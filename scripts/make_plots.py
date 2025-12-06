import os
import pandas as pd
import matplotlib.pyplot as plt

# Paths
SUMMARY_PATH = "results/counts/arg_summary_metrics.csv"
FIG_DIR = "results/figures"

# Make sure the figures folder exists
os.makedirs(FIG_DIR, exist_ok=True)

# Check that the summary file exists
if not os.path.exists(SUMMARY_PATH):
    raise SystemExit("Summary file not found. Run normalize_and_diversity.py first.")

# Load summary metrics: total_RPM, richness, shannon
summary = pd.read_csv(SUMMARY_PATH, index_col=0)

# 1) Plot total ARG abundance (RPM) per sample
plt.figure()
summary["total_RPM"].plot(kind="bar")
plt.ylabel("Total ARG abundance (RPM)")
plt.xlabel("Sample")
plt.title("Total antibiotic resistance gene abundance per sample")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "total_ARG_RPM_per_sample.png"))
plt.close()

# 2) Plot richness per sample
plt.figure()
summary["richness"].plot(kind="bar")
plt.ylabel("Number of ARGs (richness)")
plt.xlabel("Sample")
plt.title("Antibiotic resistance gene richness per sample")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "ARG_richness_per_sample.png"))
plt.close()

# 3) Plot Shannon diversity per sample
plt.figure()
summary["shannon"].plot(kind="bar")
plt.ylabel("Shannon diversity index")
plt.xlabel("Sample")
plt.title("Antibiotic resistance gene diversity per sample")
plt.tight_layout()
plt.savefig(os.path.join(FIG_DIR, "ARG_shannon_per_sample.png"))
plt.close()

print("Plots saved in results/figures/")
