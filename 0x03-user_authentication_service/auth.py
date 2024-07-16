#!/usr/bin/env python3
"""hash user password
"""

import bcrypt
from typing import List, Tuple


def _hash_password(password: str) -> bytes:
    """Hashes a password.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
