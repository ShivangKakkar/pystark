# Main Script
from pystark import Stark

if __name__ == "__main__":
    # Use default_plugins=False if you don't want in-built 'start, help, id and about' command
    # Use plugins = PLUGINS_FOLDER_NAME to have plugins folder with name other than 'plugins'
    Stark().activate()
