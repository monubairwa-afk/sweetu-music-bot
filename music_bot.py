import os
import yt_dlp
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8804962485:AAEJwFxNF5v3qoghaDg5PXA03rcoeg4o-8Q"
​
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎵 Welcome! Kisi bhi gaane ko sunne ke liye aise likhein:\n`/play <gaane ka naam>`")

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ Bhai gaane ka naam toh likho! Jaise: `/play Kesariya`")
        return
    
    query = " ".join(context.args)
    msg = await update.message.reply_text(f"🔍 YouTube par `{query}` dhoondh raha hoon...")

    try:
        # yt-dlp options to download best audio
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': 'song.%(ext)s',
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=True)
            if 'entries' in info:
                info = info['entries'][0]
            filename = "song.mp3"

        await msg.edit_text("📤 Gaana download ho gaya, bhej raha hoon...")
        
        with open(filename, 'rb') as audio:
            await update.message.reply_audio(audio=audio, title=info.get('title', query))
        
        # Clean up local file after sending
        if os.path.exists(filename):
            os.remove(filename)

    except Exception as e:
        await msg.edit_text(f"⚠️ Gaana download karne mein error aaya: {str(e)}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play))
    
    print("Music Downloader Bot is running...")
    app.run_polling()
