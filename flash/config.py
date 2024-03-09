from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "360"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/266058a34bf8966973b1a.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/266058a34bf8966973b1a.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Fv_av")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Fv_av")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5951674553").split()))


FAILED = "https://telegra.ph/file/266058a34bf8966973b1a.jpg"
