from Animal import Animal

class Canino(Animal):
  def __init__(self, garras: bool):
    self.garrasExpostas = garras

  def uivar(self):
    print(f'{self.nome} uivou!')

  def rosnar(self):
    print(f'{self.nome} rosnou!')