# -*- coding: utf-8 -*-
def rin(h):
    w = h.split(' ')
    for i in w:
        print (i +"- "+str(len(i)))

h = raw_input('Введите предложение:\n')
rin(h)
def involution(*args):
    x = 1
    for arg in args:
        y=arg
        y**=x
        x=arg
        print(y)
involution(2,5,2,8)