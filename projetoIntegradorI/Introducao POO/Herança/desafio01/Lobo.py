from Canino import Canino

class Lobo(Canino):
  def __init__(self, carnivoro: bool):
    self.carnivoro = carnivoro

  def construirMatilha(self):
    print(f'{self.nome} fez matilha!')