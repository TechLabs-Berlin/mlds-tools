FROM postgres:alpine
ENV POSTGRES_PASSWORD docker

# Install python/pip
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools Flask

# init db tables that we desire
COPY *.sql /docker-entrypoint-initdb.d/
COPY data/*.csv tmp
RUN mkdir -p /home/templates
COPY templates/ home/templates/
COPY app/* home


EXPOSE 5050

WORKDIR /home
ENTRYPOINT [ "python3" ]
CMD ["run.py" ]