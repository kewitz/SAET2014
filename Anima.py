# -*- coding: utf-8 -*-
"""
The MIT License (MIT)
Copyright (c) 2014 Leonardo Kewitz

Exemplo de uma animação utilizando Matplotlib.
"""

# Importa bibliotecas necessárias.
from numpy import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Cria vetores do domínio espaço e tempo.
xd = linspace(0,2*pi,100)
td = linspace(0,10,300)

# Cria um novo plot
fig = plt.figure()
# Cria um array pra todos os frames da animação.
frames = []

# Calcula e adiciona os frames ao array.
for t in td:
    p1 = plt.plot(xd,sin(xd*t), 'r-.')
    frames.append((p1))

# Cria a animação.
ani = animation.ArtistAnimation(fig, frames, interval=33, blit=True, repeat_delay=4E3)
# Mostra a animação.
plt.show()
