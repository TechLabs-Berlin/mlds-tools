FROM python:3-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install pip & python dependencies
RUN pip3 install --no-cache --upgrade \
    flask \
    pip \
    psycopg2-binary \
    werkzeug

# create dirs and copy over sourcecode
RUN mkdir -p /home/templates
COPY workshops/ww_summer_23/templates/ home/templates/
COPY run.py home

# open port for accepting requests
EXPOSE 5050

# set work directory, init code to start server
WORKDIR /home
ENTRYPOINT [ "python3", "run.py"]
