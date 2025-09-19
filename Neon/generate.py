import traceback
from pyrogram.types import Message
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from config import API_ID, API_HASH
from database.db import db

SESSION_STRING_SIZE = 351

@Client.on_message(filters.private & ~filters.forwarded & filters.command(["logout"]))
async def logout(client, message):
    user_data = await db.get_session(message.from_user.id)  
    if user_data is None:
        return 
    await db.set_session(message.from_user.id, session=None)  
    await message.reply("**__Logout Successfully__ 🚪**")

@Client.on_message(filters.private & ~filters.forwarded & filters.command(["login"]))
async def main(bot: Client, message: Message):
    user_data = await db.get_session(message.from_user.id)
    if user_data is not None:
        await message.reply("**__Your Are Already Logged In. First \n/logout Your Old Session. Then Do \n/login Again !!__ 🔑**")
        return 
    user_id = int(message.from_user.id)
    phone_number_msg = await bot.ask(chat_id=user_id, text="<b>__Please Send Your Phone Number Which Includes Country Code__</b>\n<b>__Example:__</b> <code>+91987654321</code>")
    if phone_number_msg.text=='/cancel':
        return await phone_number_msg.reply('<b>__Process Cancelled !!__</b>')
    phone_number = phone_number_msg.text
    client = Client(":memory:", API_ID, API_HASH)
    await client.connect()
    await phone_number_msg.reply("__Sending OTP...__")
    try:
        code = await client.send_code(phone_number)
        phone_code_msg = await bot.ask(user_id, "**__Please check for an OTP in Official Telegram Account. If you got it, Send OTP here after Reading the Below Format. \n\nIf OTP is__** `12345`, **__Please Send it as__** `1 2 3 4 5`.\n\n**__Enter /cancel to Cancel The Procces__**", filters=filters.text, timeout=600)
    except PhoneNumberInvalid:
        await phone_number_msg.reply('`PHONE_NUMBER` **is invalid.**')
        return
    if phone_code_msg.text=='/cancel':
        return await phone_code_msg.reply('<b>__Process Cancelled !!__</b>')
    try:
        phone_code = phone_code_msg.text.replace(" ", "")
        await client.sign_in(phone_number, code.phone_code_hash, phone_code)
    except PhoneCodeInvalid:
        await phone_code_msg.reply('**__OTP is Invalid.__**')
        return
    except PhoneCodeExpired:
        await phone_code_msg.reply('**__OTP is Expired.__**')
        return
    except SessionPasswordNeeded:
        two_step_msg = await bot.ask(user_id, '**__Your Account has Enabled Two-step Verification. Please Provide the Password.\n\nEnter /cancel to Cancel The Procces__**', filters=filters.text, timeout=300)
        if two_step_msg.text=='/cancel':
            return await two_step_msg.reply('<b>__Process Cancelled !!__</b>')
        try:
            password = two_step_msg.text
            await client.check_password(password=password)
        except PasswordHashInvalid:
            await two_step_msg.reply('**__Invalid Password Provided__**')
            return
    string_session = await client.export_session_string()
    await client.disconnect()
    if len(string_session) < SESSION_STRING_SIZE:
        return await message.reply('<b>__Invalid Session Sring__</b>')
    try:
        user_data = await db.get_session(message.from_user.id)
        if user_data is None:
            uclient = Client(":memory:", session_string=string_session, api_id=API_ID, api_hash=API_HASH)
            await uclient.connect()
            await db.set_session(message.from_user.id, session=string_session)
    except Exception as e:
        return await message.reply_text(f"<b>__ERROR IN LOGIN: `{e}`__</b>")
    await bot.send_message(message.from_user.id, "<b>__Account Login Successfully.\n\nIf You Get Any Error Related To AUTH KEY Then /logout first and /login again__</b>")

