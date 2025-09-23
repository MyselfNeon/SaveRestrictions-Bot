#Bot.py
from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN, LOG_CHANNEL
import datetime
from datetime import timezone, timedelta  # ✅ Added for IST

# ✅ Indian Standard Time
IST = timezone(timedelta(hours=5, minutes=30))

# Store logged users (in-memory)
LOGGED_USERS = set()

class Bot(Client):

    def __init__(self):
        super().__init__(
            "Neon Login",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="Neon"),
            workers=50,
            sleep_threshold=10
        )

    async def start(self):
        await super().start()
        me = await self.get_me()

        # Bot Deploy/Restart log
        now = datetime.datetime.now(IST)  # ✅ Using IST
        text = (
            f"**🤖 __Bot Deployed / Restarted__ ♻️**\n"
            f"**- __@{me.username}__**\n\n"
            f"**- __Date:__** __{now.strftime('%d-%b-%Y')}__\n"
            f"**- __Time:__** __{now.strftime('%I:%M %p')}__\n"
            f"**- __@neonfiles__**"
        )
        try:
            await self.send_message(LOG_CHANNEL, text)
        except Exception as e:
            print(f"Log send failed: {e}")

        print(f"**__Bot Powered By @{me.username}__**")

    async def stop(self, *args):
        me = await self.get_me()
        try:
            await self.send_message(LOG_CHANNEL, f"❌ Bot @{me.username} Stopped")
        except Exception as e:
            print(f"Stop log failed: {e}")
        await super().stop()
        print("Bot Stopped Bye")

BotInstance = Bot()

# Handler for new users (only logs once per user)
@BotInstance.on_message(filters.private & filters.incoming, group=-1)
async def new_user_log(bot: Client, message: Message):
    user = message.from_user
    if user is None:
        return

    # Log only if user not already logged
    if user.id not in LOGGED_USERS:
        LOGGED_USERS.add(user.id)

        now = datetime.datetime.now(IST)  # ✅ Using IST
        text = (
            f"**#NewUser 👤**\n"
            f"- __@{bot.me.username}__\n\n"
            f"- **__User: {user.mention}__**\n"
            f"- **__User ID:__** `{user.id}`\n"
            f"- **__Date:__** __{now.strftime('%d-%b-%Y')}__\n"
            f"- **__Time:__** __{now.strftime('%I:%M %p')}__"
        )
        try:
            await bot.send_message(LOG_CHANNEL, text)
        except Exception as e:
            print(f"New user log failed: {e}")

BotInstance.run()
