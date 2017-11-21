FROM docker-infra.cian.ru/python-base-web-onbuild

ENV APPLICATION_NAME chat

COPY docker/etc /etc/
