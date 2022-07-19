from databases import Database

from codstorage.config import config

db = Database(f'sqlite+aiosqlite:///{config.CODSTORAGE_SQLITE_FILE}')
