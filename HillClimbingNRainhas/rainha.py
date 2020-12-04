class Rainha(object):
  def __init__(self,linha,coluna):
    self.linha = linha
    self.coluna = coluna
    self.risco = 0
    self.valor = 1
    self.movimentos = 0

  def __repr__(self):
      return(str(self.valor))