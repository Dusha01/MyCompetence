import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from dotenv import load_dotenv
from aiogram import Bot
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

token = os.getenv('TOKEN')
chatID = os.getenv('CHAT_ID')

if not token or not chatID: 
    raise ValueError('Error token or chatID')

bot = Bot(token=token)

class ContactForm(BaseModel):
    name: str
    phone: str
    email: str
    subject: str
    message: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/contact")
async def submit_contact_form(form_data: ContactForm):
    try:
        message = (
            "📬 *Новое сообщение с сайта*\n\n"
            f"👤 *Имя:* {form_data.name}\n"
            f"📞 *Телефон:* {form_data.phone}\n"
            f"📧 *Email:* {form_data.email}\n"
            f"📌 *Тема:* {form_data.subject}\n\n"
            f"📝 *Сообщение:*\n{form_data.message}"
        )

        await bot.send_message(
            chat_id=chatID,
            text=message,
            parse_mode="Markdown"
        )

        logger.info('message send')
        return {"status": "success", "message": "Форма успешно отправлена"}
    except Exception as e:
        logger.error(f"Ошибка при отправке формы: {str(e)}")
        raise HTTPException(status_code=500, detail="Ошибка при обработке формы")


@app.get("/health")
async def health_check():
    return {"status": "ok"}