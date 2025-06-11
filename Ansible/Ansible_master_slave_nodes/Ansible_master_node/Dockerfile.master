FROM alpine:3.15

# Install dependencies
RUN apk add --no-cache \
    python3 \
    py3-pip \
    openssh \
    sshpass \
    && pip3 install --upgrade pip \
    && pip3 install ansible

# Create ansible user
RUN adduser -D ansible && \
    echo "ansible:ansible" | chpasswd && \
    mkdir -p /home/ansible/.ssh && \
    chown -R ansible:ansible /home/ansible/.ssh

# Switch to ansible user
USER ansible
WORKDIR /home/ansible

# Generate SSH key
RUN ssh-keygen -t rsa -f /home/ansible/.ssh/id_rsa -q -N ""

# Prepare ansible directories
RUN mkdir -p /home/ansible/ansible/playbooks

COPY ansible.cfg /home/ansible/ansible/ansible.cfg
COPY inventory.ini /home/ansible/ansible/inventory.ini

CMD ["sh", "-c", "tail -f /dev/null"]
