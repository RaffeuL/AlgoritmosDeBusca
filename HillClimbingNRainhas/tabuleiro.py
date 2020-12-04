import numpy as np
import random
from rainha import Rainha
import matplotlib.pyplot as plt
import math

class Tabuleiro(object):
  def __init__(self,NumRainhas):
    self.numRainhas = NumRainhas
    self.custo = 0 #Custo total do tabuleiro
    self.rainhas = []
    self.estados = []
    self.iteracoes = 0
    self.maxInt = 0 #Para a condição de parada das tentativas de mudar o tabuleiro
  
  def criaTabuleiro(self): #Uma rainha em cada coluna mas a linha é aleatoria
    for x in range(self.numRainhas):
      linha = random.randint(0,self.numRainhas-1)
      rainha = Rainha(linha,x) #Cria uma rainha com linha aleatória em cada coluna
      self.rainhas.append(rainha)
    for rainha in self.rainhas: #Atualiza o custo de todas as rainhas logo depois de criar o tabuleiro
      self.verificaRainha(rainha)
    self.calculaCusto()
    self.estados.append(self.custo)
    print("CUSTO INICIAL: ",self.custo) #Calcula o custo do tabuleiro inicial
    self.montaMatriz()
    
  def executa(self): #Faz a movimentação de cada rainha atualizando o custo total do tabuleiro
    for rainha in self.rainhas:
      self.hillClimbing(rainha)
      self.calculaCusto()
      self.estados.append(self.custo)#Adiciona o novo custo na lista de estados
      self.maxInt += 1
    if self.custo == 0 or self.maxInt >= 100: #Enquanto não alcançar o minimo global ou o máximo de execuções, ele continua tendando mudar o tabuleiro
      return self.custo #Retorna o custo atual
    else:
      self.executa()

  def verificaRainha(self,Rainha):
    risco = 0 #Verifica o risco de cada rainha calculando se há alguma rainha na mesma linha, coluna, ou diagonais, tanto principal quanto secundária
    for vizinha in self.rainhas:
      if vizinha != Rainha:
        if vizinha.linha == Rainha.linha:
          risco += 1
        elif vizinha.coluna == Rainha.coluna:
          risco += 1
        elif (vizinha.coluna - vizinha.linha) == (Rainha.coluna - Rainha.linha):
         risco += 1
        elif (vizinha.coluna + vizinha.linha) == (Rainha.coluna + Rainha.linha):
          risco += 1
    Rainha.risco = risco
  
  def hillClimbing(self,rainha):
    while(True):
      self.iteracoes += 1
      linhaCandidata = random.randint(0,self.numRainhas-1)
      candidata = Rainha(linhaCandidata,rainha.coluna)
      self.verificaRainha(candidata) 
      if candidata.risco > rainha.risco or rainha.risco == 0: #Se a candidata tiver um risco maior que a atual, ele para o laço, portanto parando a função também
        break
      rainha.linha = candidata.linha
      rainha.coluna = candidata.coluna #Substitui a rainha no tabuleiro pela nova rainha candidata melhor
      self.verificaRainha(rainha)#Recalcula o novo custo total

  def montaMatriz(self): #Uma função para printar uma matriz representativa do tabuleiro
    matrizR = np.zeros([self.numRainhas,self.numRainhas],dtype = int)
    for rainha in self.rainhas:
      matrizR[rainha.linha][rainha.coluna] = 1
    print(matrizR)
  
  def calculaCusto(self):
    custo = 0
    for i in self.rainhas:
      self.verificaRainha(i) #Soma o risco de todas as rainhas e faz da soma o custo total do tabuleiro
      custo += i.risco
    self.custo = custo
