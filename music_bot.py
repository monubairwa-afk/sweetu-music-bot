import os
from pyrogram import Client, filters

API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8804962485:AAEsRjVnp0wOKPaGglkNB8SJiYugFJY0qmk")

app = Client(
    "music_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text("Hello! Main aapka music bot hoon. Mera istemaal karne ke liye /play likhein.")

@app.on_message(filters.command("play"))
async def play_command(client, message):
    await message.reply_text("🎵 Ganana chal raha hai...")

print("Bot started successfully!")
app.run()
