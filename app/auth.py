from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
from .config import VALID_USERS

security = HTTPBasic()

def verify_credentials(credentials: HTTPBasicCredentials):
    correct_password = VALID_USERS.get(credentials.username)
    if not correct_password:
        return False
    return secrets.compare_digest(credentials.password, correct_password)

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    if not verify_credentials(credentials):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
