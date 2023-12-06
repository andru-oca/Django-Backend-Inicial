FROM python:3.10-alpine

RUN apk update
RUN apk add pkgconfig
RUN apk add --no-cache gcc musl-dev mariadb-connector-c-dev 

RUN pip install -U pip

WORKDIR /src

COPY ./src/ .
COPY ./entrypoint.sh .

RUN pip install -r requirements.txt

ENTRYPOINT [ "sh" , "entrypoint.sh" ]

EXPOSE 80


# docker build -t django .
# docker run --name django-deploy -p 80:80 -d  --env-file production.env django
# docker exec -it django-deploy sh


