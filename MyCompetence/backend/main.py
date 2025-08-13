from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from core.database import init_db
from modules.tg_bot.router import router as tg_bot_router
from modules.admin.router import router as admin_router
from core.container import setup_dependency_injection

app = FastAPI()
container = setup_dependency_injection()
container.wire(modules=["modules.admin.router", "modules.tg_bot.router", "modules.admin.dependencies"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tg_bot_router, prefix="/api")
app.include_router(admin_router, prefix="/admin")

#app.mount("/admin", StaticFiles(directory="static/admin", html=True), name="admin")

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.get("/health")
async def health_check():
    return {"status": "ok"}