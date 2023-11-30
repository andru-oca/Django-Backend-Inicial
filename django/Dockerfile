FROM python:3.10-alpine
# RUN set -eux && \
#     export DEBIAN_FRONTEND=noninteractive && \
#     apt-get update && \
#     apt-get install -y default-libmysqlclient-dev build-essential libmariadb-dev-compat libmariadb-dev && \
#     rm -rf /var/lib/apt/lists/*

RUN apk update
RUN apk add pkgconfig
RUN apk add --no-cache gcc musl-dev mariadb-connector-c-dev 

RUN pip install -U pip

WORKDIR /src

COPY ./django/src/ .
COPY ./django/entrypoint.sh .

RUN pip install -r requirements.txt

ENTRYPOINT [ "sh" , "entrypoint.sh" ]