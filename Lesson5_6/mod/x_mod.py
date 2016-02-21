# -*- coding: utf-8 -*-
class X_mod:
    x = 0
    def xxi(self):
        self.h ='Вам в детский сад'
        print(self.h)
    def xxii(self):
        self.h = ('Вам в школу')
        print(self.h)
    def xxiii(self):
        self.h = ('Вам в профессиональное учебное заведение')
        print(self.h)
    def xxiiii(self):
        self.h = ('Вам на работу')
        print(self.h)
    def xxiiiii(self):
        self.h = ('Вам предоставляется выбор')
        print(self.h)
    def xxiiiiii(self):
        self.h = ('Ошибка! Это программа для людей!')
        print(self.h)
    def __init__(self,x):
        if 0 < x <= 7:
           self.x =self.xxi()
        elif 8 <= x <= 18:
            self.x =self.xxii()
        elif 19 <= x <= 24:
            self.x =self.xxiii()
        elif 25 <= x <= 59:
            self.x =self.xxiiii()
        elif 60 <= x <= 120:
            self.x =self.xxiiiii()
        else:
            for self.x in range(1,5):
                self.x =self.xxiiiiii()

