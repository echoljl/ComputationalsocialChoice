import os
import random
import csv
from collections import Counter
from load_data import load_soi
from get_truncation_distribution import get_truncation_distribution
from ablation import perform_ablation



base_dir = os.path.dirname(os.path.abspath(__file__))
output_ablation_file = "ablated_ballots.csv"

with open(output_ablation_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["File Name", "Original Ballot", "Ablated Ballot"])

    datasets = {"debian": range(1, 9), "irish": range(1, 4)}

    for folder, indices in datasets.items():
        for i in indices:
            prefix = "00002" if folder == "debian" else "00001"
            local_file = f"{prefix}-0000000{i}.soi"
            full_path = os.path.join(base_dir, folder, local_file)
            
            if os.path.exists(full_path):
                ballots, num_cands = load_soi(full_path)
                
                # get truncated ballots
                dist = get_truncation_distribution(ballots)
                
                # ablation
                truncated_list = perform_ablation(ballots, dist)
                
                # save results
                for original, ablated in zip(ballots, truncated_list):
                    writer.writerow([f"{folder}/{local_file}", original, ablated])
                
                print(f"Ablation complete for: {folder}/{local_file}")

print(f"\nDone! Ablated dataset saved to {output_ablation_file}")