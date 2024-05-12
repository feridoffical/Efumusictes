# @JockieMusicbot
# Sahib @Feridoffical
# Repo Açığdısa İcazəsis Götürmə


import logging
from pyrogram import Client
from @ockieMusicbot.config import Config

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)

JockieMusicbot = Client(
    'JockieMusicbot',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)
