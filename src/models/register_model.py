from pydantic import BaseModel, EmailStr
from typing import Optional

class RegisterUserRequest(BaseModel):
    email: EmailStr
    password: str
    nombre: str
    apellido: str
    username: str

class RegisterUserResponse(BaseModel):
    message: str
    user_id: str
