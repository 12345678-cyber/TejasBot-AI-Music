import youtube_dl
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types import AudioPiped
from pyrogram import Client, filters
from pyrogram.types import Message
from config import BOT_NAME

call = PyTgCalls(Client("music_bot"))

def download_audio(url):
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}],
        "outtmpl": "song.mp3"
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return "song.mp3"

@Client.on_message(filters.command("play"))
async def play_music(client, message: Message):
    query = message.text.split(" ", 1)[1]
    await message.reply_text(f"🔍 **{BOT_NAME} Searching for:** {query}")

    ydl_opts = {"default_search": "ytsearch", "quiet": True}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)
        url = info["entries"][0]["url"]

    file_path = download_audio(url)
    chat_id = message.chat.id
    await call.join_group_call(chat_id, AudioPiped(file_path, StreamType().pulse_stream))

    await message.reply_text(f"🎵 **{BOT_NAME} Now Playing:** {query}")

@Client.on_message(filters.command("stop"))
async def stop_music(client, message: Message):
    chat_id = message.chat.id
    await call.leave_group_call(chat_id)
    await message.reply_text(f"⏹ **{BOT_NAME} Stopped Music!**")
