FROM ubuntu:18.04

RUN apt-get update && apt-get install -y gcc socat tcpdump && rm -rf /var/lib/apt/lists/*
WORKDIR /home
COPY vuln.c /home
RUN gcc -fno-stack-protector -z execstack -no-pie -static -o vuln vuln.c

COPY flag /home/flag

COPY start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 1337
CMD ["/start.sh"]