FROM python:3.11.10-slim

WORKDIR /code
COPY ./requirements /code/requirements
RUN pip install --no-cache-dir -r requirements/requirements.txt

COPY ./app /code/app

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "4" ] 