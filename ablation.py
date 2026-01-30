import random

def perform_ablation(ballots, length_distribution):
    """
    For each full ballot, pick a target length 't' from the distribution 
    and truncate the ballot to that length.
    """
    truncated_data = []

    lengths = list(length_distribution.keys())
    weights = list(length_distribution.values())
    
    for ballot in ballots:
        t = random.choices(lengths, weights=weights, k=1)[0]
        truncated_ballot = ballot[:t]
        truncated_data.append(truncated_ballot)
        
    return truncated_data

# Example
# truncated_ballots = perform_ablation(ballots, dist)