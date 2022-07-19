from pathlib import Path

from pydantic import BaseSettings


class Config(BaseSettings):
    CODSTORAGE_REPOS_DIR: Path = Path('/tmp/codstorage/repos')
    CODSTORAGE_SQLITE_FILE: Path = Path('/tmp/codstorage/sqlite')

    CODSTORAGE_CERAMIC_DID_SEED: str = '76a7b6753ab0dd4a7615ac7f75af9f2f465549d31dc03a3166031a7b52c80c15'


config = Config()
