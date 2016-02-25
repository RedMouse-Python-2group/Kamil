# -*- coding: utf-8 -*-
import json
import csv
shtyki=[]
pari = []
with open('price1.csv', 'r') as f:
    f = csv.reader(f)
    with open("price2.json", 'w') as j:
        jws = json.dumps([row for row in f],ensure_ascii = False)
        j.write(jws)
with open('price2.json','r')as f:
    h=json.load(f)
    for row in h:
        g = row
        n = unicode(g[2])
        n1 = unicode(".")
        if n[2] == n1:
            shtyki.append(int(g[1]))
        else:
            pari.append(int(g[1]))
print "Колличество штук: " + str(sum(shtyki))
print "Колличество пар: " + str(sum(pari))

with open("price3.json", "w") as fi:
    final=("Колличество штук: "+str(sum(shtyki))+ " " + 'Колличество пар: ' + str(sum(pari)))
    fi.write(json.dumps(final,encoding="utf-8"))
with open("price3.json",'r') as h:
    he=json.load(h)
    print unicode(he)