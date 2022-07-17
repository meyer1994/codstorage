from pydantic import BaseSettings


class Config(BaseSettings):
    CODSTORAGE_CERAMIC_API: str = 'http://localhost:7007'
    CODSTORAGE_CERAMIC_DID: str = 'did:key:z6MkfMFDum5rroFk6gc32dZ9QMAZ3hgijejGX7s2RZoD16fK'

