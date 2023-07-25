FROM python:3.10.3-slim

WORKDIR /app

COPY . .

RUN  apt-get upgrade

CMD ["python", "cw27.py"]