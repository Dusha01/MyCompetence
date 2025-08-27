from fastapi import APIRouter, HTTPException, Depends
from dependency_injector.wiring import inject, Provide

from modules.tg_bot.dto import ContactFormDTO, ContactResponseDTO 
from dependency_container import Container

router = APIRouter()

@router.post("/contact", response_model=ContactResponseDTO)
@inject
async def submit_contact_form(
    form_data: ContactFormDTO,
    telegram_service = Depends(Provide[Container.telegram_service])
):
    response = await telegram_service.send_contact_message(form_data)
    if response.status == "error":
        raise HTTPException(status_code=500, detail=response.message)
    return response