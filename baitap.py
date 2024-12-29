import re

def validate_vn_phone_number(phone_number):
    """Validate a Vietnam phone number."""
    pattern = r"^(03|05|07|08|09|01[2|6|8|9])+([0-9]{8})$"
    if re.match(pattern, phone_number):
        return True
    return False

# Example usage
if __name__ == "__main__":
    phone_number = input("Enter a Vietnam phone number: ").strip()
    if validate_vn_phone_number(phone_number):
        print("Valid Vietnam phone number.")
    else:
        print("Invalid Vietnam phone number.")
