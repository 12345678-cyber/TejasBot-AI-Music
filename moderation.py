from pyrogram import Client, filters
from google.cloud import vision
import os
from config import GOOGLE_API_KEY, BOT_NAME

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_API_KEY
vision_client = vision.ImageAnnotatorClient()

COPYRIGHT_KEYWORDS = ["free movie", "download movie", "watch online", "cracked software"]
BAD_WORDS = ["sex", "porn", "nude", "xxx", "hentai"]

@app.on_message(filters.text)
async def detect_nsfw_text(client, message):
    text = message.text.lower()
    if any(word in text for word in COPYRIGHT_KEYWORDS + BAD_WORDS):
        await message.delete()
        await message.reply_text(f"🚫 **{BOT_NAME} Detected Inappropriate Content!**")
