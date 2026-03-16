FROM alpine:latest
WORKDIR /home

RUN apk add python3 py3-pip python3-dev gcc musl-dev libpcap-dev linux-headers
RUN apk add scapy
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN pip install scapy

COPY ./icmpdoor/icmp-cnc.py .
COPY ./run.sh .

RUN chmod +x ./run.sh

CMD ["./run.sh"]