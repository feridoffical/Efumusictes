# @JockieMusicBot
# Sahib @Feridoffical
# Repo Açığdısa İcazəsis Götürmə


import os
from MusicAzBot.translation import Translation
from MusicAzBot.config import Config
from pyrogram import Client
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from MusicAzBot import JockieMusicBot as app

@app.on_callback_query()
async def cb_data(client, message):
    if message.data == "home":
        await message.message.edit_text(
            text=Translation.START_TEXT.format(message.from_user.mention, Config.BOT_USERNAME),
            reply_markup=Translation.START_BUTTONS,
            disable_web_page_preview=True,
        )
    elif message.data == "help":
        await message.message.edit_text(
            text=Translation.HELP_TEXT.format(message.from_user.mention),
            reply_markup=Translation.HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "musıc":
        await message.message.edit_text(
            text=Translation.MUSIC_TEXT,
            reply_markup=Translation.MUSIC_BUTTONS,
            disable_web_page_preview=True
        )