import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}$'
    return re.match(pattern, email) is not None

print(is_valid_email("test@example.com"))  # True
print(is_valid_email("bad-email.com"))     # False