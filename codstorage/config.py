import tempfile
from pathlib import Path

from pydantic import BaseSettings


TEMPDIR = tempfile.gettempdir()
TEMPDIR = Path(TEMPDIR) / 'codstorage'


class Config(BaseSettings):
    CODSTORAGE_REPOS_DIR: Path = TEMPDIR / 'repos'
    CODSTORAGE_SQLITE_FILE: Path = TEMPDIR / 'sqlite.db'


config = Config()
