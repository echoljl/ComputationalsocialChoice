def extract_features(prefix, num_cands):
    features = []
    for cand_id in range(1, num_cands + 1):
        if cand_id in prefix:
            features.append(1) # present
            features.append(prefix.index(cand_id)) # position
        else:
            features.append(0) # not present
            features.append(-1) # "unknown" position
    return features