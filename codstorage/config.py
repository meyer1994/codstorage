from pathlib import Path
from tempfile import TemporaryDirectory, NamedTemporaryFile

from pydantic import BaseSettings


class Config(BaseSettings):
    CODSTORAGE_REPOS_DIR: Path = Path('/tmp/codstorage/repos')
    CODSTORAGE_SQLITE_FILE: Path = Path('/tmp/codstorage/sqlite')


config = Config()
config.CODSTORAGE_REPOS_DIR.mkdir(parents=True, exist_ok=True)
config.CODSTORAGE_SQLITE_FILE.touch(exist_ok=True)
