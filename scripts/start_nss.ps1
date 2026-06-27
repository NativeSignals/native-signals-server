$NssRoot = "C:\Native Signals Server"
$Python = "$NssRoot\.venv\Scripts\python.exe"
$LogDir = "$NssRoot\logs"

New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

Start-Process `
    -FilePath $Python `
    -ArgumentList "-m uvicorn app.main:app --host 0.0.0.0 --port 8000" `
    -WorkingDirectory $NssRoot `
    -RedirectStandardOutput "$LogDir\nss-server.out.log" `
    -RedirectStandardError "$LogDir\nss-server.err.log" `
    -WindowStyle Hidden