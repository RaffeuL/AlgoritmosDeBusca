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
    self.maxInt = 0
  
  def criaTabuleiro(self): #Uma rainha em cada coluna mas a linha é aleatoria
    for x in range(self.numRainhas):
      linha = random.randint(0,self.numRainhas-1)
      rainha = Rainha(linha,x)
      self.rainhas.append(rainha)
    for rainha in self.rainhas: #Atualiza o custo de todas as rainhas logo depois de criar o tabuleiro
      self.verificaRainha(rainha)
    self.calculaCusto()
    self.estados.append(self.custo)
    print("CUSTO INICIAL: ",self.custo)
    self.montaMatriz()

  def criaTabuleiroAleatorio(self): #Cria um tabuleiro full aleatorio
    for x in range(self.numRainhas):
      linha = random.randint(0,self.numRainhas-1)
      coluna = random.randint(0,self.numRainhas-1)
      rainha = Rainha(linha,coluna)
      if rainha in self.rainhas:
        continue
      self.rainhas.append(rainha)
    self.montaMatriz()
  
  def executa(self): #Faz a movimentação de cada rainha atualizando o custo total do tabuleiro
    for rainha in self.rainhas:
      self.HillClimbing(rainha)
      self.calculaCusto()
      self.estados.append(self.custo)#Adiciona o novo custo na lista de estados
      self.maxInt += 1
    if self.custo == 0 or self.maxInt >= 100:
      return self.custo #Retorna o custo atual
    else:
      self.executa()

  def verificaRainha(self,Rainha):
    risco = 0
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
  
  def HillClimbing(self,rainha):
    while(True):
      self.iteracoes += 1
      linhaCandidata = random.randint(0,self.numRainhas-1)
      candidata = Rainha(linhaCandidata,rainha.coluna)
      self.verificaRainha(candidata)
      if candidata.risco > rainha.risco or rainha.risco == 0: #Se a candidata tiver um custo maior que a atual, ele para o laço, portanto para a função também
        break
      rainha.linha = candidata.linha
      rainha.coluna = candidata.coluna
      self.verificaRainha(rainha)#Faz a troca de posição e recalcula o novo custo

  def montaMatriz(self): #Uma função para printar uma matriz representativa do tabuleiro
    matrizR = np.zeros([self.numRainhas,self.numRainhas],dtype = int)
    for rainha in self.rainhas:
      matrizR[rainha.linha][rainha.coluna] = 1
    print(matrizR)
  
  def calculaCusto(self):
    custo = 0
    for i in self.rainhas:
      self.verificaRainha(i)
      custo += i.risco
    self.custo = custo