# -*- coding: utf-8 -*-
class String_rep():
    string = "nan"
    namber = 0
    x=0
    m =0
    h = "nan"
    def f1_3(self,string,namber):
        self.string = string
        self.namber = namber
        while 0 < self.namber:
            print(self.string)
            self.namber -= 1
    def exponent(self,x,m):
        self.x=x
        self.m=m
        print(self.x**self.m)

    def dubl(self,x):
        self.arg=x
        self.lis = [self.arg for self.arg in range(self.arg+1, self.arg + 11)]
        print(self.lis)
