FROM docker-infra.cian.ru/python-base-web-onbuild

ENV APPLICATION_NAME chat_take

COPY docker/etc /etc/
