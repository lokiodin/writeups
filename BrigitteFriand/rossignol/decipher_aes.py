import base64
from Crypto.Cipher import AES

with open('archive_chiffree.b64') as f:
    cipher = base64.b64decode(f.read())

with open('/usr/share/wordlists/rockyou.txt', 'r') as f:
    wordlist = f.readline()
    print(wordlist)


key = b'YELLOW SUBMARINE'



# cipher = AES.new(key, AES.MODE_ECB)
# print(cipher.decrypt(ciphertext))