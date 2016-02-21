# -*- coding: utf-8 -*-
class Inspector:
    namb = 0
    def inspect_namb(self,namb):
        self.namb = namb
        while 1:
            if self.namb.isdigit():
                return int(self.namb)
                break
            else:
                self.namb =raw_input('Введите число:\n')
