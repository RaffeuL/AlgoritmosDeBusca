from tab import Tabuleiro
import math
class Individuo(object):
  def __init__(self):
    self.tabuleiro = Tabuleiro(8)
    self.tabuleiro.criaTabuleiro()
    #self.tabuleiro.criaTabuleiroPerfeito()
    self.cromossomos = []
    self.geraCromossomo()
    self.fitness = None
    self.calculaFitness()

  def __repr__(self):
    return(str(self.fitness))  

  def geraCromossomo(self):
    for rainha in self.tabuleiro.rainhas:
      linha = bin(rainha.linha)[2:]
      self.cromossomos.append(linha)
  
  def calculaFitness(self):
    self.tabuleiro.calculaCusto()
    custoMax = int(math.factorial(8)/(2*math.factorial(8-2)))
    custo = self.tabuleiro.custo
    fitness = custoMax - custo
    self.fitness = fitness
