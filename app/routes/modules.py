from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

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
    return module_page(request, "System Status", "Device monitoring placeholder.")


@router.get("/shutdown")
async def shutdown(request: Request):
    return module_page(request, "Shutdown System", "Protected shutdown placeholder.")