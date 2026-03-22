import re

def check_password_strength(password):
    # Initialize strength score and feedback list
    score = 0
    feedback = []

    # 1. Check Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Increase length to at least 8 characters.")

    # 2. Check for Uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # 3. Check for Lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # 4. Check for Numbers
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # 5. Check for Special Characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add special characters (e.g., @, #, $).")

    # Determine strength label
    if score <= 2:
        strength = "Weak 🔴"
    elif score <= 4:
        strength = "Medium 🟡"
    else:
        strength = "Strong 🟢"

    return strength, feedback

# --- User Interface ---
print("--- Password Strength Evaluator ---")
user_input = input("Enter a password to test: ")
rating, suggestions = check_password_strength(user_input)

print(f"\nStrength: {rating}")
if suggestions:
    print("Suggestions to improve:")
    for note in suggestions:
        print(f" - {note}")