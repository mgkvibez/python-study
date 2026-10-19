def flatten(nested):
    """Flatten a list one level deep."""
    return [item for sublist in nested for item in sublist]
