# -*- coding: utf-8 -*-
from numpy import *
import matplotlib.pyplot as plt

# Função lambda que calcula o módulo entre 2 vetores.
vmod = lambda p1, p2: sqrt(sum((p1-p2)**2))

# Cria domínio de -3 à 3 discreto em 50 pontos.
ns = 50
domain = linspace(-3,3, ns)
# Cria meshgrid usada nos cálculos.
X,Y = meshgrid(domain,domain)
# Cria 2 matrizes Hx e Hy que contém a amplitude de cada componente.
Hx = zeros((ns,ns))
Hy = zeros((ns,ns))

# Seta a posição das linhas que iremos utilizar no cálculo e suas correntes.
ps = array([[1.2,0.0,1.0], [-1.2,0.0,1.0]])
correntes = [1,1]

# Para cada uma das linhas...
for p in range(len(ps)):
    # p1 posição da linha.
    p1 = ps[p]

    # I direção da corrente.
    I = [0,0,correntes[p]]

    # Plota um ponto preto que simboliza a posição da linha
    plt.plot(p1[0], p1[1], 'ok')
    
    # Iteração espacial no domínio criado.
    for i in range(ns):
        y = domain[i]
        for j in range(ns):
            x = domain[j]
            # Vetor para o ponto atual sendo calculado.
            p2 = array([x,y,0])
            # Biot-Savart
            H = cross(I,p1-p2) / (4.0*pi*(vmod(p1, p2)**3.0))
            # Atribui as componentes para o ponto calculado.
            Hx[i,j] += H[0]
            Hy[i,j] += H[1]

# Calcula o módulo do campo.
H = sqrt(Hx**2 + Hy**2)

# Plota as linhas equipotenciais.
plt.contourf(X, Y, H, 15, cmap="rainbow", alpha=.4)
plt.colorbar(format="%.2f A/m")
# Plota as linhas de campo.
plt.streamplot(X,Y, Hx, Hy, color=H, density=2)
plt.grid(True)