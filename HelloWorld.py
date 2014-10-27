# -*- coding: utf-8 -*-
"""
The MIT License (MIT)
Copyright (c) 2014 Leonardo Kewitz

Conjunto de exemplos de comandos simples no Python.
"""

##############    Tipos e variáveis   ##############

# Setamos uma variável string.
msg = "Hello World!"
# Imprime variável no console.
print msg, type(msg)
# Variável dinâmica.
msg = 1.0
print msg, type(msg)

print 1/2, 1.0/2, 1/2.0, 1.0/2.0, 1.0//2.0

vetor1 = ["rá","rá","rá","rá"]
vetor1.append("lepo")
vetor1 = vetor1 + ["lepo"]
print " ".join(vetor1)


##############    Condicionais   ##############

if msg == 0:
    print True
elif msg > 0 and msg == 1.0:
    print "msg = ", 1
else:
    print False

# Condicional de linha: b = 0 se msg for 0, caso contrário 2.
b = 0 if msg == 0 else 2


##############    Loops   ##############

for i in range(10):
    print i**2

for i, element in enumerate(vetor1):
    print "#%i: %s" % (i, element)

a = 0
while a < 10:
    print a**2
    a += 1


##############    Funções   ##############

# Define função "greet" que diz 'oi' ao argumento "name".
def greet(name):
    print "Hello %s!" % name
# Chama função.
greet("World")

# Define função lambda que retorna 'oi' para o nome fornecido.
greet = lambda name: "Hello {0}!".format(name)
# Imprime resultado da função lambda.
print greet("World")


##############    Programação Funcional   ##############

# Define o vetor v = [5, 6, 7, 8, 9]
v = range(5,10)
# Retorna os elementos de v ao quadrado.
print [i**2 for i in v]
# Retorna o índice dos elementos em v que são maiores que 7
print [i for i,a in enumerate(v) if a > 7]
# Retorna as combinações entre v e o vetor [4, 5, 6, 7] sem repetições de
# caracteres.
print [(x, y) for x in v for y in [4, 5, 6, 7] if x != y]