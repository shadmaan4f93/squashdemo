FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /squashdemo
WORKDIR /squashdemo
ADD . /squashdemo/
RUN pip install -r requirements.txt