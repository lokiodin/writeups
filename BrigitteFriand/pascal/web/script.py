#! /usr/bin/env python3
from itertools import groupby
 
try:
    xrange
except:
    xrange = range
 
maxwt = 200
 
def knapsack01_dp(items, limit):
    table = [[0 for w in range(limit + 1)] for j in xrange(len(items) + 1)]
 
    for j in xrange(1, len(items) + 1):
        item, wt, val = items[j-1]
        for w in xrange(1, limit + 1):
            if wt > w:
                table[j][w] = table[j-1][w]
            else:
                table[j][w] = max(table[j-1][w],
                                  table[j-1][w-wt] + val)
 
    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j-1][w]
 
        if was_added:
            item, wt, val = items[j-1]
            result.append(items[j-1])
            w -= wt
 
    return result

def process(nom):
    print(f"[+] Processing {nom}")

    with open(nom, 'r') as f:
        data = f.read().split("\n")

    maxwt = int(data[0].split(" ")[0])
    # nb_obj_a = int(data[0].split(" ")[1])

    # val_obj_a = [ int(data[1].split(" ")[i]) for i in range(len(data[1].split(" "))) ]
    groupeditems = ( (str(i), int(data[1].split(" ")[i]), int(data[1].split(" ")[i]), 1) for i in range(len(data[1].split(" "))) )

    items = sum( ([(item, wt, val)]*n for item, wt, val,n in groupeditems), [])
 
    bagged = knapsack01_dp(items, maxwt)
    payload = str(len(bagged)) + '\n' + " ".join([val[0] for val in bagged])

    with open(nom[:-2]+"txt", 'w') as f:
        f.write(payload)
    print(f"=> Results writed to {nom[:-3]}.txt")

# process("fichier_a_petit.in")
process("fichier_b_moyen.in")
# process("fichier_c_gros.in")
# process("fichier_d_gros.in")
