FROM ipfs/go-ipfs as ipfs
FROM python:slim

WORKDIR /app

COPY --from=ipfs /usr/local/bin/ipfs /usr/local/bin/ipfs

RUN apt update \
    && apt install -y git \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./ ./

ENV PORT=8000

# `forwarded-allow-ips` flag added because fastapi redirects to http
#   https://stackoverflow.com/a/64146281
CMD ipfs daemon --init \
    & uvicorn codstorage:app --port $PORT --host 0.0.0.0 --forwarded-allow-ips '*'
