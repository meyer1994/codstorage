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

CMD ipfs daemon --init & uvicorn codstorage:app --port $PORT --host 0.0.0.0
