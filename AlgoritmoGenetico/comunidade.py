from tab import *
import operator
import random
import math
import copy as cp
from individuo import Individuo 

class Comunidade(object):
  def __init__(self, n):
    self.individuos = []
    self.geraComunidadeInicial(n) #Gera uma comunidade inicial com n sendo a população
    self.ordenaFitness()

  def mostraIndividuos(self):
    for i in self.individuos:
      print(i, end="->")
      
  def ordenaFitness(self): #Ordena os fitness, colocando os piores para o inicio
    self.individuos.sort(key=operator.attrgetter('fitness'))

  def geraComunidadeInicial(self,n):
    print("+"*20,"Comunidade Inicial","+"*20)
    for i in range(n):
      individuo = Individuo() 
      self.individuos.append(individuo)

  def geraComunidade(self): #Gerando uma nova comunidade a partir da antiga
    novosIndividuos = []
    i = 0
    #print("+"*20, "Etapa de Cruzamento","+"*20)
    while (i+1)<=(len(self.individuos)-1):
      novoInd = self.cruzar(self.individuos[i],self.individuos[i+1])
      if novoInd != None: #Se gerar filhos ele faz toda a operação
        print("casal:",i,"+",i+1)
        filho1 = novoInd[0]
        print("")
        print("Filho 1:",filho1)
        filho2 = novoInd[1]
        print("Filho 2:",filho2)
        print("")
        novosIndividuos.append(filho1) #Uma lista com os novos individuos
        novosIndividuos.append(filho2)
        i = i+2
      else:
        i = i+2
    corte = 20-len(novosIndividuos) #Tratamento para a quantidade de individuos permaner a mesma (20) caso não gere filhos o suficiente
    self.ordenaFitness()
    novosIndividuos.sort(key=operator.attrgetter('fitness'))
    if len(novosIndividuos) == 20:
      novosIndividuos.insert(0,self.individuos[-1]) #Se todos os pais
    else:
      for i in range(corte):
        novosIndividuos.append(self.individuos[-(i+1)])
    self.individuos = novosIndividuos
    self.ordenaFitness()
    if self.verificaMelhor() == True: return True
    print("+"*20,"Comunidade Atual","+"*20)
    print(self.individuos)

  def cruzar(self,pai,mae):
    taxaDoCruzamento = random.randint(0,100)
    if taxaDoCruzamento >= 80: #Se não houver cruzamente ele retorna vazio
      return None
    corte = random.randint(1,7) #Pega aonde vai ser o corte
    print("")
    print("Corte do cromossomo: ",corte)
    filho1 = Individuo()
    filho2 = Individuo()
    filho1.tabuleiro.rainhas.clear()
    filho2.tabuleiro.rainhas.clear() #Limpa as listas pois sempre que um individuo é iniciado ele ja começa com um tabueiro pronto
    filho1.cromossomos.clear()
    filho2.cromossomos.clear()
    for cromossomo in range(0,corte): #Do 0 até o corte do pai
      rainhaPai = cp.deepcopy(pai.tabuleiro.rainhas[cromossomo])
      rainhaMae = cp.deepcopy(mae.tabuleiro.rainhas[cromossomo])
      filho1.tabuleiro.rainhas.append(rainhaPai)
      filho2.tabuleiro.rainhas.append(rainhaMae) #Faz a mesclagem dos pais para os filhos
    for cromossomo in range(corte,8): #Do corte até o fim, pra mãe
      rainhaPai = cp.deepcopy(pai.tabuleiro.rainhas[cromossomo])
      rainhaMae = cp.deepcopy(mae.tabuleiro.rainhas[cromossomo])
      filho1.tabuleiro.rainhas.append(rainhaMae)
      filho2.tabuleiro.rainhas.append(rainhaPai)
    print("")
    print("Cromossomos do pai:",pai.cromossomos)
    print("Cromossomos da mae:",mae.cromossomos)
    print("")
    taxaDeMutacao = 3
    chance1 = random.randint(0,100) #Pega um número entre 0 e 100, se for menor ou igual a 3 ele muta
    print("Chance do Filho 1:",chance1)
    if chance1 <= taxaDeMutacao:
      filho1 = self.mutacao(filho1)
    chance2 = random.randint(0,100)
    print("Chance do Filho 2:",chance2)
    if chance2 <= taxaDeMutacao:
      filho2 = self.mutacao(filho2)
    filho1.geraCromossomo()
    filho2.geraCromossomo() #Gerando a lista de cromossomos com as novas rainhas
    filho1.calculaFitness() #Calculando os fitness dos filhos
    filho2.calculaFitness()
    print("")
    print("Filho 1:",filho1.fitness)
    print("Filho 2:",filho2.fitness)
    print("")
    filhos = [filho1, filho2]
    return filhos

  def mutacao(self,individuo):
    rainhaAfetada = random.randint(0,7) #Gera o número da coluna que será afetada
    print("")
    print("SOFREU MUTAÇÃO NA COLUNA",rainhaAfetada+1)
    print("")
    individuo.tabuleiro.rainhas[rainhaAfetada].linha = random.randint(0,7) #Muda pra uma linha aleatória
    return individuo

  def verificaMelhor(self): #Verifica se o melhor individuo possível foi gerado
    if self.individuos[-1].fitness==28:
      print("="*20,"Melhor Individuo Encontrado","="*20)
      print("Comossomo:",self.individuos[-1].cromossomos)
      print("fitness:", self.individuos[-1])
      print("Solução:")
      self.individuos[-1].tabuleiro.montaMatriz()
      return True
    return False
