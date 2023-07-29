import re

def validate_credentials(username, password):
    # Validate username
    if not re.match(r'^[a-zA-Z0-9]{4,10}$', username):
        return False
    
    # Validate password
    if not re.match(r'^[a-zA-Z0-9@#$%^&+=]{8,16}$', password):
        return False
    
    return True

# Test the function
print(validate_credentials("user123", "password123"))  # True
print(validate_credentials("user_123", "password123"))  # False
print(validate_credentials("user123", "p@ssword"))     # False
