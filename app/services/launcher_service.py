import subprocess
from pathlib import Path


XR18_PATH = Path(r"C:\Native Signals Server\tools\XR18\X-AIR-Edit.exe")


def launch_xr18():
    if not XR18_PATH.exists():
        return {
            "status": "error",
            "message": f"XR18 app not found: {XR18_PATH}"
        }

    subprocess.Popen(
        [str(XR18_PATH)],
        cwd=str(XR18_PATH.parent),
        shell=False
    )

    return {
        "status": "started",
        "app": "XR18 Mixer",
        "path": str(XR18_PATH)
    }