import os

class Config(object):

    API_ID = int(os.environ.get("API_ID", 12345))

    API_HASH = str(os.environ.get("API_HASH", ""))

    BOT_TOKEN = str(os.environ.get("BOT_TOKEN", ""))
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 1117429940 ))

    START = str(os.environ.get("START_TEXT", "Hi Iam A FeedBack Bot [Made By](https://t.me/LEGEND_OF_TG)"))

    HELP = str(os.environ.get("HELP_TEXT", ""))

    DONATE = str(os.environ.get("DONATE_TEXT", "Send Your Feedbacks Here About Our L.M Channels"))

    DONATE_LINK = str(os.environ.get("DONATE_LINK", ""))

    UPDATE_CHANNEL = str(os.environ.get("UPDATE_CHANNEL", ""))

    SUPPORT_GROUP = str(os.environ.get("SUPPORT_GROUP", ""))

