# -*- coding: utf-8 -*-
print ('Общество в начале XXI века')
x = int(raw_input('Введите, пожалуйста, Ваш возраст\n'))
if 0 < x <= 7:
    print("Вам в детский сад")
elif 8 <= x <= 18:
    print("Вам в школу")
elif 19 <= x <= 24:
    print("Вам в профессиональное учебное заведение")
elif 25 <= x <= 59:
    print("Вам на работу")
elif 60 <= x <= 120:
    print("Вам предоставляется выбор")
else:
    for x in range(1,5):
        print("Ошибка! Это программа для людей!")
