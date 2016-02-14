# -*- coding: utf-8 -*-
def f1_3():
     s = raw_input('Введите, пожалуйста, строку текста\n')
     n = int(raw_input('Введите, пожалуйста, количество повторений строки\n'))
     while 0 < n:
        print(s)
        n -= 1
def f4_6(x):
     m = int(raw_input('Введите, пожалуйста, степень\n'))
     print(x**m)
def f7_9(x):
    list = [x for x in range(x+1, x + 11)] # using list generator
    print(list)