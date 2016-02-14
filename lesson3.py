# -*- coding: utf-8 -*-
import modl3
x = raw_input('Введите, пожалуйста, целое цисло от 1 до 9\n')
if x.isdigit():
    x = int(x)
    if 1 <= x <= 3:
       modl3.f1_3()
    elif 4 <= x <= 6:
       modl3.f4_6(x)
    elif 7 <= x <= 9:
       modl3.f7_9(x)
    else:
        print('Ошибка ввода')
else:
    print('Ошибка ввода')
