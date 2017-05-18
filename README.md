# python-telegram-bot-GAE
Little project to upload and run a Telegram Bot on Google App Engine using the python-telegram-bot library and webhooks

*IMPORTANT*:
This project was created because there are only a few examples related to webhooks, python-telgram-bot and GAE all together and maybe none related to dispatcher and webhook working at one time.

### WHAT YOU NEED

- python-telegram-bot (library) Version: 5.0
- pip
- gcloud (https://cloud.google.com/sdk/)

You might need to enable billing on your Google App Engine project in order to get it to work.

### SETUP

1. Copy or move config.ini.example to config.ini. Inside, replace:
- &lt;TELEGRAM-BOT-TOKEN&gt; with the token BotFather gave you
- &lt;GAE-PROJECT-NAME&gt; with the same as above.

2. Make a new folder called "lib" in the project root.

3. Open a command line, navigate to your project root and type 'pip install -t lib -r requirements.txt' and wait until install is complete.

4. Type 'gcloud config set project &lt;GAE-PROJECT-NAME&gt;' in the terminal.

5. Now type 'gcloud app create' and choose your region.

6. Type 'gcloud app deploy'.

DONE! Open your browser and visit https://&lt;GAE-PROJECT-NAME&gt;.appspot.com/set_webhook. You should read "Webhook set" in the page.

You may now use your new bot! The default function is just echo. Feel free to customize it all you like.

### CREDITS
I used two examples found on GitHub to setup this project:

 1. https://github.com/sooyhwang/Simple-Echo-Telegram-Bot
 2. https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot2.py

I acheived the final result with the help of Jannes Höke, @jh0ker on GitHub


enjoy :)
