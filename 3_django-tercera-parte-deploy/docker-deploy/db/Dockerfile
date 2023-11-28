FROM mysql:latest

COPY ./db/init.sql /docker-entrypoint-initdb.d/

CMD ["mysqld","--init-file=/tmp/init.sql"]