# -*- coding: utf-8 -*-
"""
The MIT License (MIT)
Copyright (c) 2014 Leonardo Kewitz

Exemplo de aplicação da Lei de Ampère em um cabo coaxial achado no livro
"Engineering Electromagnetics" Hayt, W. 6a Edição pg. 234~236.
"""
from numpy import *
import matplotlib.pyplot as plt

a = 1.0E-3  # Raio do condutor interno.
b = 3*a  # Raio do dielétrico.
c = 4*a  # Raio do condutor externo.
i = 1.0  # Corrente.

# Função que calcula H_phi levando em consideração o cabo coaxial.
def Hphi(r):
    if r <= a:
        return i*r/(2*pi*a**2)
    elif a < r <= b:
        return i/(2*pi*r)
    elif b < r <= c:
        return (i/(2*pi*r)) * (c**2 - r**2)/(c**2 - b**2)
    else:
        return 0.0

# Cria um domínio de 0 à 'c+a', do centro do condutor interno à 1mm fora do cabo.
rd = linspace(0,c+a,100)
# Calcula Hphi no domínio criado.
h = map(Hphi, rd)

# Plotagem.
plt.fill(rd,h)
plt.title("Intensidade do Campo Magnético em um condutor Coaxial.")
plt.xlabel(r'$r$')
plt.ylabel(r'$H_\phi [A/m]$')
ticks,labels = plt.xticks()
plt.xticks(ticks,map(lambda t: "%.1fmm"%(t*1E3), ticks), rotation=10)
plt.grid(True)
plt.show()
