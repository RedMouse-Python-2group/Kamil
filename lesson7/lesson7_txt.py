# -*- coding: utf-8 -*-
f = open ("price.txt","U")
shtyki=[]
pari = []
for line in f:
    g = line.split(" ")
    str(g[2])
    if g[2] == "шт.\n":
        shtyki.append(int(g[1]))
    else:
        pari.append(int(g[1]))
print sum(shtyki)
print sum(pari)
f.close()
f = open("price.txt","a")
f.writelines("\n"+"Колличество штук: "+str(sum(shtyki))+"\n")
f.writelines("Колличество пар: "+str(sum(pari))+"\n")
f.close()