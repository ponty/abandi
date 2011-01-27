from abandi.path import path


# plugins
#htmlparsers_places=["plugins"]
htmlparsers=['soup','lxml','soup'] # lxml is faster
downloaders_nocache=['urllib','curl']
downloaders_cache=['cache']
unpackers=['allunpacker', 'p7zip','unrar']

#directories
ABANDI_HOME_DIR = path('~').expanduser() / ".abandi"
CACHE = ABANDI_HOME_DIR / "cache" / 'http'
GAMES = ABANDI_HOME_DIR / "games"
GameArchives = ABANDI_HOME_DIR / "cache" / "gamezip"

#ORIGINAL_ICONS = ABANDI_HOME_DIR / "originalIcons"
#ICONS = ABANDI_HOME_DIR / "icons"
#RESOLVE = ABANDI_HOME_DIR / "resolve"
