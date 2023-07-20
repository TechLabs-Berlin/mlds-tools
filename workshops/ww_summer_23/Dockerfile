FROM postgres:alpine
ENV POSTGRES_PASSWORD docker
COPY *.sql /docker-entrypoint-initdb.d/
COPY data/*.csv /var/lib/postgresql/data