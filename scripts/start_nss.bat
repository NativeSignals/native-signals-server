@echo off
cd /d "C:\Native Signals Server"
"C:\Native Signals Server\.venv\Scripts\python.exe" -m uvicorn app.main:app --host 0.0.0.0 --port 8000 >> "C:\Native Signals Server\logs\nss-server.out.log" 2>> "C:\Native Signals Server\logs\nss-server.err.log"