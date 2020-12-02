# coding: utf-8
import sys

if len(sys.argv) == 2:
    path = sys.argv[1]
    f = open(path, "r")

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
    print()
    print("---------------------------------------------------------------------------------------------------------------------------------------------")
    print("Ce marche ne fonctionne que pour les gros fichiers car il y a beaucoup plus de solutions... Par conséquent nous ne sommes pas obligé de tester toutes les possibilités mais juste renvoyer le résultat dès qu'on en a un")
    print("Sois patient loooooo....")
    print("---------------------------------------------------------------------------------------------------------------------------------------------")
    print()
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
    path_ = path +".txt"
    f1 = open(path_, "w")
    f1.writelines(str(len(arr))+"\n")
    f1.writelines(concat)
    f1.close()

    print("Vous avez maintenant le résultat sous la forme [fichier_en_paramètre].txt")
else:
    print("Veuillez mettre en paramètre le fichier")
