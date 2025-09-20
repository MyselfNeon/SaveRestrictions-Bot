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
            f"**🤖 __Bot Deployed / Restarted__ ♻️**\n"
            f"**🌀 __{me.username} is Up__ ✅**\n\n"
            f"**📅 __Date:** {now.strftime('%d-%m-%Y')}__**\n"
            f"**⏰ __Time:** {now.strftime('%H:%M:%S')}__**"
        )
        try:
            await self.send_message(LOG_CHANNEL, text)
        except Exception as e:
            print(f"Log send failed: {e}")

        print(f**__Bot Powered By @{me.username}__**)

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
        f"**#NewUser**\n"
        f"- **__@{bot.me.username}__**\n\n"
        f"- **__User ID:__** `{user.id}`\n"
        f"- **__User: {user.mention}__**"
    )
    try:
        await bot.send_message(LOG_CHANNEL, text)
    except Exception as e:
        print(f"New user log failed: {e}")

BotInstance.run()
