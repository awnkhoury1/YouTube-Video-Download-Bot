import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7348374482:AAHc1Hocy5J38qATXkfh1HRDz1hvKZQW5JE")
    API_ID = int(os.environ.get("API_ID", "27129628"))
    API_HASH = os.environ.get("API_HASH", "8615528798f3185ffcb7f889925e5a5c")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "https://t.me/AkBots1st")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
