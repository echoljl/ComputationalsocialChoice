from collections import Counter

def get_truncation_distribution(ballots):
    lengths = [len(b) for b in ballots]
    counts = Counter(lengths)
    total = len(ballots)
    dist = {length: count / total for length, count in counts.items()}
    return dist