# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'AnganBot')
API_ID = int(environ.get('API_ID', '23483999'))
API_HASH = environ.get('API_HASH', 'f7177824ce1cde688f2f9520dfe6339e')
BOT_TOKEN = environ.get('BOT_TOKEN', "8022291716:AAHPC97MoqLUPX7XLC29f9W1R5QllxsfqLk")


# Start Message Pictures
PICS = (environ.get('PICS', 'https://graph.org/file/ce1723991756e48c35aa1.jpg')).split()

# Admins & Users
ADMINS = [7891845883]  
auth_users = []  
AUTH_USERS = (auth_users + ADMINS) if auth_users else ADMINS

# Log channel
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1003084161492'))

# File channels
CHANNELS = [-1002820902360]

# Force subscribe channel
REQUEST_TO_JOIN_MODE = True
TRY_AGAIN_BTN = True
AUTH_CHANNEL = -1002699575817

# Request channel
REQST_CHANNEL = None
INDEX_REQ_CHANNEL = LOG_CHANNEL

# Support group
SUPPORT_CHAT_ID = -1002486269632

# File Store & Delete Channels
FILE_STORE_CHANNEL = []
DELETE_CHANNELS = [0]


# MongoDB information
DATABASE_URI = "mongodb+srv://angan:angan@angan.zt9nvpm.mongodb.net/?retryWrites=true&w=majority&appName=Angan"
DATABASE_NAME = "angan"
COLLECTION_NAME = 'vjcollection'
MULTIPLE_DATABASE = False


# Premium & Referral (optional, enabled by default)
PREMIUM_AND_REFERAL_MODE = False
REFERAL_COUNT = 20
REFERAL_PREMEIUM_TIME = '1month'
PAYMENT_QR = 'https://graph.org/file/ce1723991756e48c35aa1.jpg'
PAYMENT_TEXT = '<b>- ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs - \n\n- 30ʀs - 1 ᴡᴇᴇᴋ\n- 50ʀs - 1 ᴍᴏɴᴛʜs\n- 120ʀs - 3 ᴍᴏɴᴛʜs\n- 220ʀs - 6 ᴍᴏɴᴛʜs\n\n🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs 🎁\n\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋ\n○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs\n○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ\n○ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ\n○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs\n○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs\n○ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ\n○ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1ʜ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ\n\n✨ ᴜᴘɪ ɪᴅ - <code>demo@okxyz</code>\n\nᴄʟɪᴄᴋ ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ /myplan\n\n💢 ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ\n\n‼️ ᴀғᴛᴇʀ sᴇɴᴅɪɴɢ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴜs sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ</b>'


# Clone Info
CLONE_MODE = False
CLONE_DATABASE_URI = ""
PUBLIC_FILE_CHANNEL = ""


# Links
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/angan_support')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/angan_channel')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'angan_support')
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/AnganOfficial')


# Features
AI_SPELL_CHECK = True
PM_SEARCH = True
BUTTON_MODE = True
MAX_BTN = True
IS_TUTORIAL = False
IMDB = False
AUTO_FFILTER = True
AUTO_DELETE = True
LONG_IMDB_DESCRIPTION = False
SPELL_CHECK_REPLY = True
MELCOW_NEW_USERS = True
PROTECT_CONTENT = False
PUBLIC_FILE_STORE = True
NO_RESULTS_MSG = False
USE_CAPTION_FILTER = True


# Token Verification Info
VERIFY = False


# Shortlink Info
SHORTLINK_MODE = False


# Others
CACHE_TIME = 1800
MAX_B_TN = "5"
PORT = "8080"
MSG_ALRT = 'Hello My Dear Friends ❤️'
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
MAX_LIST_ELM = None


# Options
LANGUAGES = ["malayalam","tamil","english","hindi","telugu","kannada"]
SEASONS = ["season 1","season 2","season 3","season 4","season 5"]
EPISODES = ["E01","E02","E03","E04","E05","E06","E07","E08","E09","E10"]
QUALITIES = ["360p","480p","720p","1080p"]
YEARS = ["2020","2021","2022","2023","2024","2025"]


# Online Stream & Download
STREAM_MODE = True
MULTI_CLIENT = False
SLEEP_THRESHOLD = 60
PING_INTERVAL = 1200
ON_HEROKU = False
URL = "https://angan-bot.herokuapp.com/"


# Rename Mode
RENAME_MODE = False

# Auto Approve Mode
AUTO_APPROVE_MODE = False

# Reactions
REACTIONS = ["🤝","😇","🤗","😍","👍","🎅","😐","🥰","🤩","😱","🤣","😘","👏","😛","😈","🎉","⚡️","🫡","🤓","😎","🏆","🔥","🤭","🌚","🆒","👻","😁"]

# DB Routing
if MULTIPLE_DATABASE == False:
    USER_DB_URI = DATABASE_URI
    OTHER_DB_URI = DATABASE_URI
    FILE_DB_URI = DATABASE_URI
    SEC_FILE_DB_URI = DATABASE_URI
else:
    USER_DB_URI = DATABASE_URI    
    OTHER_DB_URI = O_DB_URI       
    FILE_DB_URI = F_DB_URI        
    SEC_FILE_DB_URI = S_DB_URI
