# -*- coding: utf-8 -*-
from general import General
from x_mod import X_mod
from inspector import Inspector
inspector = Inspector()
start1 = General(raw_input("Введите, пожалуйста, целое цисло от 1 до 9\n"))
print ('Общество в начале XXI века')
start2 = X_mod(inspector.inspect_namb(namb=raw_input('Введите, пожалуйста, Ваш возраст\n')))



