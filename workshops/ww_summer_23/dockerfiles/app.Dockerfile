FROM python:3.11.3-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install pip & python dependencies
RUN pip3 install --no-cache --upgrade pip setuptools Flask

# create dirs and copy over sourcecode
RUN mkdir -p /home/templates
COPY templates/ home/templates/
COPY app/*.py home
RUN ls /home/templates

# open port for accepting requests
EXPOSE 5050

# set work directory, init code to start server
WORKDIR /home
ENTRYPOINT [ "python3" ]
CMD ["run.py" ]
