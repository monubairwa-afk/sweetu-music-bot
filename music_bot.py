import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8804962485:AAEJwFxNF5v3qoghaDg5PXA03rcoeg4o-8Q"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Main aapka music bot hoon. /play likhein.")

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎵 Gaana chal raha hai...")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play))
    
    print("Bot is running successfully...")
    app.run_polling()
