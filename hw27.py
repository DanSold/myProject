import hashlib

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_password_hash(password: str) -> str:
    result = pwd_context.hash(password)
    return result

txt = "Company123"

x = txt.isascii()

print(x)