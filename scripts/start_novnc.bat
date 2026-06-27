@echo off
cd /d "C:\Native Signals Server"
"C:\Native Signals Server\.venv\Scripts\python.exe" -m websockify --web "C:\Native Signals Server\tools\noVNC" 6080 127.0.0.1:5900 >> "C:\Native Signals Server\logs\novnc.out.log" 2>> "C:\Native Signals Server\logs\novnc.err.log"