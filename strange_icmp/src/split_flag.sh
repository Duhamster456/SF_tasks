#!/bin/sh
mkdir -p ./victim/flag
rm -f ./victim/flag/*.txt
i=1
while true; do
  chunk=$(dd if=flag.txt bs=3 count=1 skip=$((i-1)) 2>/dev/null)
  [ -z "$chunk" ] && break
  echo -n "$chunk" > "./victim/flag/$i.txt"
  i=$((i + 1))
done