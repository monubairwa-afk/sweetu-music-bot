import os
from pyrogram import Client, filters

API_ID = 38520576
API_HASH = "fcd1232557078626b7911a2f71a1b0fa"
BOT_TOKEN = "8804962485:AAEsRjVnp0wOKPaGglkNB8SJiYugFJY0qmk"

app = Client(
    "music_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
def start_command(client, message):
    message.reply_text("Hello! Main aapka music bot hoon. Mera istemaal karne ke liye /play likhein.")

@app.on_message(filters.command("play"))
def play_command(client, message):
    message.reply_text("🎵 Ganana chal raha hai...")

print("Bot is starting successfully...")
app.run()
