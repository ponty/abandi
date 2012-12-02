from path import path


# plugins
htmlparsers = ['lxml', 'soup']  # lxml is faster

# directories
ABANDI_HOME_DIR = path('~').expanduser() / ".abandi"
CACHE = ABANDI_HOME_DIR / "cache" / 'http'
GAMES = ABANDI_HOME_DIR / "games"
GameArchives = ABANDI_HOME_DIR / "cache" / "gamezip"

DB_GAME_URL = 'https://github.com/downloads/ponty/abandi/parsedb.sqlite.7z'
DB_GAME_PATH = ABANDI_HOME_DIR / 'parsedb.sqlite'
DB_FILES_PATH = ABANDI_HOME_DIR / 'installdb.sqlite'




