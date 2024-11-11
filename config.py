import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "21188057"))
    API_HASH = os.environ.get("API_HASH", "8564fab8db759bb04b1907bd12ed98ef")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7986341240:AAHK_z4ks4a-FHojtVVHuhlCyctKz8QFA9Y")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "-6964538561")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://rahat:rahat@rahat.ncjti.mongodb.net/?retryWrites=true&w=majority&appName=Rahat")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Rahat")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1002442033969"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "@RM_Save_messeges_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
