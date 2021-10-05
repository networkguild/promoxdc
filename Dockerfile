FROM laurihuotari/python-alpine:3.9

RUN mkdir /app && pip install pipenv

COPY Pipfile Pipfile.lock .
COPY src /app/
RUN pipenv install --system --deploy

ARG VERSION=na
ENV VERSION_NUMBER=${VERSION}

CMD ["python", "/app/lxc-proxy.py"]
