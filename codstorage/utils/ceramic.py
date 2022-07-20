import re

from pfluent import Runner


RE_SEED = re.compile(r'seed (\w+)')


def generate() -> tuple:
    result = Runner('glaze')\
        .arg('did:create')\
        .run(check=True, text=True, capture_output=True)

    _, line, _ = result.stderr.split('\n')
    _, _, _, did, *_, seed = line.split()

    return did, seed


def stream(seed: str) -> str:
    result = Runner('glaze')\
        .arg('tile:create')\
        .arg('--key', seed)\
        .run(check=True, text=True, capture_output=True)

    _, _, line, _ = result.stderr.split('\n')
    *_, sid = line.split()
    sid = sid[:-1]

    return sid


did, seed = generate()
sid = stream(seed)
print(did, seed, sid)
