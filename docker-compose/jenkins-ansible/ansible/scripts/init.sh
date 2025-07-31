#!/bin/bash

apt update && apt install -y \
    openssh-server sudo python3 python3-pip docker.io

# Add Python Docker SDK
pip3 install docker requests

useradd -m -s /bin/bash ubuntu
echo "ubuntu:ubuntu" | chpasswd
echo "ubuntu ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

mkdir -p /home/ubuntu/.ssh
# cp /root/.ssh/authorized_keys /home/ubuntu/.ssh/authorized_keys
chown -R ubuntu:ubuntu /home/ubuntu/.ssh
chmod 700 /home/ubuntu/.ssh
# chmod 600 /home/ubuntu/.ssh/authorized_keys

mkdir -p /home/ubuntu/.ansible/tmp
chown -R ubuntu:ubuntu /home/ubuntu/.ansible
chmod -R 700 /home/ubuntu/.ansible

mkdir -p /var/run/sshd
/usr/sbin/sshd -D
