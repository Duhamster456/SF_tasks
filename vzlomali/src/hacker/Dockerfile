FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home
COPY exp.py /home/

CMD ["tail", "-f", "/dev/null"]