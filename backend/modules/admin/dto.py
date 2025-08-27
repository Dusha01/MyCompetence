from pydantic import BaseModel
from typing import Optional

class UserDTO(BaseModel):
    username: str
    email: str
    disabled: Optional[bool] = None

class TokenDTO(BaseModel):
    access_token: str
    token_type: str

class LoginFormDTO(BaseModel):
    username: str
    password: str