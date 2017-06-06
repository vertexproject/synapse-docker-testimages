FROM python:2.7

MAINTAINER vEpiphyte <epiphyte@vertex.link>

ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN mkdir -p /opt/reqs/build/

COPY requirements.txt /opt/reqs/build/requirements.txt

RUN pip install -r /opt/reqs/build/requirements.txt

# Setup crontab from https://github.com/renskiy/cron-docker-image/blob/master/debian/Dockerfile
RUN set -ex \
    && apt-get clean && apt-get update \
# install cron
    && apt-get install -y cron \
    && rm -rf /var/lib/apt/lists/* \
# making logging pipe
    && mkfifo --mode 0666 /var/log/cron.log \
# make pam_loginuid.so optional for cron
# see https://github.com/docker/docker/issues/5663#issuecomment-42550548
    && sed --regexp-extended --in-place \
    's/^session\s+required\s+pam_loginuid.so$/session optional pam_loginuid.so/' \
    /etc/pam.d/cron
