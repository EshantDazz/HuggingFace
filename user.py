# schemas/user.py

from enum import Enum
from pydantic import BaseModel, EmailStr, constr


class UserRoleEnum(str, Enum):
    SYSTEM_ADMIN = "SYSTEM_ADMIN"
    TSM = "TSM"


class UserCreate(BaseModel):
    user_name: constr(min_length=3, max_length=50)
    user_email: EmailStr
    user_role: UserRoleEnum

    class Config:
        use_enum_values = True
