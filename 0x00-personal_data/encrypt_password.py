#!/usr/bin/env python3
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using a random salt"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def is_valid(hashed_password: bytes, password:str) -> bool:
    """Validates the hashed password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)