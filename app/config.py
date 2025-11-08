import os
from typing import Dict

def get_valid_users() -> Dict[str, str]:
    """get allowed users from env"""
    users = {}
    
    users_env = os.getenv("BASIC_AUTH_USERS")
    
    for user_pair in users_env.split(","):
        if ":" in user_pair:
            username, password = user_pair.split(":", 1)
            users[username.strip()] = password.strip()
    
    return users

VALID_USERS = get_valid_users()
