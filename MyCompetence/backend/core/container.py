from dependency_injector import containers, providers
from core.config import Settings

from dependency_container import Container

def setup_dependency_injection():
    container = Container()
    container.config.from_dict({
        "TOKEN": Settings.TOKEN,
        "CHAT_ID": Settings.CHAT_ID
    })
    return container