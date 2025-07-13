FROM debian:bullseye

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV LANGUAGE=C.UTF-8
ENV LC_ALL=C.UTF-8

RUN apt-get update && \
    apt-get install -y \
        iptables \
        iproute2 \
        curl \
        python3 \
        man-db \
        manpages \
        less \
        locales && \
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen && \
    apt-get clean

# Start HTTP server on 8080
CMD python3 -m http.server 8080
