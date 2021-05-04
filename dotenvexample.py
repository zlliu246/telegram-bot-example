import os
from dotenv import load_dotenv

load_dotenv() 
TOKEN = os.getenv("TOKEN")

print("Your telegram bot token is:", TOKEN) 

from telegram.ext import *

def route(update, context):
    # text represents whatever you send it
    text = update.message.text

    # telegram bot replies 
    update.message.reply_text(text)

updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.text, route))
updater.start_polling()

print("Your telegram bot is running!")

updater.idle()


