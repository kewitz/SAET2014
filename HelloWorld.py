# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 16:56:14 2014

@author: leo
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