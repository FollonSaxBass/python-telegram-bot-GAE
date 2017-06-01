#!/usr/bin/env python
from webapp2 import RequestHandler

import telegram
from telegram import bot
from message_handler import bot, setup, webhook
from credentials import TOKEN, APP_URL
import json



class WebHookHandler(RequestHandler):
    def set_webhook(self):
        '''
        Set webhook for your bot
        '''
        s = bot.setWebhook(APP_URL + '/' + TOKEN)
        if s:
            self.response.write("Webhook set")
        else:
            self.response.write("Webhook setup failed")

    def webhook_handler(self):
        # Retrieve the message in JSON and then transform it to Telegram object
        body = json.loads(self.request.body)
        update = telegram.Update.de_json(body)
        webhook(update)
