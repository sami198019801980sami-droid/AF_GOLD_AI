import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")

SYMBOLS = ["XAUUSD", "USNDQ100", "US30"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 AF GOLD AI\n"
        "مرحباً بك!\n"
        "محلل الذهب والناسداك والداو جونز.\n\n"
        "الأوامر:\n"
        "/markets - عرض الأسواق\n"
        "/help - المساعدة"
    )

async def markets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "📊 AF GOLD AI - الأسواق\n\n"
    for symbol in SYMBOLS:
        message += f"🔹 {symbol}: جاهز للتحليل\n"
    await update.message.reply_text(message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "AF GOLD AI\n"
        "سيتم تطوير نظام تحليل وإشارات التداول."
    )

def main():
    if not TOKEN:
        raise ValueError("TELEGRAM_TOKEN is missing")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("markets", markets))
    app.add_handler(CommandHandler("help", help_command))
    app.run_polling()

if name == "main":
    main()
