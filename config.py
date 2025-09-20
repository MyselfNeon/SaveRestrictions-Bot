import os

# Bot Token
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID & Hash
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "841851780"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "MyselfNeon")

# Log Channel to Track New Users 
LOG_CHANNEL = -1001889915480  # replace with your log channel id

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then False
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
