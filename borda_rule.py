def borda_rule(preferences):
    """
    Computes the Borda winner(s) from a set of preference rankings.
    
    :param preferences: List of rankings
    :return: List of winners (with possible ties)
    """
    if not preferences:
        return []

    # Number of candidates
    m = len(preferences[0])
    for i in preferences:
        if len(i) > m:
            m = len(i)
    scores = {}

    # Initialise candidate scores
    for i in preferences:
        for candidate in i:
            scores[candidate] = 0

    # Calculate scores
    for ballot in preferences:
        for index, candidate in enumerate(ballot):
            points = m - 1 - index
            scores[candidate] += points

    # Find winner(s)
    max_score = max(scores.values())
    winners = [cand for cand, score in scores.items() if score == max_score]
    
    return winners, scores

# To test if it works
prefs = [
    ['A', 'B', 'C'],
    ['B', 'C', 'A', 'D'],
    ['A', 'C', 'B']
]

winners, scores = borda_rule(prefs)
print(f"Scores: {scores}")
print(f"Winner(s): {winners}")