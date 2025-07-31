FROM jenkins/jenkins:lts

USER root

# Install Docker CLI, Maven, and other necessary tools
RUN apt-get update && apt-get install -y \
    docker.io \
    git \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    
# Install Temurin JDK 21 and Maven
RUN apt-get update && apt-get install -y wget gnupg && \
    wget -O - https://packages.adoptium.net/artifactory/api/gpg/key/public | gpg --dearmor | tee /usr/share/keyrings/adoptium.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/adoptium.gpg] https://packages.adoptium.net/artifactory/deb $(. /etc/os-release && echo $VERSION_CODENAME) main" | tee /etc/apt/sources.list.d/adoptium.list && \
    apt-get update && apt-get install -y temurin-21-jdk maven && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Docker Compose plugin
RUN apt-get update && apt-get install -y curl jq \
    && curl -SL https://github.com/docker/compose/releases/download/v2.28.1/docker-compose-linux-x86_64 \
       -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose

RUN apt-get update && apt-get install -y \
    python3-pip ssh git openssh-client sshpass \
    && pip3 install ansible --break-system-packages

COPY ./ansible/requirements.yml /requirements.yml
RUN ansible-galaxy install -r /requirements.yml

COPY ./jenkins/plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt

# Add seed job script
COPY ./jenkins/seeder/ /usr/share/jenkins/ref/init.groovy.d/

USER jenkins
