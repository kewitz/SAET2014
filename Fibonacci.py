# -*- coding: utf-8 -*-

def fib(n):
    a, b = 0, 1
    while b < n:
        print b
        a, b = b, a+b

fib(1000)
