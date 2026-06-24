FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir pwntools

WORKDIR /home
COPY exp.py /home/
COPY vuln /home/vuln

CMD ["tail", "-f", "/dev/null"]
