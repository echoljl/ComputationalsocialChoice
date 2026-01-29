import os
import numpy as np
from preflibtools.instances import OrdinalInstance
from collections import Counter
from borda_rule import borda_rule

def load_preflib_soi(file_path):
    base_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_path, file_path)
    
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Could not find file at: {full_path}")

    instance = OrdinalInstance()
    instance.parse_file(full_path)
    
    raw_ballots = instance.full_profile()
    clean_ballots = [[cand for tier in ballot for cand in tier] for ballot in raw_ballots]
    
    return clean_ballots, instance.num_alternatives

def get_truncation_distribution(ballots):
    lengths = [len(b) for b in ballots]
    counts = Counter(lengths)
    total = len(ballots)
    dist = {length: count / total for length, count in counts.items()}
    return dist

#example
ballots, num_cands = load_preflib_soi("debian/00002-00000001.soi")
print(f"Success! Loaded {len(ballots)} ballots.")

# calculate ballot length
dist = get_truncation_distribution(ballots)
print(f"Length distribution: {dist}")

# borda
winners, scores = borda_rule(ballots)
print(f"True Winner(s): {winners}")
print(f"Scores: {scores}")