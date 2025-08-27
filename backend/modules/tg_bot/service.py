import logging
from aiogram import Bot
from dependency_injector.wiring import inject, Provide

from modules.tg_bot.dto import ContactFormDTO, ContactResponseDTO

logger = logging.getLogger(__name__)

class TelegramBotService:
    @inject
    def __init__(
        self, 
        token: str = Provide["config.TOKEN"],
        chat_id: str = Provide["config.CHAT_ID"]
    ):
        if not token or not chat_id:
            raise ValueError('Error token or chatID')
        self.bot = Bot(token=token)
        self.chat_id = chat_id

    async def send_contact_message(self, form_data: ContactFormDTO) -> ContactResponseDTO:
        try:
            message = (
                "📬 *Новое сообщение с сайта*\n\n"
                f"👤 *Имя:* {form_data.name}\n"
                f"📞 *Телефон:* {form_data.phone}\n"
                f"📧 *Email:* {form_data.email}\n"
                f"📌 *Тема:* {form_data.subject}\n\n"
                f"📝 *Сообщение:*\n{form_data.message}"
            )

            await self.bot.send_message(
                chat_id=self.chat_id,
                text=message,
                parse_mode="Markdown"
            )

            logger.info('Message sent successfully')
            return ContactResponseDTO(
                status="success",
                message="Форма успешно отправлена"
            )
        except Exception as e:
            logger.error(f"Ошибка при отправке формы: {str(e)}")
            return ContactResponseDTO(
                status="error",
                message="Ошибка при обработке формы"
            )