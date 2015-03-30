FROM python:2.7

# Set up the App
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
ADD package.json /code/

RUN pip install -r requirements.txt
