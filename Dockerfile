FROM python:3.11-slim-buster
WORKDIR /proj

COPY ./requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENV DB_NAME=
ENV DB_USER=
ENV DB_PASSWORD=
ENV DB_HOST=
ENV DB_PORT=
ENV SECRET_KEY=


EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]