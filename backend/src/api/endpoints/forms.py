from fastapi import APIRouter, HTTPException, Depends
import logging

from src.models.schemas import ContactForm, ContactResponse
from src.services.telegram_service import TelegramService
from src.utils.validators import validate_contact_form

router = APIRouter(prefix="/api", tags=["contact"])

@router.post("/contact", response_model=ContactResponse)
async def contact_form(
    form: ContactForm,
    telegram_service: TelegramService = Depends()
):
    try:
        validate_contact_form(form)
        
        telegram_sent = await telegram_service.send_notification(form)
        
        if not telegram_sent:
            logging.warning("Telegram notification failed, but form data received")
        
        # Логирование успешного получения формы
        logging.info(f"Contact form received: {form.name}, {form.email}, {form.subject}")
        
        return ContactResponse(
            status="success",
            message="Form submitted successfully",
            telegram_sent=telegram_sent
        )
        
    except ValueError as e:
        logging.warning(f"Validation error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logging.error(f"Error processing contact form: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")