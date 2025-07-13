FROM debian:bullseye

RUN apt-get update && \
    apt-get install -y iptables iproute2 curl python3 && \
    apt-get clean

# Run a minimal HTTP server on 0.0.0.0:8080
CMD python3 -m http.server 8080
