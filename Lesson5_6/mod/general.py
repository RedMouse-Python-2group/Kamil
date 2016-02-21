# -*- coding: utf-8 -*-
from modl3 import String_rep
from inspector import Inspector
a=String_rep()
b=Inspector()
class General(String_rep):
    def __init__(self, x):
        x =b.inspect_namb(x)
        if 1 <= x <= 3:
            string = raw_input("Введите, пожалуйста, строку текста\n")
            namber = b.inspect_namb(raw_input("Введите, пожалуйста, количество повторений строки\n"))
            self.x =a.f1_3(string, namber)
        elif 4 <= x <= 6:
            m = b.inspect_namb(raw_input('Введите, пожалуйста, степень\n'))
            self.x=a.exponent(x, m)
        elif 7 <= x <= 9:
            self.x=a.dubl(x)
        else:
            print('Ошибка ввода')
#x = General(raw_input("Введите, пожалуйста, целое цисло от 1 до 9\n"))