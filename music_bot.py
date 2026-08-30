import os
from pyrogram import Client, filters

# Render par set kiye gaye environment variables ya direct yahan daal sakte hain
API_ID = int(os.getenv("API_ID", "123456"))  # Apna Telegram API ID yahan dalein
API_HASH = os.getenv("API_HASH", "your_api_hash")  # Apna API Hash yahan dalein
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
    await message.reply_text("🎵 Ganana chal raha hai... (Voice chat support jald hi active hoga!)")

print("Bot is starting...")
app.run()
