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
 
#como no slide da aula dizia que o fitness deve retornar valores melhores para individuos melhores, decidimos transformar o problema em maximização 
  def calculaFitness(self): 
    self.tabuleiro.calculaCusto()
    custoMax = int(math.factorial(8)/(2*math.factorial(8-2))) #calculo do custo maximo de ataques possivel
    custo = self.tabuleiro.custo 
    fitness = custoMax - custo #quanto maior o fitness, menos ataques entre pares de rainhas
    self.fitness = fitness
