from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from dependency_injector.wiring import inject, Provide

from modules.admin.dto import TokenDTO, UserDTO, LoginFormDTO
from modules.admin.dependencies import get_current_active_user
from dependency_container import Container

router = APIRouter()

@router.post("/token", response_model=TokenDTO)
@inject
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    admin_service = Depends(Provide[Container.admin_service])
):
    login_data = LoginFormDTO(
        username=form_data.username,
        password=form_data.password
    )
    return await admin_service.login_for_access_token(login_data)

@router.get("/me", response_model=UserDTO)
async def read_users_me(current_user: UserDTO = Depends(get_current_active_user)):
    return current_user

@router.get("/site-data", response_model=dict)
async def get_site_data(current_user: UserDTO = Depends(get_current_active_user)):
    return "1"
