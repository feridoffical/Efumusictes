# @JockieMusicBot
# Sahib @Feridoffical
# Repo Açığdısa İcazəsis Götürmə


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JockieMusicBot.config import Config

class Translation(object):

    START_TEXT = """
**Salam {} 👋**

**Mənim Adım  ️️️️️🇦🇿 {} Sizin Üçün Musiqi, Video Yükləmək Və Mahnı Sözlərini Tapmaq Üçün Hazırlanmış Telegram Botuyam Bacarıqlarımla Tanış Olmaq Üçün `🇦🇿 Əmrlər` Buttonuna Toxunun.**

"""    
    HELP_TEXT = """
**{} 🇦🇿 Əmrlərim Bunlardır  Buttonlara Toxunaraq İstədiyiniz Əmr Haqqında Məlumat Ala Bilərsiniz**

"""

    MUSIC_TEXT = """
🔮 Istifadə: /song 
🧩 Nümunə: /song Rei - Ah Canım Sevgilim
📃 Açıqlama: Musiqi yükləyir.

🔮 Istifadə: /video
🧩  Nümunə:/video Rei - Ah Canım Sevgilim
📃 Açıqlama: Video yükləyir.

🔮 Istifadə: /lyrics 
🧩 Nümunə: /lyrics Rei - Ah Canım Sevgilim
📃 Açıqlama: Musiqinin sözlərini tapır.

🔮 Istifadə: /search
🧩 Nümunə: /search Rei - Ah Canım Sevgilim
📃 Açıqlama: YouTube axtarış üçün istifadə edə bilərsiniz.
"""









    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('➕ Məni Qrupa Əlavə Et ➕', url=f"https://t.me/{Config.BOT_USERNAME}?startgroup=true")          
        ],[
        InlineKeyboardButton('🇦🇿 Əmrlər', callback_data='help'),
        ],[
        InlineKeyboardButton('Sahibim🧑‍💻',  url=f"https://t.me/{Config.OWNER_NAME}"),
        InlineKeyboardButton("🎵 Playlist", url=f"https://t.me/{Config.PLAYLIST_NAME}"),
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🎵 Musiqi', callback_data='musıc'), 
        ],[        
        InlineKeyboardButton('↪️ Geri Qayıt', callback_data='home'),
        ]]
    )
    
    
    MUSIC_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('↪️ Geri Qayıt', callback_data='help'),
        ]]
    )
