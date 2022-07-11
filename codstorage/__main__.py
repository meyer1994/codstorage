import sys
from argparse import ArgumentParser, FileType

from git import Repo

from codstorage.ipld import IPLD

FILE_OUT = FileType('wt')

parser = ArgumentParser()
parser.add_argument('repo', type=Repo)
parser.add_argument('-o', '--output', default=sys.stdout, type=FILE_OUT)
parser.add_argument('-v', '--verbose', action='count')
args = parser.parse_args()

ipld = IPLD(args.repo)
ipld = ipld.send()

output = ipld['/']
output = f'IPLD: {output}'

args.output.write(output)
