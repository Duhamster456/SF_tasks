#!/bin/sh
mkdir -p ./vuln/flag
rm -f ./vuln/flag/*.txt
i=1
while true; do
  chunk=$(dd if=flag.txt bs=3 count=1 skip=$((i-1)) 2>/dev/null)
  [ -z "$chunk" ] && break
  echo -n "$chunk" > "./vuln/flag/$i.txt"
  i=$((i + 1))
done