from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from app.services.device_service import get_dashboard_devices

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/")
async def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "version": "0.2.0",
            "devices": get_dashboard_devices()
        }
    )