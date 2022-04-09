class Config:
    TOKEN=os.environ['BOT_TOKEN']
    APP_HASH=os.environ['API_HASH']
    APP_ID=int(os.environ['API_ID'])

    if not TOKEN:
        raise ValueError(' BOT TOKEN not set')
    
    if not APP_HASH:
        raise ValueError("APP_HASH not set, set it first")

    if not APP_ID:
        raise ValueError("APP_ID not set, set it first")

    

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

bot=Client(
           ":memory:",
           api_id=Config.APP_ID,
           api_hash=Config.APP_HASH,
           bot_token=Config.TOKEN
)
