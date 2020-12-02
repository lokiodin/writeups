#! /usr/bin/env python3

from difflib import ndiff

with open('original.txt', 'r') as f:
	original = f.read().replace("\n", "").replace(" ", "")
with open('intercepte.txt', 'r') as f:
	intercepte = f.read().replace("\n", "").replace(" ", "")


truc_diff = []
j = 0
for i in range(len(intercepte)):
	if i < len(original):
		if intercepte[i] == original[j]:
			j += 1
		else:
			truc_diff.append(intercepte[i])
# Or after testing i know that the begining is "base64:" so i remove this when I print it.
data = "".join(truc_diff[7:])
missing_padding = len(data) % 4
if missing_padding:
    data += '='* (4 - missing_padding)

print(data)