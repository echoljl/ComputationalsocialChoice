from preflibtools.instances import OrdinalInstance

def load_soi(full_path):
    instance = OrdinalInstance()
    instance.parse_file(full_path)
    raw_ballots = instance.full_profile()

    return [[c for tier in b for c in tier] for b in raw_ballots], instance.num_alternatives