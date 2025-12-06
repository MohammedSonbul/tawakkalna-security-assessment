import re

def validate_user_input(user_id):
    # Only digits allowed (prevents injection)
    pattern = r"^[0-9]{10}$"

    if re.match(pattern, user_id):
        return "valid"
    else:
        return "invalid"


# Simple test
print(validate_user_input("1234567890"))      # valid
print(validate_user_input("12; DROP TABLE"))  # invalid
