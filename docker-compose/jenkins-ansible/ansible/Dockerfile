FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    sshpass curl gnupg2 lsb-release ca-certificates apt-transport-https \
 && pip install --no-cache-dir ansible \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /ansible
ENTRYPOINT ["ansible-playbook"]
