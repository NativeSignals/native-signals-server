def get_dashboard_devices():
    return [
        {
            "name": "XR18 Mixer",
            "status_id": "xr18",
            "status": "offline",
            "url": "/xr18",
            "description": "Mixer control and scene loading."
        },
        {
            "name": "Boss Head 1",
            "status_id": "boss_head_1",
            "status": "offline",
            "url": "/boss/head-1",
            "description": "Guitar head editor launcher."
        },
        {
            "name": "Boss Head 2",
            "status_id": "boss_head_2",
            "status": "offline",
            "url": "/boss/head-2",
            "description": "Second guitar head editor launcher."
        },
        {
            "name": "Prompter",
            "status_id": "prompter",
            "status": "offline",
            "url": "/prompter",
            "description": "Open lyrics editor and stage prompter."
        },
        {
            "name": "Recording",
            "status_id": "recording",
            "status": "standby",
            "url": "/recording",
            "description": "Start, stop and save live recordings."
        },
        {
            "name": "NSS Desktop",
            "status_id": "desktop",
            "status": "standby",
            "url": "/desktop",
            "description": "Open browser-based remote control for the NSS Host."
        }
    ]