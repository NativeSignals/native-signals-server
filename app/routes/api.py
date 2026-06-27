from app.services.system_service import get_system_status
from fastapi import APIRouter

router = APIRouter(prefix="/api")

@router.get("/system")

async def system_status():

    return get_system_status()

@router.get("/status")
async def get_status():
    return {
        "nss_host": "online",
        "web_server": "online",
        "xr18": "online",
        "boss_head_1": "offline",
        "boss_head_2": "online",
        "prompter": "offline",
        "recording": "standby",
        "desktop": "standby"
    }