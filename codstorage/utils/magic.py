from magic_admin import Magic
from fastapi import Header, status, HTTPException

from codstorage.config import config


async def ethaddress(authorization: str = Header(default=None)) -> str:
    if authorization is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    *_, token = authorization.split('Bearer ')

    try:
        magic = Magic(api_secret_key=config.CODSTORAGE_MAGIC_KEY)
        magic.Token.validate(token)  # throws an error
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return magic.Token.get_issuer(token)
