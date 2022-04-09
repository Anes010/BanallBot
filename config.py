import os
from pyrogram import Client

api_id = int(os.environ.get("API_ID", 12345))
api_hash = os.environ.get('API_HASH')
token = os.environ.get('BOT_TOKEN')

bot=Client(
           ":memory:",
           api_id,
           api_hash,
           bot_token
)
