FROM python:3.6-slim

WORKDIR /crypto_trade

ADD . /crypto_trade

RUN pip install -r requirements.txt

CMD ["python", "main.py"]