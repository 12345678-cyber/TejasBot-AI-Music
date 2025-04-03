from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN
from ai_chat import get_ai_response
from music_player import play_music, stop_music
from moderation import detect_nsfw_text, detect_nsfw_image
from logging_system import log_admin_actions, log_ai_chat, log_nsfw_content, log_music

app = Client("tejasbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("👋 Hello! I'm **Tejas - AI + Music + Moderation Bot!**")

@app.on_message(filters.text & ~filters.command)
async def chatgpt_reply(client, message):
    response = get_ai_response(message.text)
    await message.reply_text(f"🤖 **Tejas Says:** {response}")

@app.on_message(filters.command("play"))
async def play(client, message):
    await play_music(client, message)

@app.on_message(filters.command("stop"))
async def stop(client, message):
    await stop_music(client, message)

app.add_handler(detect_nsfw_text)
app.add_handler(detect_nsfw_image)
app.add_handler(log_admin_actions)
app.add_handler(log_ai_chat)
app.add_handler(log_nsfw_content)
app.add_handler(log_music)

app.run()
