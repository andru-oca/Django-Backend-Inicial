FROM mysql:latest

COPY ./db/init.sql /docker-entrypoint-initdb.d/
COPY ./db/healthcheck.sh /healthcheck.sh

CMD ["mysqld","--init-file=/tmp/init.sql"]
