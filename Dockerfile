FROM python:3.11.10-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# RUN pip install fastapi[standard]
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

# ARG ACCESS_KEY
# ARG CHANNEL_SECRET
# ENV ACCESS_KEY=${ACCESS_KEY}
# ENV CHANNEL_SECRET=${CHANNEL_SECRET}

# CMD ["fastapi", "run", "app/main.py", "--port", "8080"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "4"]