# powerd by Beta
import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "TOXIC-MUSIC")
API_ID = int(getenv("API_ID", "25374274"))
API_HASH = getenv("API_HASH", "")
OWNER_ID = int(getenv("OWNER_ID", ""))
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")
LOG_ID = getenv("LOG_ID", "-1001518479327")
START_IMG = getenv("START_IMG")

OWNER_NAME = getenv("OWNER_NAME", "OFFLINE_HU_VMRO")
ALIVE_NAME = getenv("ALIVE_NAME", "TOXIC")
BOT_USERNAME = getenv("BOT_USERNAME", "")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://graph.org/file/db0705d103a75a09597be.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TOXIC-BOY-OP/DORAEMON-MUSICBOT")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://graph.org/file/db0705d103a75a09597be.jpg")
IMG_1 = getenv("IMG_1", "https://graph.org/file/db0705d103a75a09597be.jpg")
IMG_2 = getenv("IMG_2", "https://graph.org/file/db0705d103a75a09597be.jpg")
IMG_3 = getenv("IMG_3", "https://graph.org/file/db0705d103a75a09597be.jpg")
IMG_4 = getenv("IMG_4", "https://graph.org/file/db0705d103a75a09597be.jpg")
IMG_5 = getenv("IMG_5", "https://graph.org/file/db0705d103a75a09597be.jpg")
IMG_6 = getenv("IMG_6", "https://graph.org/file/db0705d103a75a09597be.jpg")
DB_URL = getenv("DB_URL", "mongodb+srv://hnyx:wywyw2@cluster0.9dxlslv.mongodb.net/?retryWrites=true&w=majority")
