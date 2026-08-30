import os
import asyncio
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
async def start_command(client, message):
    await message.reply_text("Hello! Main aapka music bot hoon. Mera istemaal karne ke liye /play likhein.")

@app.on_message(filters.command("play"))
async def play_command(client, message):
    await message.reply_text("🎵 Ganana chal raha hai...")

async def main():
    await app.start()
    print("Bot started successfully!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
