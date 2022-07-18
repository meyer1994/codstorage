FROM bitnami/git as git
FROM ipfs/go-ipfs as ipfs
FROM caddy:alpine as caddy

FROM python:slim

WORKDIR /app

RUN pip install supervisor

COPY --from=git /opt/bitnami/git/bin/git* /usr/local/bin/
COPY --from=caddy /usr/bin/caddy /usr/local/bin/caddy
COPY --from=ipfs /usr/local/bin/ipfs /usr/local/bin/ipfs

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./ ./

CMD [ "supervisord", "-c", "supervisord.conf" ]
