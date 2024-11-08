import re

def password_strength(password):
    # Initialize score and feedback
    score = 0
    feedback = []

    # Check length of the password
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should include at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Evaluate strength
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    else:
        strength = "Weak"

    # Print feedback
    print(f"Password Strength: {strength}")
    if feedback:
        print("Suggestions for improvement:")
        for suggestion in feedback:
            print(f"- {suggestion}")

# Example usage
password = input("Enter a password to test its strength: ")
password_strength(password)
