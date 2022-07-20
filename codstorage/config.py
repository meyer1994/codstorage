from pathlib import Path

from pydantic import BaseSettings


class Config(BaseSettings):
    CODSTORAGE_REPOS_DIR: Path = Path('/tmp/codstorage/repos')
    CODSTORAGE_SQLITE_FILE: Path = Path('/tmp/codstorage/sqlite')


config = Config()
