# Project Configuration
# See https://pystark.codes/start/settings for details


# Path of the 'plugins' directory in relation to the root directory or List of multiple paths
# If name of your directory is 'files' and it is in the same folder as 'bot.py', pass plugin='files'.
# Defaults to 'plugins', i.e, a folder named 'plugins' in same directory as 'bot.py'
PLUGINS = "plugins" or ["plugins"]

# Set bot menu using command description if provided
SET_BOT_MENU = True

# Prefixes for commands. For multiple prefixes, specify multiple together like ["&", "*", "/", "."]
CMD_PREFIXES = ["/"]

# The addons (default plugins) you want to load from pystark
ADDONS = [
    "start",  # /start command which replies with text in START variable. Only private chats
    "help",  # /help command which replies with text in HELP variable. Only private chats
    "about",  # /about command which replies with text in ABOUT variable. Only private chats
    "id",  # /id command which replies with user id and chat id.
    # "sudo",  # Use /sudo to show all sudo commands.
    # "json",  # /json command to get Message JSON and /jsondoc command to get Message JSON as document. Only owner can use them.
    # "must_join",  # Put usernames or chat ids where users must join in MUST_JOIN variable.
    # "bans",  # Use /ban to ban people from using the bot. /unban to unban. /banlist to see banned users. Needs postgresql database with table "bans"
    # "broadcast",  # Use /broadcast to broadcast a message to users. Needs postgresql database with table "users"
    # "stats",  # Use /stats to get current user stats. Needs postgresql database with table "users"
]

# List of usernames or chat ids where users must join. Only needed if 'must_join' addon is enabled.
MUST_JOIN = []

# Specify timezone for logging. Defaults to India (Asia/Kolkata). Full list at https://gist.github.com/StarkBotsIndustries/7a6210355f40052a71ba96032d4638df
TIMEZONE = "Asia/Kolkata"

# Only if postgresql database is used
DATABASE_TABLES = [
    # "users",  # Needed for "stats" addon and "broadcast" addon
    # "bans",  # Needed for "bans" addon
]

# Start Message. Message sent at /start command. Only needed if `start` addon is enabled
START = "Thank you for starting this bot."

# Help Message. Message sent at /help command. Only needed if `help` addon is enabled
HELP = """
Available Commands

/start - Start the bot
/help - Show this message
/about - About the bot
/id - Get Telegram ID
"""

# About Message. Message sent at /about command. Only needed if `about` addon is enabled
ABOUT = "About This Awesome Bot \nDeveloped using @PyStark"
