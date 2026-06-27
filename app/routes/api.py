from fastapi import APIRouter

from app.services.system_service import get_system_status
from app.services.launcher_service import launch_xr18

router = APIRouter(prefix="/api")


@router.get("/system")
async def api_system():
    return get_system_status()


@router.post("/launch/xr18")
async def api_launch_xr18():
    return launch_xr18()


@router.get("/status")
async def api_status():
    return {
        "nss_host": "online",
        "web_server": "online",
        "xr18": "offline",
        "boss_head_1": "offline",
        "boss_head_2": "offline",
        "prompter": "offline",
        "recording": "standby",
        "desktop": "standby",
    }