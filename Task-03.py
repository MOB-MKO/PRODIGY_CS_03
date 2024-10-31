import re

def check_password_strength(password):
    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    number_criteria = re.search(r"[0-9]", password) is not None
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None
    
    # Calculate strength score
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    
    # Provide feedback based on score
    if strength_score == 5:
        strength = "Very Strong"
        feedback = "Your password is very strong!"
    elif strength_score == 4:
        strength = "Strong"
        feedback = "Your password is strong, but you can add more special characters or numbers to make it stronger."
    elif strength_score == 3:
        strength = "Moderate"
        feedback = "Your password is moderate. Consider adding uppercase letters, numbers, or special characters to make it stronger."
    elif strength_score == 2:
        strength = "Weak"
        feedback = "Your password is weak. It should be longer and contain a mix of uppercase letters, lowercase letters, numbers, and special characters."
    else:
        strength = "Very Weak"
        feedback = "Your password is very weak. Consider using a longer password with a mix of uppercase, lowercase, numbers, and special characters."

    # Display results
    print(f"Password Strength: {strength}")
    print("Feedback:", feedback)

# Get password input from the user
password = input("Enter your password: ")
check_password_strength(password)
