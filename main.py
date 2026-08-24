import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)

# جلب التوكين من المتغيرات الأمنية في Koyeb
TOKEN = os.getenv("8868088936:AAH56-pwHiRQ8f1u3jWRDhsd0PgX4dt7BXI")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك! البوت يعمل الآن على Koyeb مجاناً 24/7 🚀")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"كررت رسالتك: {update.message.text}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("البوت يعمل بنجاح...")
    app.run_polling()
