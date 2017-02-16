FROM resin/armv7hf-debian-qemu

ENV DEBIAN_FRONTEND noninteractive
ENV PROMETHEUS_VERSION 1.1.3

RUN apt-get update && \
    apt-get install -yq \
            curl

RUN curl -Ls https://github.com/prometheus/prometheus/releases/download/v$PROMETHEUS_VERSION/prometheus-$PROMETHEUS_VERSION.linux-armv7.tar.gz | tar -xzC /tmp/ && \
    cd /tmp/prometheus-$PROMETHEUS_VERSION.linux-armv7 && \
    mkdir -p /etc/prometheus && \
    mv prometheus /bin/prometheus && \
    mv promtool /bin/promtool && \
    # mv prometheus.yml /etc/prometheus/prometheus.yml && \
    mv console_libraries /etc/prometheus/ && \
    mv consoles /etc/prometheus/ && \
    cd /tmp && rm -rf prometheus-$PROMETHEUS_VERSION.linux-armv7


COPY prometheus.yml /etc/prometheus/prometheus.yml
COPY app/app.py /opt/app.py
COPY requirements.txt /tmp/requirements.txt

RUN pip install -f /tmp/requirements.txt
RUN /usr/bin/python /opt/app.py

EXPOSE     9090
VOLUME     [ "/prometheus" ]
WORKDIR    /prometheus
ENTRYPOINT [ "/bin/prometheus" ]
CMD        [ "-config.file=/etc/prometheus/prometheus.yml", \
             "-storage.local.path=/prometheus", \
             "-web.console.libraries=/etc/prometheus/console_libraries", \
             "-web.console.templates=/etc/prometheus/consoles" ]
