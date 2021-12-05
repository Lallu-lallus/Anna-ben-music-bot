
import os
import re


class Config:
    ADMIN = os.environ.get("ADMINS", "1316963576")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", 12345))
    CHAT = int(os.environ.get("CHAT", ""))
    LOG_GROUP = os.environ.get("LOG_GROUP", "")
    if LOG_GROUP:
        LOG_GROUP = int(LOG_GROUP)
    else:
        LOG_GROUP = None
    STREAM_URL = os.environ.get("STREAM_URL", "https://radioindia.net/radio/hungamanow/icecast.audio")
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    SESSION = os.environ.get("SESSION_STRING", "")
    SUDO_USERS = os.environ.get("SUDO_USERS", "")

