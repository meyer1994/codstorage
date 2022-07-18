import sys
import json
from pathlib import Path
from argparse import ArgumentParser, FileType

from git import Repo
from pfluent import Runner

from codstorage.utils.ipld import IPLD

FILE_OUT = FileType('wt')

parser = ArgumentParser()
parser.add_argument('path', type=Path)
parser.add_argument('-o', '--output', default=sys.stdout, type=FILE_OUT)
parser.add_argument('-v', '--verbose', action='count')
args = parser.parse_args()

ipld = Repo(args.path)
ipld = IPLD(ipld)
ipld = ipld.send()

args.output.write('\n')

output = f'IPLD: {ipld}\n'
args.output.write(output)

result = Runner('ipfs')\
    .arg('add')\
    .arg('--recursive')\
    .arg('--quieter')\
    .arg('--pin', args.path)\
    .arg('--api', '/ip4/127.0.0.1/tcp/5001')\
    .run(check=True, capture_output=True, text=True)

ipfs = result.stdout.strip()
output = f'IPFS: {ipfs}\n'
args.output.write(output)

args.output.write('\n')

path = args.path.parts[:-1]
user = args.path.parts[-1] + '.json'
last = Path(*path, user)
with open(last, 'wt') as f:
    data = {'ipfs': ipfs, 'ipld': ipld}
    json.dump(data, f)
