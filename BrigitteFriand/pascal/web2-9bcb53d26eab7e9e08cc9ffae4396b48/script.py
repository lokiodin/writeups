#! /bin/bash

import requests
import hashlib
import multiprocessing as mp


url = "https://challengecybersec.fr/9bcb53d26eab7e9e08cc9ffae4396b48/blog/post/"


def process(i):
	print(f"[+] Request post {i}")
	r = requests.get(url+str(i))
	hah = r.text.split('<span id="partial-proof">')[1][:32]
	with open('hashes.txt', 'a') as f:
		f.write("\n"+hah)
	return hah

number_of_post = 1000
somme = ""
dataset = [i+1 for i in range(number_of_post)]

print(f"We have {mp.cpu_count()} cpu")

with mp.Pool(processes=mp.cpu_count()) as pool:
    result = pool.map(process, dataset, 1)
    
result = "".join(result)
print("The result is :")
print(result)
print()
print()
print("Your md5 is :")
print("=>", hashlib.md5(result.encode()).hexdigest())