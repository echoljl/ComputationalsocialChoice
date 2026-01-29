import os
from preflibtools.instances import OrdinalInstance

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

#example
ballots, num_cands = load_preflib_soi("debian/00002-00000001.soi")
print(f"Success! Loaded {len(ballots)} ballots.")