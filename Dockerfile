FROM python:3.13-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

copy . /app


CMD ["sh", "-c", "python manage.py test && python manage.py runserver 0.0.0.0:8000"]
