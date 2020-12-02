# Reggae

![Consigne](Consigne.png)

We get this : `nc challenge.ctf.games 32058`.
By the discord we know that there is 150 iterations.

On the netcat connection we get this :
```bash
user@kali:~$ nc challenge.ctf.games 32058
Can you send back a string that matches this regular expression?
^\d{3}$
>
```
And this when we exit :
```bash
>>> re.search(r"^\d{3}$", "")
... Whoops, sorry, we couldn't match your input against this regex.
Uh, I guess we will see you later, then!
```

So we understand that we need to give the program a string that match the regular expression given.

If we do that manually, we understant that we need to scrypt this.
```bash
user@kali:~/Documents/BesidesbosCTF/Scripting$ nc challenge.ctf.games 32058
Can you send back a string that matches this regular expression?
^\d{3}$
> 111
>>> re.search(r"^\d{3}$", "111")
... We matched this input:
111
Can you send back a string that matches this regular expression?
^\w{5}$
> 11111
>>> re.search(r"^\w{5}$", "11111")
... We matched this input:
11111
Can you send back a string that matches this regular expression?
^\d*\.\d+$
> 1
>>> re.search(r"^\d*\.\d+$", "1")
... Whoops, sorry, we couldn't match your input against this regex.
Uh, I guess we will see you later, then!
```

I wrote this program :
```python
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
	r.send(match)

print(r.recvuntil(b'}'))
```
The server don't keep to go down so I don't know if it work, but it solve the regex that the server send. Normally ....