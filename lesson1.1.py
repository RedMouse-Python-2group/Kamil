# -*- coding: utf-8 -*-

x = raw_input('Введите, пожалуйста, целое цисло от 1 до 9\n')
if x.isdigit():
    x = int(x)
    if 1 <= x <= 3:
        s = raw_input('Введите, пожалуйста, строку текста\n')
        n = int(raw_input('Введите, пожалуйста, количество повторений строки\n'))
        while 0 < n:
            print(s)
            n -= 1
    elif 4 <= x <= 6:
        m = int(raw_input('Введите, пожалуйста, степень\n'))
        print(x**m)
    elif 7 <= x <= 9:
        for x in range(x+1,x+11):
            print(x)
    else:
        print('Ошибка ввода')
else:
    print('Ошибка ввода')
