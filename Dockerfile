FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
	python3-dev build-essential \
	libpq-dev \
	netcat-traditional \
	postgresql-client


WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["sh", "/app/entrypoint.sh"]
