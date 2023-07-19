import re


def checking_validation_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not re.search(r'[+\-/*!"№;%:?()=]', password):
        return False
    if any(char.isspace() or not char.isascii() for char in password):
        return False
    return True
