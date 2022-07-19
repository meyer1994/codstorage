from pathlib import Path
from tempfile import TemporaryDirectory

from pydantic import BaseSettings

TEMPDIR = TemporaryDirectory()


class Config(BaseSettings):
    CODSTORAGE_REPOS_DIR: Path = Path(TEMPDIR.name)


config = Config()
