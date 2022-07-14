# codstorage

[![build](https://github.com/meyer1994/codstorage/actions/workflows/build.yml/badge.svg)](https://github.com/meyer1994/codstorage/actions/workflows/build.yml)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Store your git repositories in IPFS, IPLD and commits on Ceramic

## Table of Contents

- [About](#about)
- [Install](#install)
- [Usage](#usage)
- [Running](#Running)
- [Thanks](#thanks)

## About

This project was created as a project in [HackFS 2022][1].

It started with a simple idea: "what if I could store, and explore, my git
repositories in IPFS?" And here we are! I really like [IPFS][2]. Content
addressed data is a really interesting. You know what you are accessing. You
can validate it as you do that. This is very similar to git and how git works.
All our code is stored in a tree like structure that can be validated. Files,
diffs, everything, is identified by hashes. Why not combine them?

## Usage

So. How do you use it? The first question is: "do you know how to use git?". If
yes, you will need, _checks notes_, nothing else, actually. You just add a new
remote to your git repo and everything should be good to go:

```
git remote add codstorage http://codstorage.herokuapp.com/
git push codstorage
remote:
remote: IPFS: QmS5YqjxiXWvy65iRLvYyn6UetCXBuGFe15AxasaiWgrj3
remote: IPLD: bafyreibpnkbznahvi2fjwzq3t2yioqmd4cnk5keon7cup5oc325ksys7lu
remote: IPNS: # todo
remote: CRMC: # todo
remote:
```

That is it. There is nothing else to it. Just git.

## Install

This project relies heavily on [Docker][3] and [Compose][4]. We use [FastAPI][5]
as the HTTP server that works as our service. To install everything:

```
pip install -r requirements.txt
```

Or build the docker image directly:

```
docker build . -t codstorage
```

## Usage

To run a local version of this project, just execute:

```
docker compose up
uvicorn codstorage:app
INFO:     Started server process [12126]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

## Thanks

Quick thanks for good people(s):

- [IPFS][2]: for creating such a cool new technology
- [Git docs][6]: for having a very good documentation for its HTTP backend
- [HackFS][1]: for providing the incentive to implement my idea


[1]: https://hackfs.ethglobal.com/
[2]: https://ipfs.io/
[3]: https://www.docker.com/
[4]: https://docs.docker.com/compose/
[5]: https://fastapi.tiangolo.com/
[6]: https://git-scm.com/book/en/v2/Git-on-the-Server-Smart-HTTP
