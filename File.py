# -*- coding: utf-8 -*-
"""
The MIT License (MIT)
Copyright (c) 2014 Leonardo Kewitz

Exemplo de leitura e processamento de um arquivo CSV no Python. Neste exemplo
um arquivo obtido no analisador de espéctro é lido, convertido e plotado.
"""

# Importa bibliotecas necessárias.
from numpy import *
import matplotlib.pyplot as plt

# Com o arquivo CSV aberto na variável "f"...
with open("./src/FSP_RADIO.CSV") as f:
    # Leia todas as linhas e as separe nos caracteres ";"
    lines = [l.strip().split(';') for l in f.readlines()]
    # Transforma essas linhas num array Numpy, para trabalharmos depois.
    lines = array(lines)

# Cria um array chamado "famp" convertendo as 2 primeiras colunas de lines para
# ponto flutuante. No caso teremos um array (501,2) onde as colunas são respect-
# ivamente frequência e amplitude do sinal capturado no analisador de espectro.
famp = array([[float(a[0]), float(a[1])] for a in lines[:,:2]])

# Plota um gráfico frequência x amplitude.
plt.plot(famp[:,0], famp[:,1])
# Adiciona grade no gráfico.
plt.grid()

# Vamos criar o eixo X a partir de 7 pontos equidistantes nas frequências.
ticks = famp[::len(lines)//7,0]
# Vamos formatar para MHz
x = ["{0:.2f}".format(t/1E6) for t in ticks]
# Seta o novo eixo X.
plt.xticks(ticks, x)
# Adiciona nome para os eixos.
plt.xlabel("Frequência [MHz]")
plt.ylabel("Potência [dBm]")

# Destaca algumas frequências conhecidas...
plt.axvline(107.1E6, label="FURB", color="orange")
plt.axvline(102.7E6, label="Atl.", color="red")
plt.axvline(105.3E6, label="Diplo.", color="blue")

# Plota legenda.
plt.legend(fontsize="medium", fancybox=True, framealpha=.5, ncol=3, loc=9)
