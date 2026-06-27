from fastapi import FastAPI

app = FastAPI(
    title="Native Signals Server",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "name": "Native Signals Server",
        "short": "NSS",
        "version": "0.1.0",
        "status": "running"
    }