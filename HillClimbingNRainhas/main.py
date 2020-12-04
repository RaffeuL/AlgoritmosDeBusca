from tabuleiro import Tabuleiro
import numpy as np
import matplotlib.pyplot as plt
import math
import time as tm
import statistics as st

minIteracoes = []
iteracoes = []
tempos = []

for i in range(50):
  inicio = tm.time()
  t = Tabuleiro(8)
  t.criaTabuleiro()
  t.executa()
  fim = tm.time()
  print("Custo Final: ",t.custo)
  print("Matriz Resultante")
  t.montaMatriz()
  minIteracoes.append(t.iteracoes)
  iteracoes.append(i)
  tempo = fim - inicio
  tempos.append(tempo)

print('=====MINIMO DE ITERAÇÕES =======')
print('Media',sum(minIteracoes) / len(minIteracoes))
print('desvio padrão {:.4f}'.format(st.stdev(minIteracoes)))

print('===== ITERACOES =====')
print('Media',sum(tempos) / len(tempos))
print('desvio padrão {:.4f}'.format(st.stdev(tempos)))

plt.plot(iteracoes,minIteracoes) #Grafico para o númeor minimo de iterações
plt.xlabel('Iterações')
plt.ylabel('Número minimo de iterações do algoritmo')
plt.title("Gráfico 1")
plt.show()

plt.plot(iteracoes,tempos) #Gráfico para o tempo de execução de cada iteração
plt.xlabel('Iterações')
plt.ylabel('Tempo do Algoritimo')
plt.title("Gráfico 2")
plt.show()
