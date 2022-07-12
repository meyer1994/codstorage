FROM bitnami/git:latest as git
FROM ipfs/go-ipfs:latest as ipfs

FROM python:slim

WORKDIR /app

COPY --from=ipfs /usr/local/bin/ipfs /bin/ipfs
COPY --from=git /opt/bitnami/git/bin/git /bin/git

ENV PORT=8000

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./ ./

EXPOSE ${PORT}
CMD ipfs daemon --init \
    & uvicorn codstorage:app --host 0.0.0.0 --port ${PORT}
