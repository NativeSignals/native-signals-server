from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="Native Signals Server",
    version="0.2.0"
)

templates = Jinja2Templates(directory="app/templates")

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)


def page(request: Request, title: str, subtitle: str):
    return templates.TemplateResponse(
        request=request,
        name="page.html",
        context={
            "title": title,
            "subtitle": subtitle,
            "version": app.version
        }
    )


@app.get("/")
async def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"version": app.version}
    )


@app.get("/xr18")
async def xr18(request: Request):
    return page(request, "XR18 Mixer", "Mixer control placeholder")


@app.get("/boss/head-1")
async def boss_head_1(request: Request):
    return page(request, "Boss Head 1", "Boss Tone Studio placeholder")


@app.get("/boss/head-2")
async def boss_head_2(request: Request):
    return page(request, "Boss Head 2", "Boss Tone Studio placeholder")


@app.get("/prompter")
async def prompter(request: Request):
    return page(request, "Prompter", "Prompter editor placeholder")


@app.get("/recording")
async def recording(request: Request):
    return page(request, "Recording", "Recording control placeholder")


@app.get("/devices")
async def devices(request: Request):
    return page(request, "System Status", "Device monitoring placeholder")


@app.get("/shutdown")
async def shutdown(request: Request):
    return page(request, "Shutdown System", "Protected shutdown placeholder")