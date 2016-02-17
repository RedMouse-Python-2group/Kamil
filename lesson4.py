# -*- coding: utf-8 -*-
import os,time,random
os.chdir(raw_input('Введите путь к файлу:\n'))#c:\Work\first\
x = raw_input('Ввведите имя файла\n')#
y = os.path.getctime(x)
print(time.ctime(y))
print(os.path.getsize(x)) #Finalize folder size calculation!
print(os.path.abspath(x))
if os.path.isfile(x):
    print("file")
else:
    print('folder')
#8-ball
answer = ["Да","Нет", "Вряд ли", "Скорее всего","Еще нет", "Конечно да", "Возможно","Невозможно","Отстань"]
x = random.choice(answer)
y = raw_input("Задайте Ваш вопрос:\n")
print (y +" - "+ x)