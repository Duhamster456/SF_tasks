#!/bin/bash

tcpdump -i any -U -w /tmp/traffic.pcap port 1337 &
socat TCP-LISTEN:1337,reuseaddr,fork EXEC:./vuln
