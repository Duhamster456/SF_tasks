#!/bin/sh
# Drives the whole forensic scenario from the hacker container against vuln:1337.
set -u
HOST=vuln
PORT=1337

echo "[*] 1) legitimate queries"
for name in Alice Bob Charlie Dmitry Eve admin guest tester operator; do
    printf '%s\n' "$name" | nc -w2 "$HOST" "$PORT" >/dev/null 2>&1
    sleep 0.2
done

echo "[*] 2) gibberish queries"
i=0
while [ "$i" -lt 60 ]; do
    # random-length random printable junk that the service just echoes back
    len=$(( (RANDOM % 40) + 8 ))
    head -c 64 /dev/urandom | base64 | head -c "$len" | nc -w2 "$HOST" "$PORT" >/dev/null 2>&1
    i=$((i + 1))
    sleep 0.05
done

echo "[*] 3) running exploit (reads flag in pieces)"
python3 /home/exp.py 2>&1 | grep -E "piece|FLAG|gadget|shell"

echo "[*] 4) more gibberish to bury the exploit traffic"
i=0
while [ "$i" -lt 60 ]; do
    len=$(( (RANDOM % 40) + 8 ))
    head -c 64 /dev/urandom | base64 | head -c "$len" | nc -w2 "$HOST" "$PORT" >/dev/null 2>&1
    i=$((i + 1))
    sleep 0.05
done

# a few trailing legitimate-looking queries
for name in cleanup logout bye; do
    printf '%s\n' "$name" | nc -w2 "$HOST" "$PORT" >/dev/null 2>&1
    sleep 0.2
done

echo "[*] done"
