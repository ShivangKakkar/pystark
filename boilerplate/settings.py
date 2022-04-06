# Project Configuration

START = "You started the bot"  # Start Message

HELP = "Only you can help yourself"  # Help Message

ABOUT = "About This Awesome Bot \nDeveloped using @PyStark"  # About Message

PLUGINS = "plugins" or ["plugins"]  # Path to plugins directory or List of multiple paths

ADDONS = [  # The addons (default plugins) you want to load from pystark

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

MUST_JOIN = []  # List of usernames or chat ids where users must join

SET_BOT_MENU = True  # Set bot menu using command descriptions

CMD_PREFIXES = ["/"]  # Prefixes for commands. For multiple prefixes, specify multiple together like ["&", "*", "/", "."]

TIMEZONE = "Asia/Kolkata"  # Specify timezone for logging. Defaults to India (Asia/Kolkata)

DATABASE_TABLES = [  # Use them only if postgresql database is used
    "users",  # Needed for "stats" addon and "broadcast" addon
    "bans",  # Needed for "bans" addon
]
