from pydantic import BaseModel
from typing import Optional

class LoginUserRequest(BaseModel):
    username: str
    password: str
