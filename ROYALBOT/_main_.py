import requests
from pyrogram import Client as Bot

from ROYALBOT.config import API_HASH
from ROYALBOT.config import API_ID
from ROYALBOT.config import BG_IMAGE
from ROYALBOT.config import BOT_TOKEN
from ROYALBOT.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="ROYALBOT.modules"),
)

bot.start()
run()
