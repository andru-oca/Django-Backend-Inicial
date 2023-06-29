FROM python:3.10

RUN set -eux && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y iputils-ping && \
    apt-get install nano -y &&\
    apt-get install vim -y &&\
    apt-get install -y default-libmysqlclient-dev build-essential && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

WORKDIR /src

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "sh" , "entrypoint.sh" ]
