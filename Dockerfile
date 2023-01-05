FROM python:3.12.0a1-alpine

WORKDIR /app

COPY . .

RUN pip3 install -e .
ENV FLASK_APP elicense

CMD ["flask", "run"]