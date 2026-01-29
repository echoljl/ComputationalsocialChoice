import os
import numpy as np
from preflibtools.instances import OrdinalInstance
from collections import Counter
from borda_rule import borda_rule
import csv

def load_preflib_soi(full_path):
    instance = OrdinalInstance()
    instance.parse_file(full_path)
    raw_ballots = instance.full_profile()

    return [[c for tier in b for c in tier] for b in raw_ballots], instance.num_alternatives

def get_truncation_distribution(ballots):
    lengths = [len(b) for b in ballots]
    counts = Counter(lengths)
    total = len(ballots)
    dist = {length: count / total for length, count in counts.items()}
    return dist

output_file = "borda_results.csv"
base_dir = os.path.dirname(os.path.abspath(__file__))

# borda results
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["File Name", "Winner", "Ranking"])

    for i in range(1, 9):
        local_file = f"00002-0000000{i}.soi"
        relative_path = f"debian/{local_file}"
        full_path = os.path.join(base_dir, "debian", local_file)
        
        if os.path.exists(full_path):
            ballots, num_cands = load_preflib_soi(full_path)
            winners, scores = borda_rule(ballots)
            writer.writerow([relative_path, winners, scores])
            print(f"Processed: {relative_path}")
        else:
            print(f"File not found: {full_path}")
    
    for i in range(1, 4):
        local_file = f"00001-0000000{i}.soi"
        relative_path = f"irish/{local_file}"
        full_path = os.path.join(base_dir, "irish", local_file)
        
        if os.path.exists(full_path):
            ballots, num_cands = load_preflib_soi(full_path)
            winners, scores = borda_rule(ballots)
            writer.writerow([relative_path, winners, scores])
            print(f"Processed: {relative_path}")
        else:
            print(f"File not found: {full_path}")

print(f"\nDone! Results saved to {output_file}")