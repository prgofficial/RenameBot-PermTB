import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    BANNED_USERS = []
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    TG_MAX_FILE_SIZE = 2097152000
    CHUNK_SIZE = 128
    DB_URI = os.environ.get("DATABASE_URL", "")
    CAPTION = os.environ.get("CAPTION", "")

