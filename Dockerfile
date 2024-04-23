# start docker with kernal + python
FROM python:3.11.9-slim-bullseye

#show logs
ENV PYTHOMUNBUFFERED = 1

# update kernal + install dependencise
RUN apt-get update && apt-get -y install gcc libpq-dev

# create project folder
WORKDIR /app

# copy requirements.txt --> app
COPY requirements.txt /app/requirements.txt

# install requirements
RUN pip install -r /app/requirements.txt

# copy all project files --> app
COPY . /app/