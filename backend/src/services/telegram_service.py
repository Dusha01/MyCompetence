from aiogram import Bot
from aiogram.enums import ParseMode  # Добавляем правильный импорт
import logging

from settings import settings

class TelegramService:
    def __init__(self):
        self.bot = None
        self.chat_id = settings.telegram_chat_id
        
        if settings.telegram_bot_token:
            self.bot = Bot(token=settings.telegram_bot_token)
    
    async def send_notification(self, form_data) -> bool:
        if not self.bot or not self.chat_id:
            logging.warning("Telegram bot not configured")
            return False
        
        try:
            message_text = f"""
📧 *Новое сообщение с сайта*

*Имя:* {form_data.name}
*Телефон:* {form_data.phone}
*Email:* {form_data.email}
*Тема:* {form_data.subject}

*Сообщение:*
{form_data.message}
            """
            
            await self.bot.send_message(
                chat_id=self.chat_id,
                text=message_text,
                parse_mode=ParseMode.MARKDOWN  # Исправляем здесь
            )
            return True
        except Exception as e:
            logging.error(f"Error sending Telegram message: {e}")
            return False

telegram_service = TelegramService()