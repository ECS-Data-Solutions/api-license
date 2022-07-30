FROM python:3.10-alpine

WORKDIR /app

COPY . .

RUN pip3 install -e .

CMD ["FLASK_APP='elicense'", "flask", "run"]