"""
Copy paste this code, insert your token, and run this code
Windows: `python quickstart.py` 
MacOS: `python3 quickstart.py`

This telegram bot replies you with whatever you send it
    eg. if you send "hello" to it, it will reply with "hello"
"""

from telegram.ext import *

TOKEN="INSERT TELEGRAM BOT TOKEN HERE"

def route(update, context):
    # text represents whatever you send it
    text = update.message.text

    # control what your telegram bot does in this function

    # telegram bot replies 
    update.message.reply_text(text)

updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.text, route))
updater.start_polling()

print("Your telegram bot is running!")

updater.idle()