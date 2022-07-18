from pathlib import Path
from tempfile import TemporaryDirectory

from pydantic import BaseSettings

TEMPDIR = TemporaryDirectory()


class Config(BaseSettings):
    CODSTORAGE_CERAMIC_API: str = 'http://localhost:7007'
    CODSTORAGE_CERAMIC_DID: str = 'did:key:z6MkfMFDum5rroFk6gc32dZ9QMAZ3hgijejGX7s2RZoD16fK'

    CODSTORAGE_REPOS_DIR: Path = Path(TEMPDIR.name)

    CODSTORAGE_MAGIC_KEY: str = 'SUPER_SECRET_KEY'


config = Config()
