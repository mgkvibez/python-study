def password_strength(password):
    """Rate the strength of a password."""
    if len(password) < 8:
        return "weak"
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    if has_upper and has_lower and has_digit:
        return "strong"
    if has_upper or has_digit:
        return "medium"
    return "weak"
