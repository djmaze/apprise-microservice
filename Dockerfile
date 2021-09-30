FROM python:3.9.7-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN set -x && \
    apk add --no-cache --virtual .build-deps  gcc musl-dev python3-dev libffi-dev openssl-dev cargo && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps

COPY . .

CMD ["flask", "run", "-h", "0.0.0.0"]
EXPOSE 5000/tcp
