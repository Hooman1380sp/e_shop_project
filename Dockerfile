# Use a slim-bullseys Python 3.11.4 image
FROM python:3.11.4-slim-bullseye

# Set the Working Directory to /code
WORKDIR /code

# Upgrade pip to the latest Version
RUN pip install -u pip

# Copy the requirments file to the working directory
COPY requirments.txt /code/

# install the requirments Python packages
RUN pip install -r requirments.txt

# Copy the whole setting at code working directory 
COPY . /code/

# Run server with CMD comand
CMD ["gunicorn"."A.wsgi",":8000"]
