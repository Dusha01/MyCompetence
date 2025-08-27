from datetime import timedelta
from fastapi import HTTPException, status
from dependency_injector.wiring import inject, Provide

from core.security import (
    verify_password,
    create_access_token,
    decode_token
)
from core.config import Settings
from core.models import UserInDB
from modules.admin.dto import UserDTO, TokenDTO, LoginFormDTO

class AdminService:
    @inject
    def __init__(self, db = Provide["db"]):
        self.db = db

    async def authenticate_user(self, username: str, password: str) -> UserInDB:
        user_dict = await self.db.users.find_one({"username": username})
        if not user_dict:
            return None
        user = UserInDB(**user_dict)
        if not verify_password(password, user.hashed_password):
            return None
        return user

    async def login_for_access_token(self, form_data: LoginFormDTO) -> TokenDTO:
        user = await self.authenticate_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=Settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        return TokenDTO(access_token=access_token, token_type="bearer")

    async def get_current_user(self, token: str) -> UserDTO:
        payload = decode_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        user_dict = await self.db.users.find_one({"username": username})

        if user_dict is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return UserDTO(**user_dict)