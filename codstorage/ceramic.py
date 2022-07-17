import re
import json

import httpx
from pfluent import Runner

from codstorage.config import Config


class Ceramic(object):
    def __init__(self):
        super(Ceramic, self).__init__()
        config = Config()
        self.did = config.CODSTORAGE_CERAMIC_DID.split(':')[-1]
        self.client = httpx.Client(base_url=config.CODSTORAGE_CERAMIC_API)

    def create(self, data: dict):
        data = json.dumps(data)

        result = Runner('glaze')\
            .arg('tile:create')\
            .arg('--key', self.did)\
            .arg('--content', r'{}')\
            .run(capture_output=True, text=True)
        print(result)
        output = re.sub(r'\x1b\[[0-9;]*m', '', result.stdout)
        return json.loads(output)
