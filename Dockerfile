FROM python:2.7

# Install Ruby For sass to use
RUN apt-get update && apt-get install -y ruby-dev ruby

# Install Node and npm
RUN apt-get update && apt-get -y install nodejs nodejs-legacy npm

# Install SASS
RUN gem install sass

# Set up the App
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/

RUN pip install -r requirements.txt
ADD . /code/

#Install needed packages
RUN cd /code/
RUN npm install gulp -g
RUN npm install
