import secrets

from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes = ['bcrypt'],
    deprecated = "auto"
)
"""
Cryptocontext is a very useful class that allows us to work with different hash algorithms. New passwords will be hashed
using the new algorithm, but existing passwords will still be recognized
"""

def generate_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(palin_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def generate_token() -> str:
    return secrets.token_urlsafe(32)