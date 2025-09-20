from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN, LOG_CHANNEL
import datetime


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
        now = datetime.datetime.now()
        text = (
            f"🤖 **Bot Deploy/Restart**\n\n"
            f"- `{me.username}` is **Up ✅**\n\n"
            f"📅 **Date:** `{now.strftime('%d-%m-%Y')}`\n"
            f"⏰ **Time:** `{now.strftime('%H:%M:%S')}`"
        )
        try:
            await self.send_message(LOG_CHANNEL, text)
        except Exception as e:
            print(f"Log send failed: {e}")

        print(f'Bot Powered By @{me.username}')

    async def stop(self, *args):
        me = await self.get_me()
        try:
            await self.send_message(LOG_CHANNEL, f"❌ Bot @{me.username} Stopped")
        except Exception as e:
            print(f"Stop log failed: {e}")
        await super().stop()
        print('Bot Stopped Bye')


BotInstance = Bot()


# Handler for new users
@BotInstance.on_message(filters.private & filters.incoming)
async def new_user_log(bot: Client, message: Message):
    user = message.from_user
    if user is None:
        return

    # Prepare log
    text = (
        f"👤 **#NewUser**\n\n"
        f"- @{bot.me.username}\n\n"
        f"- **User ID:** `{user.id}`\n"
        f"- **User:** {user.mention}"
    )
    try:
        await bot.send_message(LOG_CHANNEL, text)
    except Exception as e:
        print(f"New user log failed: {e}")


BotInstance.run()
