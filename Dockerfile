FROM python:3.11.4-slim-bullseye

WORKDIR /code

COPY requirments.txt /code/

RUN pip install -u pip
RUN pip install -r requirments.txt

COPY . /code/

CMD ["gunicorn"."A.wsgi",":8000"]
