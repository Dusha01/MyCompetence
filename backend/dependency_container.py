from dependency_injector import containers, providers

from core.database import get_db

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[
        "modules.admin.router",
        "modules.tg_bot.router",
        "modules.admin.dependencies"
    ])

    config = providers.Configuration()
    db = providers.Resource(get_db)

    admin_service = providers.Factory(
        "modules.admin.service.AdminService",
        db=db
    )
    
    telegram_service = providers.Factory(
        "modules.tg_bot.service.TelegramBotService",
        token=config.TOKEN,
        chat_id=config.CHAT_ID
    )
