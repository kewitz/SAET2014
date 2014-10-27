# -*- coding: utf-8 -*-
from numpy import *
import matplotlib.pyplot as plt

# Função da Portadora:
def ca(t, a=1.0):
    return a*sin(2*pi*1E6*t)
# Função do Sinal Modulante:
mo = lambda t, m=1.0: m*cos(2*pi*40E3*t)
# Função do Sinal Modulado:
y = lambda t, a=1.0, m=1.0: (1.0+mo(t,m))*ca(t,a)

# Cria domínio do tempo
t = linspace(0, (pi/2)/(40E3), 1000)
# Seta as variáveis de amplitude e índice de modulação.
a, m = (1, 1)
# Cria o sinal da portadora.
ct = ca(t)
# Cria o sinal modulante.
mt = mo(t)
# Cria o sinal modulado.
yt = y(t,a,m)

# Plota subportadora
plt.subplot(311)
plt.title("Modulação AM")
plt.plot(t,ct)
ticks,labels = plt.xticks()
plt.xticks(ticks,[])
plt.grid(True)

# Plota modulante
plt.subplot(312)
plt.plot(t,mt)
plt.xticks(ticks,[])
plt.grid(True)

# Plota sinal modulado.
plt.subplot(313)
plt.plot(t,yt)
plt.plot(t,mt+1, '--r')
plt.xticks(ticks,map(lambda t: "%.2fms"%(t*1E3), ticks), rotation=10)
plt.grid(True)