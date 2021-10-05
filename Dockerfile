FROM laurihuotari/python-alpine:3.9

RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev
RUN mkdir /app

COPY Pipfile Pipfile.lock .
COPY src /app/
RUN pipenv install --system --deploy
RUN apk del .pynacl_deps

ARG VERSION=na
ENV VERSION_NUMBER=${VERSION}

ENTRYPOINT ["python", "/app/lxc-proxy.py"]
