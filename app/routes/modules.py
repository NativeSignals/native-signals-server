from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.services.system_service import get_system_status
from app.services.device_service import get_dashboard_devices

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


def module_page(request: Request, title: str, subtitle: str):
    return templates.TemplateResponse(
        request=request,
        name="module.html",
        context={
            "title": title,
            "subtitle": subtitle,
            "version": "0.2.0"
        }
    )


@router.get("/xr18")
async def xr18(request: Request):
    return module_page(request, "XR18 Mixer", "Mixer control and scene loading.")


@router.get("/boss/head-1")
async def boss_head_1(request: Request):
    return module_page(request, "Boss Head 1", "Boss Tone Studio launcher placeholder.")


@router.get("/boss/head-2")
async def boss_head_2(request: Request):
    return module_page(request, "Boss Head 2", "Second Boss Tone Studio launcher placeholder.")


@router.get("/prompter")
async def prompter(request: Request):
    return module_page(request, "Prompter", "Lyrics editor and stage prompter placeholder.")


@router.get("/recording")
async def recording(request: Request):
    return module_page(request, "Recording", "Live recording control placeholder.")


@router.get("/devices")
async def devices(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="system_status.html",
        context={
            "version": "0.2.0",
            "system": get_system_status(),
            "devices": get_dashboard_devices()
        }
    )


@router.get("/shutdown")
async def shutdown(request: Request):
    return module_page(request, "Shutdown System", "Protected shutdown placeholder.")

@router.get("/desktop")
async def desktop(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="desktop.html",
        context={
            "title": "NSS Desktop",
            "subtitle": "Browser-based remote control for the NSS Host.",
            "version": "0.2.0",
            "desktop_url": "http://192.168.0.238:6080"
        }
    )