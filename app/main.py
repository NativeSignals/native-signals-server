from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes import dashboard, modules

app = FastAPI(
    title="Native Signals Server",
    version="0.2.0"
)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

app.include_router(dashboard.router)
app.include_router(modules.router)