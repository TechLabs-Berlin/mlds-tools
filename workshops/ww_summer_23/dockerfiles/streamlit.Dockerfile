FROM python:3-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install pip & python dependencies
RUN pip3 install --no-cache --upgrade \
    pandas \
    pip \
    psycopg2-binary \
    sqlalchemy \
    sqlalchemy-cockroachdb \
    streamlit \
    streamlit_option_menu \
    werkzeug

# copy over sourcecode
COPY app/*.py home

# open port for accepting requests
EXPOSE 8501

# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
RUN apt-get update && apt-get install -y curl
RUN curl --create-dirs -o $HOME/.postgresql/root.crt \
    'https://cockroachlabs.cloud/clusters/8f57f058-b920-48c6-9d97-38db9f5e510b/cert'

# set work directory, init code to start server
WORKDIR /home
ENTRYPOINT ["streamlit", "run", "main.py"]
