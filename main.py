import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("HTTP API:
8573872030:AAFTVQeD6sC7s0aF_GZ6eUB-5pRxKIvkv6Y")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("FlashSave Bot is online ⚡")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send any message. More features coming soon.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Received: " + update.message.text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_cmd))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()
