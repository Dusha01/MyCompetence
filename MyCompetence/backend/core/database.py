from motor.motor_asyncio import AsyncIOMotorClient

from core.config import Settings
from core.models import UserInDB
from core.security import get_password_hash

client = None
db = None

async def init_db():
    global client, db
    client = AsyncIOMotorClient(Settings.MONGO_URL)
    db = client[Settings.DB_NAME]

    existing_admin = await db.users.find_one({"username": Settings.ADMIN_USERNAME})
    if not existing_admin:
        admin_user = UserInDB(
            username=Settings.ADMIN_USERNAME,
            email="admin@example.com",
            hashed_password=get_password_hash(Settings.ADMIN_PASSWORD),
            disabled=False
        )
        await db.users.insert_one(admin_user.dict())

def get_db():
    return db