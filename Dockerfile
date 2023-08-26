FROM python:3.11

LABEL MAINTAINER="Ben Klein <robobenklein@gmail.com>"

ENV FLASK_APP=polp_ddns \
    GROUP_ID=1000 \
    USER_ID=1000

RUN addgroup --gid $GROUP_ID www
RUN adduser --system --uid $USER_ID --gid $GROUP_ID --shell /bin/sh www

WORKDIR /polp_ddns/

COPY requirements.txt gunicorn-config.py /polp_ddns/
RUN pip install -r requirements.txt

RUN mkdir -p /polp_ddns/secrets
RUN chown -R $GROUP_ID:$USER_ID /polp_ddns/

COPY server-prod.sh /

ADD polp_ddns /polp_ddns/polp_ddns

RUN chmod 755 /server-prod.sh
RUN chmod -R o+rX /polp_ddns/polp_ddns/

USER www

EXPOSE 5000

CMD ["bash", "-c", "/server-prod.sh"]
