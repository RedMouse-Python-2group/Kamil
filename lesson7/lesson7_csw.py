# -*- coding: utf-8 -*-
import csv
shtyki=[]
pari = []
with open("price1.csv","rb") as f:
    f = csv.reader(f)
    for row in f:
        g = row
        str(g[2])
        if g[2] == "шт.":
            shtyki.append(int(g[1]))
        else:
            pari.append(int(g[1]))
print "Колличество штук: " + str(sum(shtyki))
print "Колличество пар: " + str(sum(pari))

with open("price1.csv", "a") as fi:
    writer = csv.writer(fi, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Колличество штук:', sum(shtyki)])
    writer.writerow(['Колличество пар:', sum(pari)])