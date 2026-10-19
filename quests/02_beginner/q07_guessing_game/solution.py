def evaluate_guess(secret, guess):
    """Compare a guess to a secret number."""
    if guess == secret:
        return "correct"
    if guess < secret:
        return "too low"
    return "too high"
