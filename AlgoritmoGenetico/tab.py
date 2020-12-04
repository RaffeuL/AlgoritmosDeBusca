import numpy as np
import random
from rainha import Rainha

class Tabuleiro(object):
  def __init__(self,NumRainhas):
    self.numRainhas = NumRainhas
    self.custo = 0 #Custo total do tabuleiro
    self.rainhas = []
    self.estados = []
  
  def criaTabuleiro(self): #Uma rainha em cada coluna mas a linha é aleatoria
    for x in range(self.numRainhas):
      linha = random.randint(0,self.numRainhas-1)
      rainha = Rainha(linha,x)
      self.rainhas.append(rainha)
    for rainha in self.rainhas: #Atualiza o custo de todas as rainhas logo depois de criar o tabuleiro
      self.verificaRainha(rainha)
    self.calculaCusto()
    self.estados.append(self.custo)

  def criaTabuleiroPerfeito(self): #Cria um tabuleiro com tudo nuuma linha
    rainha = Rainha(6,0)
    self.rainhas.append(rainha)
    rainha = Rainha(4,1)
    self.rainhas.append(rainha)
    rainha = Rainha(2,2)
    self.rainhas.append(rainha)
    rainha = Rainha(0,3)
    self.rainhas.append(rainha)
    rainha = Rainha(5,4)
    self.rainhas.append(rainha)
    rainha = Rainha(7,5)
    self.rainhas.append(rainha)
    rainha = Rainha(1,6)
    self.rainhas.append(rainha)
    rainha = Rainha(3,7)
    self.rainhas.append(rainha)
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
      self.moveRainha(rainha)
      self.calculaCusto()
      print(self.custo)
      self.estados.append(self.custo)#Adiciona o novo custo na lista de estados

    print("="*100)
    print("CUSTO DA MATRIZ: ",self.custo)
    
    print("#"*100)
    return self.custo #Retorna o custo atual

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
    self.custo = int(custo/2)

  