def check_length(password):
    length = len(password)

    if length < 8:
        return f"Password is too short ({length} characters). Use at least 8"
    elif length < 12:
        return f"Password length is okay ({length} characters), but 12+ is wanted"
    else:
        return f"Good ({length} characters)"
    
def check_character_diversity(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any (c in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for c in password)

    diversity_score = sum([has_upper, has_lower, has_digit, has_special])

    feedback = []
    if not has_upper:
        feedback.append("Missing Uppercase letters (A-Z)")
    if not has_lower:
        feedback.append("Missing lowercase letters (a-z)")
    if not has_digit:
        feedback.append("Missing numbers (0-9)")
    if not has_special:
        feedback.append("Missing special characters (!@#$%)")

    if diversity_score == 4:
        return f"Excellent! All character types present ({diversity_score}/4)"
    elif diversity_score >= 3:
        return f"Good ({diversity_score}/4). Missing: {', '.join(feedback)}"
    else:
        return f"Bad ({diversity_score}/4). Missing: {', '.join(feedback)}"

def calculate_strength(password):
    score = 0

    length = len(password)
    if length >= 8:
        score += 20
    if length >= 12:
        score += 20
    if length >= 16:
        score += 10
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any (c in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for c in password)

    if has_upper:
        score += 15
    if has_lower:
        score += 15
    if has_digit:
        score += 10
    if has_special:
        score += 10

    if score >= 80:
        strength = "STRONG"
    elif score >= 60:
        strength = "MODERATE"
    elif score >= 40:
        strength = "WEAK"
    else:
        strength = "VERY WEAK"

    return score, strength
    


if __name__ == "__main__":
    test_password = "Mypassword123!45@$%@"
    print("=== PASSWORD ANALYZER ===")
    print(f"Testing: '{test_password}'")
    print()
    print(check_length(test_password))
    print(check_character_diversity(test_password))
    
    score, strength = calculate_strength(test_password)
    print(f"\nOverall Score: {score}/100")
    print(f"Strength: {strength}")