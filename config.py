import os
from pyrogram import Client

app_id = int(os.environ.get("API_ID", 12345))
app_key = os.environ.get('API_HASH')
token = os.environ.get('BOT_TOKEN')

bot=Client(
           ":memory:",
           api_id,
           api_hash,
           bot_token
)
