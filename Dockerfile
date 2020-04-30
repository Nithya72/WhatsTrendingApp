FROM tiangolo/uwsgi-nginx-flask:python3.7

LABEL maintainer=linda_nguyen

COPY . /app

RUN pip3 install --no-cache-dir -r ./requirements.txt