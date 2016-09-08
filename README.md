# python-telegram-bot-GAE
Little project to upload and run Telegram Bot on Google App Engine using python-telegram-bot library and webhooks

*IMPORTANT*:
This project was created because there are only few examples related to WebHook, python-teelgram-bot and GAE all together and maybe none related to dispatcher and webhook working at one time.

WHAT DO YOU NEED:

- python-telegram-bot (library)
- pip

HOW TO SETUP THE PROJECT:

1. In app.yaml change "GAE-PROJECT-NAME" with your project name in GAE

2. In credentials.py:
TOKEN = 'YOUR-BOT-TOKEN'
APP_URL = 'YOUR-APP-URL'
    - set up your token taken from  botfather
    - set up your app url like:
    https://GAE-PROJECT-NAME.appspot.com

3. Make a folder called "lib" in the root of the project

4. Open cmd line or shell and type 'pip install -t lib -r requirements.txt' and wait until the process finishes

5. Go to /lib/future/backports/misc.py and comment line 900 -->"# from subprocess import check_output"

DONE! Upload your project open your browser and go to

- APP_URL/set_webhook, then try to send a message to your bot.

CREDITS:
I used two examples found on GitHub to setup this project:

 1. https://github.com/sooyhwang/Simple-Echo-Telegram-Bot
 2. https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot2.py

I acheived the final result with the help of Jannes Höke, @jh0ker on GitHub


enjoy :)
