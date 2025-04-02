from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from uuid import UUID

class User(BaseModel):
    id: UUID
    instance_id: Optional[UUID] = None
    aud: Optional[str] = None
    role: Optional[str] = None
    email: Optional[EmailStr] = None
    email_confirmed_at: Optional[datetime] = None
    invited_at: Optional[datetime] = None
    last_sign_in_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    phone: Optional[str] = None
    phone_confirmed_at: Optional[datetime] = None
    is_super_admin: Optional[bool] = None
    is_sso_user: Optional[bool] = None
    is_anonymous: Optional[bool] = None
    deleted_at: Optional[datetime] = None

    class Config:
        orm_mode = True  # Permite convertir objetos ORM a Pydantic