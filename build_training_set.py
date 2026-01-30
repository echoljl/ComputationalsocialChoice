from prefix_features import extract_features

def build_training_set(full_ballots, target_pos, num_cands):
    X = []
    y = []
    
    for original_ballot in full_ballots:
        # is the original ballot long enough
        if len(original_ballot) > target_pos:
            # everything before the target position
            prefix = original_ballot[:target_pos]
            
            # candidate at the target position
            label = original_ballot[target_pos]
            
            X.append(extract_features(prefix, num_cands))
            y.append(label)
            
    return X, y

# Example: Predict who is in the 3rd spot
# X_train, y_train = build_training_set(ballots, target_pos=2, num_cands=num_cands)