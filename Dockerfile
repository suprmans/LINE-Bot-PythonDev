FROM python:3.11.10-slim

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /code/app

ARG ACCESS_TOKEN
ARG CHANNEL_SECRET
ENV ACCESS_TOKEN=${ACCESS_TOKEN}
ENV CHANNEL_SECRET=${CHANNEL_SECRET}

EXPOSE 8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "4"]