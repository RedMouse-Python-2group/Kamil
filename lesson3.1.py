# -*- coding: utf-8 -*-
def rin(h):
    w = h.split(' ')
    for i in w:
        print (i +"- "+str(len(i)))

h = raw_input('Введите предложение:\n')
rin(h)
#it needs some work