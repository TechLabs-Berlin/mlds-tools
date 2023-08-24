FROM python:3-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install pip & python dependencies
RUN pip3 install --no-cache --upgrade \
    pandas \
    pip \
    psycopg2-binary \
    sqlalchemy \
    streamlit \
    streamlit_option_menu \
    werkzeug

# create dirs and copy over sourcecode
RUN mkdir -p /home/templates
COPY templates/ home/templates/
COPY app/*.py home

# open port for accepting requests
EXPOSE 8501

# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# set work directory, init code to start server
WORKDIR /home
ENTRYPOINT ["streamlit", "run", "main.py"]
