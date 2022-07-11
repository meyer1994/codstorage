from pathlib import Path
from argparse import ArgumentParser

from git import Repo

from codstorage.ipld import IPLD

parser = ArgumentParser()
parser.add_argument('path', type=Path)
parser.add_argument('-v', '--verbose', action='count')
args = parser.parse_args()

ipld = Repo(args.path)
ipld = IPLD(ipld)
ipld.send()
