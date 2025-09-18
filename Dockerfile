FROM python:3.10.8-slim-bullseye
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD gunicorn app:app & python3 bot.py
