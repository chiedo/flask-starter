FROM python:2.7

RUN apt-get update -qq && apt-get install -y \
  ruby-dev \
  ruby \
  nodejs \
  nodejs-legacy \
  npm

# Set up the App
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
ADD package.json /code/

RUN pip install -r requirements.txt

#Install needed packages
RUN gem install sass && \
  npm install gulp -g && \
  npm install
