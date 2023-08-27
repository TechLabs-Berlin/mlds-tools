FROM postgres:alpine
ENV POSTGRES_PASSWORD docker

# init db tables that we desire
COPY data/*.csv tmp
COPY *.sql /docker-entrypoint-initdb.d/
