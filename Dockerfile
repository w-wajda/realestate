FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8080
EXPOSE 8080