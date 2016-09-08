#!/usr/bin/env python

import sys
import os

sys.path.append(os.path.join(os.path.abspath('.'), 'venv/Lib/site-packages'))

import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
from credentials import TOKEN
from handlers.handlers import echo, error, help, start

dispatcher = None
bot = Bot(TOKEN)

def setup():
    '''GAE DISPATCHER SETUP'''

    global dispatcher
    # Note that update_queue is setted to None and
    # 0 workers are allowed on Google app Engine (If not-->Problems with multithreading)
    dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0)

    # ---Register handlers here---
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(MessageHandler([Filters.text], echo))
    dispatcher.add_error_handler(error)

    return dispatcher

def webhook(update):
    global dispatcher
    # Manually get updates and pass to dispatcher
    dispatcher.process_update(update)
