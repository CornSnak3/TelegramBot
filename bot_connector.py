import os
import logging
from dotenv import load_dotenv
from pathlib import Path
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

class BotConnector:
    def __init__(self):
        dotenvPath = Path("conf/telegram.env")
        load_dotenv(dotenv_path=dotenvPath)
        self.token = os.getenv("API_TOKEN")
        self.chatId = os.getenv("CHAT_ID")
        self.listener()

    def listener(self):
        updater = Updater(self.token, use_context=True)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", self.start))
        dp.add_handler(MessageHandler(Filters.text & ~Filters.command, self.echo))
        updater.start_polling()
        updater.idle()

    def start(self, update: Update, context):
        user = update.effective_user
        update.message.reply_text(update.message.text)

    def echo(self, update: Update, context):
        update.message.reply_text(update.message.text)