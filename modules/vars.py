# SudoR2spr WOODcraft
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os

API_ID    = os.environ.get("API_ID", "23303247")
API_HASH  = os.environ.get("API_HASH", "23623f737dc15708708c65a7297e1510")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7410621236:AAFDEtY2LE6glSLwNX-kAmZyKeN1Ksh8bOc") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

