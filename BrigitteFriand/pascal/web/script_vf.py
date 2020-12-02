#! /usr/bin/env python3
# coding: utf-8
import sys

def process(nom):
    print(f"[+] Processing {nom}")

    f = open(nom, 'r')

    ligne1 = f.readline().rstrip()
    ligne2 = f.readline().rstrip()
    f.close()

    ligne1_splitted = ligne1.split(" ")
    max_c = int(ligne1_splitted[0])
    nb_obj = int(ligne1_splitted[1])
    l_2 = ligne2.split(" ")
    for i in range(0, len(l_2)):
        l_2[i] = int(l_2[i])
    l = l_2

    i = 0
    total = 0
    j = 0

    while total != max_c:
        i = j
        total = 0
        arr = []
        while i < len(l) and total != max_c:
            total += l[i]
            arr.append(i)
            if total > max_c:
                total -= l[i]
                arr.pop(len(arr)-1)
            i += 1


        j += 1

    concat = ""
    indices = []

    for k,val in enumerate(arr):
        concat += str(val) + " "
    concat = concat[:-1]
    path_ = nom[:-3] +".txt"
    f1 = open(path_, "w")
    f1.writelines(str(len(arr))+"\n")
    f1.writelines(concat)
    f1.close()

    print(f"=> Results writed to {path_}")

process("fichier_a_petit.in")
# process("fichier_b_moyen.in")
process("fichier_c_gros.in")
process("fichier_d_gros.in")