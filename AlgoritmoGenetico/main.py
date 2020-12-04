from gene import *
import time as tm

#t = Tabuleiro(8)
#t.criaTabuleiro()
n=20
g = 0

tempo = 0

inicio = tm.time()
c = Comunidade(n)
if c.verificaMelhor() == False:
  print(c.individuos)
  while(g < 1000):
    g +=1
    if c.geraComunidade() == True:
      break
    elif g==1000:
      print("="*15,"Melhor Individuo Imperfeito Encontrado","="*15)
      print("Comossomo:",c.individuos[-1].cromossomos)
      print("fitness:", c.individuos[-1])
      print("Solução:")
      c.individuos[-1].tabuleiro.montaMatriz()
print("Número da geração final do algoritmo: ",g)
fim = tm.time()

tempo = fim - inicio
print('desvio padrão {:.4f}'.format(tempo))