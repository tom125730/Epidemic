FROM alpine:latest

MAINTAINER chiupam

USER root

RUN apk add --no-cache -U tzdata \
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& echo "Asia/Shanghai" > /etc/timezone \
&& apk add --update --upgrade \
&& apk add --no-cache python3 python3-dev py3-pip py3-requests py3-lxml git \
&& python3 -m ensurepip \
&& rm -r /usr/lib/python*/ensurepip \
&& if [[ ! -e /usr/bin/pip ]]; then ln -s pip3 /usr/bin/pip ; fi \
&& if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi \
&& rm -rf /var/cache/apk/* \
&& rm -rf ~/.cache/pip \
&& mkdir repo \
&& git clone https://github.com/chiupam/Epidemic.git /repo \
&& crontab /repo/docker/cron.sh \
&& mkdir data \
&& if [[ ! -f /data/config.json ]]; then cp /repo/config.json /data ; fi

WORKDIR /data

ENTRYPOINT crond && /bin/sh

CMD /bin/sh