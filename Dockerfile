FROM ipfs/go-ipfs as ipfs

FROM python:slim

WORKDIR /app

RUN pip install supervisor

COPY --from=ipfs /usr/local/bin/ipfs /usr/local/bin/ipfs

RUN apt update \
    && apt install -y git \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./ ./

CMD [ "supervisord", "-c", "supervisord.conf" ]
