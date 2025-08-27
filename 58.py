import re

def is_valid_password(password):
    if (len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[@$!%*?&]", password)):
        return True
    return False

print(is_valid_password("Passw0rd@"))  # True