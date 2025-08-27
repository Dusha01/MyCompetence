from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from dependency_injector.wiring import inject, Provide

from modules.admin.dto import UserDTO
from dependency_container import Container

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/admin/token")

@inject
async def get_current_user(
    token: str = Depends(oauth2_scheme),
    admin_service = Depends(Provide[Container.admin_service])
) -> UserDTO:
    return await admin_service.get_current_user(token)

async def get_current_active_user(current_user: UserDTO = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user