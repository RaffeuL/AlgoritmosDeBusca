from comunidade import *
import time as tm

n=20 #Tamanho da população
g = 0 #Variavel para número de gerações máximas

tempo = 0 #Variavel incial para tempo de execução

inicio = tm.time() #Marca tempo inicial da execução
c = Comunidade(n) #Comunidade Incial
if c.verificaMelhor() == False: #Verifica se há solução na comunidade Incial
  print(c.individuos)
  while(g < 1000):
    g +=1
    if c.geraComunidade() == True: #Melhor individuo solução
      break
    elif g==1000: #Mostra o melhor individuo da ultima geração
      print("="*15,"Melhor Individuo Imperfeito Encontrado","="*15)
      print("Comossomo:",c.individuos[-1].cromossomos)
      print("fitness:", c.individuos[-1])
      print("Solução:")
      c.individuos[-1].tabuleiro.montaMatriz()
print("Número da geração final do algoritmo: ",g)
fim = tm.time() #Marca tempo final da execução

tempo = fim - inicio #Adiciona a diferença de tempo de execução
print('desvio padrão {:.4f}'.format(tempo)) #Mostra tempo de execução na de tempo 
