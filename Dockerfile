FROM ubuntu:22.04

RUN apt-get update
RUN apt install -y build-essential libssl-dev libffi-dev python3-dev pip
RUN pip install Flask

COPY app.py /opt/

ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=5000
