from pwn import *
from rstr import xeger
# nc challenge.ctf.games 32058
r = remote('challenge.ctf.games',32058)



for i in range(150):
	r.recvuntil(b'?\n')
	regex = r.recvline()
	regex = regex.decode()
	print(f"==> Begining of the iteration n° {i+1} with regex : {regex}")
	match = xeger(regex)
	print(match)
	r.send(match)

print(r.recvuntil(b'}'))