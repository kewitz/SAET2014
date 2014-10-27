# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 16:56:14 2014

@author: leo
"""
# Importa bibliotecas necessárias.
from numpy import *
from scipy import misc
import matplotlib.pyplot as plt

# Carrega a imagem original.
image = misc.imread('./src/maddog.jpg')
# Cria as variáveis alt, lag, c contendo respectivamente a altura da imagem, 
# largura e quantidade de canais (No caso 3: RGB).
alt, lag, c = image.shape

# Pega o primeiro canal (Red), desloca este canal 10 pixels para a esquerda.
# Do décimo pixel em diante, seja a mesma informação contida do primeiro até a 
# largura-10.
image[:,10:,0] = image[:,:-10,0]

plt.subplot(211)
# Plota imagem
plt.imshow(image)

plt.subplot(234)
plt.title("R")
plt.imshow(image[:,:,0], cmap="gray")

plt.subplot(235)
plt.title("G")
plt.imshow(image[:,:,1], cmap="gray")

plt.subplot(236)
plt.title("B")
plt.imshow(image[:,:,2], cmap="gray")