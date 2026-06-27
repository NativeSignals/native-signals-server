def get_dashboard_devices():
    return [
        {
            "name": "XR18 Mixer",
            "status": "online",
            "url": "/xr18",
            "description": "Mixer control and scene loading."
        },
        {
            "name": "Boss Head 1",
            "status": "offline",
            "url": "/boss/head-1",
            "description": "Guitar head editor launcher."
        },
        {
            "name": "Boss Head 2",
            "status": "offline",
            "url": "/boss/head-2",
            "description": "Second guitar head editor launcher."
        },
        {
            "name": "Prompter",
            "status": "offline",
            "url": "/prompter",
            "description": "Open lyrics editor and stage prompter."
        },
        {
            "name": "Recording",
            "status": "standby",
            "url": "/recording",
            "description": "Start, stop and save live recordings."
        },
        {
            "name": "System Status",
            "status": "online",
            "url": "/devices",
            "description": "Check NSS host and connected devices."
        }
    ]