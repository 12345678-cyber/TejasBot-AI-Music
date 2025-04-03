from pyrogram import Client, filters
from config import LOG_CHANNEL_ID, BOT_NAME

async def log_message(client, text):
    await client.send_message(LOG_CHANNEL_ID, f"📌 **{BOT_NAME} Log:**\n{text}")
