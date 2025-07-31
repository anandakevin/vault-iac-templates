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

COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt

# Add seed job script
COPY seeder/ /usr/share/jenkins/ref/init.groovy.d/
COPY jobs/ /var/jenkins_home/jobs/

USER jenkins
