from dotenv import load_dotenv
from os import environ

load_dotenv()


SECRET = environ.get("SECRET")
ALGORITHM = environ.get("ALGORITHM")

BOT_API = environ.get("BOT_API")


WEBHOOK = "https://api.telegram.org/bot{token}/setWebhook?url={host}/user/webhook{token}"

TELEGRAM_GETME = "https://api.telegram.org/bot{token}/getMe"