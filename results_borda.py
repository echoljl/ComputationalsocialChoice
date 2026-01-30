import os
import numpy as np
from collections import Counter
from borda_rule import borda_rule
import csv
from load_data import load_soi



output_file = "borda_results.csv"
base_dir = os.path.dirname(os.path.abspath(__file__))

with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["File Name", "Winner", "Ranking"])

    datasets = {"debian": range(1, 9), "irish": range(1, 4)}

    for folder, indices in datasets.items():
        for i in indices:
            prefix = "00002" if folder == "debian" else "00001"
            local_file = f"{prefix}-0000000{i}.soi"
            full_path = os.path.join(base_dir, folder, local_file)
            
            if os.path.exists(full_path):
                ballots, num_cands = load_soi(full_path)
                winners, scores = borda_rule(ballots)
                writer.writerow([f"{folder}/{local_file}", winners, scores])
                print(f"Processed: {f"{folder}/{local_file}"}")

print(f"\nDone! Results saved to {output_file}")