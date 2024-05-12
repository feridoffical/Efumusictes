import os


class Config:

   API_ID = int(os.getenv("API_ID", "4248265"))
   API_HASH = os.getenv("API_HASH", "4558365783a6294bc2456c1f69483739")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "7072473208:AAH1PrJGdNg6eiJr87K9Tb07Mhj32dkYr-Y")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "JockieMusicbot")
   OWNER_NAME = os.environ.get("OWNER_NAME", "Feridmov") 
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "JockieMusicPlaylist")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1002103037611"))
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "Feridmov")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/c34c2d05ce742278154cf.jpg") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/c34c2d05ce742278154cf.jpg")    
