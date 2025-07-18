def is_valid(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()_+"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        return True
    else:
        return False

# Test
print(is_valid("Password@123"))  # ✅ True
print(is_valid("pass12"))        # ❌ False
