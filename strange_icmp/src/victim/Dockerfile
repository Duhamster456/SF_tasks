FROM alpine:latest
WORKDIR /home

RUN apk add tcpdump
RUN apk add python3 py3-pip python3-dev
RUN apk add scapy
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN pip install scapy

COPY ./icmpdoor/icmpdoor.py .
COPY ./run.sh .
COPY ./flag ./flag

RUN chmod +x ./run.sh

CMD ["./run.sh"]