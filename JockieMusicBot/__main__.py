# @JockieMusicbot
# Sahib @Feridoffical
# Repo Açığdısa İcazəsis Götürmə


from JockieMusicbot.config import Config
from JockieMusicbot.translation import Translation
from JockieMusicbot.Plugin import *
from JockieMusicbot.Music import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from JockieMusicbot import JockieMusicbot as app
from JockieMusicbot import LOGGER

MusicAzBotIMG = f"{Config.START_IMG}"



@app.on_message(filters.private & filters.incoming & filters.command(['start']))
async def start(client, message):
    await message.reply_photo(
        MusicAzBotIMG,
        caption=Translation.START_TEXT.format(message.from_user.mention, Config.BOT_USERNAME),
        reply_markup=Translation.START_BUTTONS
    )
    

app.start()
LOGGER.info(f"{Config.BOT_USERNAME} Uğurla Başladı Sahibim {Config.OWNER_NAME}")
idle()
