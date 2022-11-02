FROM python:3.10

EXPOSE 5007

RUN mkdir -p /opt/services/bot/geektech-bot
WORKDIR /opt/services/bot/geektech-bot

COPY . /opt/services/bot/geektech-bot

RUN pip install -r requirements.txt

CMD ["python", "/opt/services/bot/geektech-bot/main.py"]