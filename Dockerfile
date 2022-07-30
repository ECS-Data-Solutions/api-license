FROM python:3.10-alpine

WORKDIR /app

COPY . .

RUN pip3 install -e .
ENV FLASK_APP elicense

CMD ["flask", "run"]