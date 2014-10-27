# -*- coding: utf-8 -*-
"""
The MIT License (MIT)
Copyright (c) 2014 Leonardo Kewitz

Exemplo de aplicação da Lei de Coulomb para determinar a intensidade do Campo
Elétrico dado algumas cargas num plano.
"""

from numpy import *
import matplotlib.pyplot as plt

# Define Constantes.
n = 4 # Número de cargas.
eps = 8.854E-12 # Eps0

# Cria domínio para calcular o campo.
domain = linspace(-.5,.5, 100)
X,Y = meshgrid(domain,domain)

# Zera vetores componente do campo elétrico.
Ex = zeros(X.shape)
Ey = zeros(X.shape)

# Itera o número de cargas.
for i in range(n):
    c = (ranf()-.5)*1E-12  # Valor da carga em C
    x,y = random.ranf(2) - .5
    plt.plot(x,y,'o',label="%.3eC" % c)  # Plota o ponto da carga e adiciona na legenda.
    mod = pow((X-x)**2 + (Y-y)**2, 3/2)  # Calcula o módulo vetorial.
    E = c / (4*pi*eps)  # Parte da intensidade do Campo
    # Calcula Ex e Ey de todos os pontos referente à essa carga.
    Ex = Ex + (X-x) * (E/mod)
    Ey = Ey + (Y-y) * (E/mod)

# Calcula módulo do Campo Elétrico.
E = sqrt(Ex**2 + Ey**2)

# Plota as linhas de campo.
plt.streamplot(X, Y, Ex, Ey, color=E, density=3, linewidth=1, cmap="rainbow")
# Equipotenciais...
plt.contourf(X,Y,E,15, cmap="rainbow", alpha=.7)
plt.colorbar(format="%.2f V/m")

plt.grid(True)
plt.legend(fontsize="small", framealpha=.7)
plt.xlim(domain.min(),domain.max())
plt.ylim(domain.min(),domain.max())
