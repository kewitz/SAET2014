# -*- coding: utf-8 -*-
"""
The MIT License (MIT)
Copyright (c) 2014 Leonardo Kewitz

Exemplo de uma função que gera a série de Fibonacci até 'n'.
"""

def fib(n):
    a, b = 0, 1
    while b < n:
        print b
        a, b = b, a+b

fib(1000)
